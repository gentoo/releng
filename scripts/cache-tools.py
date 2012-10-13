#!/usr/bin/env python
# Copyright 1999-2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $
#
# Zac Medico <zmedico@gentoo.org>
#

import errno, fpformat, os, sys, time

if not hasattr(__builtins__, "set"):
	from sets import Set as set
from itertools import chain

def create_syncronized_func(myfunc, mylock):
	def newfunc(*pargs, **kwargs):
		mylock.acquire()
		try:
			myfunc(*pargs, **kwargs)
		finally:
			mylock.release()
	return myfunc

class ConsoleUpdate(object):

	_synchronized_methods = ["append", "carriageReturn",
		"newLine", "reset", "update"]

	def __init__(self):
		self.offset = 0
		import sys
		self.stream = sys.stdout
		self.quiet = False
		import threading
		self._lock = threading.RLock()
		for method_name in self._synchronized_methods:
			myfunc = create_syncronized_func(
				getattr(self, method_name), self._lock)
			setattr(self, method_name, myfunc)
		# ANSI code that clears from the cursor to the end of the line
		self._CLEAR_EOL = None
		try:
			import curses
			try:
				curses.setupterm()
				self._CLEAR_EOL = curses.tigetstr('el')
			except curses.error:
				pass
		except ImportError:
			pass
		if not self._CLEAR_EOL:
			self._CLEAR_EOL = '\x1b[K'

	def acquire(self, **kwargs):
		return self._lock.acquire(**kwargs)

	def release(self):
		self._lock.release()

	def reset(self):
		self.offset = 0

	def carriageReturn(self):
		if not self.quiet:
			self.stream.write("\r")
			self.stream.write(self._CLEAR_EOL)
			self.offset = 0

	def newLine(self):
		if not self.quiet:
			self.stream.write("\n")
			self.stream.flush()
			self.reset()

	def update(self, msg):
		if not self.quiet:
			self.carriageReturn()
			self.append(msg)

	def append(self, msg):
		if not self.quiet:
			self.offset += len(msg)
			self.stream.write(msg)
			self.stream.flush()

class ProgressCounter(object):
	def __init__(self):
		self.total = 0
		self.current = 0

class ProgressAnalyzer(ProgressCounter):
	def __init__(self):
		self.start_time = time.time()
		self.currentTime = self.start_time
		self._samples = []
		self.sampleCount = 20
	def percentage(self, digs=0):
		if self.total > 0:
			float_percent = 100 * float(self.current) / float(self.total)
		else:
			float_percent = 0.0
		return fpformat.fix(float_percent,digs)
	def totalTime(self):
		self._samples.append((self.currentTime, self.current))
		while len(self._samples) > self.sampleCount:
			self._samples.pop(0)
		prev_time, prev_count = self._samples[0]
		time_delta = self.currentTime - prev_time
		if time_delta > 0:
			rate = (self.current - prev_count) / time_delta
			if rate > 0:
				return self.total / rate
		return 0
	def remaining_time(self):
		return self.totalTime() - self.elapsed_time()
	def elapsed_time(self):
		return self.currentTime - self.start_time

class ConsoleProgress(object):
	def __init__(self, name="Progress", console=None):
		self.name = name
		self.analyzer = ProgressAnalyzer()
		if console is None:
			self.console = ConsoleUpdate()
		else:
			self.console = console
		self.time_format="%H:%M:%S"
		self.quiet = False
		self.lastUpdate = 0
		self.latency = 0.5

	def formatTime(self, t):
		return time.strftime(self.time_format, time.gmtime(t))

	def displayProgress(self, current, total):
		if self.quiet:
			return

		self.analyzer.currentTime = time.time()
		if self.analyzer.currentTime - self.lastUpdate < self.latency:
			return
		self.lastUpdate = self.analyzer.currentTime
		self.analyzer.current = current
		self.analyzer.total = total

		output = ((self.name, self.analyzer.percentage(1).rjust(4) + "%"),
		("Elapsed", self.formatTime(self.analyzer.elapsed_time())),
		("Remaining", self.formatTime(self.analyzer.remaining_time())),
		("Total", self.formatTime(self.analyzer.totalTime())))
		self.console.update(" ".join([ x[0] + ": " + x[1] for x in output ]))

class ProgressHandler(object):
	def __init__(self):
		self.curval = 0
		self.maxval = 0
		self.last_update = 0
		self.min_display_latency = 0.2

	def onProgress(self, maxval, curval):
		self.maxval = maxval
		self.curval = curval
		cur_time = time.time()
		if cur_time - self.last_update >= self.min_display_latency:
			self.last_update = cur_time
			self.display()

	def display(self):
		raise NotImplementedError(self)

def open_file(filename=None):
	if filename is None:
		f = sys.stderr
	elif filename == "-":
		f = sys.stdout
	else:
		try:
			filename = os.path.expanduser(filename)
			f = open(filename, "a")
		except (IOError, OSError), e:
			sys.stderr.write("%s\n" % e)
			sys.exit(e.errno)
	return f

def create_log(name="", logfile=None, loglevel=0):
	import logging
	log = logging.getLogger(name)
	log.setLevel(loglevel)
	handler = logging.StreamHandler(open_file(logfile))
	handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
	log.addHandler(handler)
	return log

def is_interrupt(e):
	if isinstance(e, (SystemExit, KeyboardInterrupt)):
		return True
	return hasattr(e, "errno") and e.errno == errno.EINTR

def mirror_cache(valid_nodes_iterable, src_cache, trg_cache, log,
	eclass_cache, cleanse_on_transfer_failure):

	cleanse_candidates = set(trg_cache.iterkeys())
	update_count = 0

	# Since the loop below is mission critical, we continue after *any*
	# exception that is not an interrupt.

	for x in valid_nodes_iterable:
		log.debug("%s mirroring" % x)
		if not cleanse_on_transfer_failure:
			cleanse_candidates.discard(x)

		try:
			entry = copy_dict(src_cache[x])
		except KeyError, e:
			log.error("%s missing source: %s" % (x, str(e)))
			del e
			continue
		except Exception, e:
			if is_interrupt(e):
				raise
			log.error("%s reading source: %s" % (x, str(e)))
			del e
			continue

		write_it = True
		trg = None

		try:
			trg = copy_dict(trg_cache[x])
			if long(trg["_mtime_"]) == long(entry["_mtime_"]) and \
				eclass_cache.is_eclass_data_valid(trg["_eclasses_"]) and \
				set(trg["_eclasses_"]) == set(entry["_eclasses_"]):
				write_it = False
		except KeyError:
			pass
		except Exception, e:
			if is_interrupt(e):
				raise
			log.error("%s reading target: %s" % (x, str(e)))
			del e

		if trg and not write_it:
			""" We don't want to skip the write unless we're really sure that
			the existing cache is identical, so don't trust _mtime_ and
			_eclasses_ alone."""
			for d in (entry, trg):
				if "EAPI" in d and d["EAPI"] in ("", "0"):
					del d["EAPI"]
			for k in set(chain(entry, trg)).difference(
				("_mtime_", "_eclasses_")):
				if trg.get(k, "") != entry.get(k, ""):
					write_it = True
					break

		if write_it:
			update_count += 1
			log.info("%s transferring" % x)
			inherited = entry.get("INHERITED", None)
			if inherited:
				if src_cache.complete_eclass_entries:
					if not "_eclasses_" in entry:
						log.error("%s missing _eclasses_" % x)
						continue
					if not eclass_cache.is_eclass_data_valid(entry["_eclasses_"]):
						log.error("%s stale _eclasses_" % x)
						continue
				else:
					entry["_eclasses_"] = eclass_cache.get_eclass_data(entry["INHERITED"].split(), \
						from_master_only=True)
					if not entry["_eclasses_"]:
						log.error("%s stale _eclasses_" % x)
						continue
			try:
				trg_cache[x] = entry
				cleanse_candidates.discard(x)
			except Exception, e:
				if is_interrupt(e):
					raise
				log.error("%s writing target: %s" % (x, str(e)))
				del e
		else:
			cleanse_candidates.discard(x)

	if not trg_cache.autocommits:
		try:
			trg_cache.commit()
		except Exception, e:
			if is_interrupt(e):
				raise
			log.error("committing target: %s" % str(e))
			del e

	return update_count, cleanse_candidates

def copy_dict(src, dest=None):
	"""Some cache implementations throw cache errors when accessing the values.
	We grab all the values at once here so that we don't have to be concerned
	about exceptions later."""
	if dest is None:
		dest = {}
	for k, v in src.iteritems():
		dest[k] = v
	return dest

class ListPackages(object):
	def __init__(self, portdb, log, shuffle=False):
		self._portdb = portdb
		self._log = log
		self._shuffle = shuffle

	def run(self):
		log = self._log
		cp_list = self._portdb.cp_list
		cp_all = self._portdb.cp_all()
		if self._shuffle:
			from random import shuffle
			shuffle(cp_all)
		else:
			cp_all.sort()
		cpv_all = []
		# Since the loop below is mission critical, we continue after *any*
		# exception that is not an interrupt.
		for cp in cp_all:
			log.debug("%s cp_list" % cp)
			try:
				cpv_all.extend(cp_list(cp))
			except Exception, e:
				if is_interrupt(e):
					raise
				self._log.error("%s cp_list: %s" % (cp, str(e)))

		self.cpv_all = cpv_all

class MetadataGenerate(object):
	"""When cache generation fails for some reason, cleanse the stale cache
	entry if it exists.  This prevents the master mirror from distributing
	stale cache, and will allow clients to safely assume that all cache is
	valid.  The mtime requirement is especially annoying due to bug #139134
	(timestamps of cache entries don't change when an eclass changes) and the
	interaction of timestamps with rsync."""
	def __init__(self, portdb, cpv_all, log):
		self._portdb = portdb
		self._cpv_all = cpv_all
		self._log = log

	def run(self, onProgress=None):
		log = self._log
		portdb = self._portdb
		cpv_all = self._cpv_all
		auxdb = portdb.auxdb[portdb.porttree_root]
		cleanse_candidates = set(auxdb.iterkeys())

		# Since the loop below is mission critical, we continue after *any*
		# exception that is not an interrupt.
		maxval = len(cpv_all)
		curval = 0
		if onProgress:
			onProgress(maxval, curval)
		while cpv_all:
			cpv = cpv_all.pop(0)
			log.debug("%s generating" % cpv)
			try:
				portdb.aux_get(cpv, ["EAPI"])
				# Cleanse if the above doesn't succeed (prevent clients from
				# receiving stale cache, and let them assume it is valid).
				cleanse_candidates.discard(cpv)
			except Exception, e:
				if is_interrupt(e):
					raise
				log.error("%s generating: %s" % (cpv, str(e)))
				del e
			curval += 1
			if onProgress:
				onProgress(maxval, curval)

		self.target_cache = auxdb
		self.dead_nodes = cleanse_candidates

class MetadataTransfer(object):
	def __init__(self, portdb, cpv_all, forward, cleanse_on_transfer_failure,
		log):
		self._portdb = portdb
		self._cpv_all = cpv_all
		self._log = log
		self._forward = forward
		self._cleanse_on_transfer_failure = cleanse_on_transfer_failure

	def run(self, onProgress=None):
		log = self._log
		portdb = self._portdb
		cpv_all = self._cpv_all
		aux_cache = portdb.auxdb[portdb.porttree_root]
		import portage
		auxdbkeys = portage.auxdbkeys[:]
		metadbmodule = portdb.mysettings.load_best_module("portdbapi.metadbmodule")
		portdir_cache = metadbmodule(portdb.porttree_root, "metadata/cache",
			auxdbkeys)

		maxval = len(cpv_all)
		curval = 0
		if onProgress:
			onProgress(maxval, curval)
		class pkg_iter(object):
			def __init__(self, pkg_list, onProgress=None):
				self.pkg_list = pkg_list
				self.maxval = len(pkg_list)
				self.curval = 0
				self.onProgress = onProgress
			def __iter__(self):
				while self.pkg_list:
					yield self.pkg_list.pop()
					self.curval += 1
					if self.onProgress:
						self.onProgress(self.maxval, self.curval)

		if self._forward:
			src_cache = portdir_cache
			trg_cache = aux_cache
		else:
			src_cache = aux_cache
			trg_cache = portdir_cache

		""" This encapsulates validation of eclass timestamps and also fills in
		missing data (mtimes and/or paths) as necessary for the given cache
		format."""
		eclass_cache = portage.eclass_cache.cache(portdb.porttree_root)

		if not trg_cache.autocommits:
			trg_cache.sync(100)

		self.target_cache = trg_cache
		self.update_count, self.dead_nodes = mirror_cache(
			pkg_iter(cpv_all, onProgress=onProgress),
			src_cache, trg_cache, log, eclass_cache,
			self._cleanse_on_transfer_failure)

class CacheCleanse(object):
	def __init__(self, auxdb, dead_nodes, log):
		self._auxdb = auxdb
		self._dead_nodes = dead_nodes
		self._log = log
	def run(self):
		auxdb = self._auxdb
		log = self._log
		for cpv in self._dead_nodes:
			try:
				log.info("%s cleansing" % cpv)
				del auxdb[cpv]
			except Exception, e:
				if is_interrupt(e):
					raise
				log.error("%s cleansing: %s" % (cpv, str(e)))
				del e

def import_portage():
	try:
		from portage import data as portage_data
	except ImportError:
		import portage_data
	# If we're not already root or in the portage group, we make the gid of the
	# current process become portage_gid.
	if os.getgid() != 0 and portage_data.portage_gid not in os.getgroups():
		portage_data.portage_gid = os.getgid()
		portage_data.secpass = 1

	os.environ["PORTAGE_LEGACY_GLOBALS"] = "false"
	import portage
	del os.environ["PORTAGE_LEGACY_GLOBALS"]
	return portage

def create_portdb(portdir=None, cachedir=None, config_root=None,
	target_root=None, profile=None, **kwargs):

	if cachedir is not None:
		os.environ["PORTAGE_DEPCACHEDIR"] = cachedir
	if config_root is None:
		config_root = os.environ.get("PORTAGE_CONFIGROOT", "/")
	if target_root is None:
		target_root = os.environ.get("ROOT", "/")
	if profile is None:
		profile = ""

	portage = import_portage()
	try:
		from portage import const as portage_const
	except ImportError:
		import portage_const

	# Disable overlays because we only generate metadata for the main repo.
	os.environ["PORTDIR_OVERLAY"] = ""
	conf = portage.config(config_profile_path=profile,
		config_incrementals=portage_const.INCREMENTALS,
		target_root=target_root,
		config_root=config_root)

	if portdir is None:
		portdir = conf["PORTDIR"]

	# The cannonical path is the key for portdb.auxdb.
	portdir = os.path.realpath(portdir)
	conf["PORTDIR"] = portdir
	conf.backup_changes("PORTDIR")

	portdb = portage.portdbapi(portdir,
		mysettings=conf)

	return portdb

def parse_args(myargv):
	description = "This program will ensure that the metadata cache is up to date for entire portage tree."
	usage = "usage: cache-tools [options] --generate || --transfer"
	from optparse import OptionParser
	parser = OptionParser(description=description, usage=usage)
	parser.add_option("--portdir",
		help="location of the portage tree",
		dest="portdir")
	parser.add_option("--cachedir",
		help="location of the metadata cache",
		dest="cachedir")
	parser.add_option("--profile",
		help="location of the profile",
		dest="profile")
	parser.add_option("--generate",
		help="generate metadata as necessary to ensure that the cache is fully populated",
		action="store_true", dest="generate", default=False)
	parser.add_option("--shuffle",
		help="generate cache in random rather than sorted order (useful to prevent two separate instances from competing to generate metadata for the same packages simultaneously)",
		action="store_true", dest="shuffle", default=False)
	parser.add_option("--transfer",
		help="transfer metadata from portdir to cachedir or vice versa",
		action="store_true", dest="transfer", default=False)
	parser.add_option("--cleanse-on-transfer-failure",
		help="cleanse target cache when transfer fails for any reason (such as the source being unavailable)",
		action="store_true", dest="cleanse_on_transfer_failure", default=False)
	parser.add_option("--forward",
		help="forward metadata transfer flows from portdir to cachedir (default)",
		action="store_true", dest="forward", default=True)
	parser.add_option("--reverse",
		help="reverse metadata transfer flows from cachedir to portdir",
		action="store_false", dest="forward", default=True)
	parser.add_option("--logfile",
		help="send status messages to a file (default is stderr)",
		dest="logfile", default=None)
	parser.add_option("--loglevel",
		help="numeric log level (defauls to 0 and may range from 0 to 50 corresponding to the default levels of the python logging module)",
		dest="loglevel", default="0")
	parser.add_option("--reportfile",
		help="send a report to a file",
		dest="reportfile", default=None)
	parser.add_option("--spawn-outfile",
		help="redirect ouput of spawned processes to a file instead of stdout/stderr",
		dest="spawn_outfile", default=None)
	parser.add_option("--no-progress",
		action="store_false", dest="progress", default=True,
		help="disable progress output to tty")
	options, args = parser.parse_args(args=myargv)

	# Conversion to dict allows us to use **opts as function args later on.
	opts = {}
	all_options = ("portdir", "cachedir", "profile", "progress", "logfile",
		"loglevel", "generate", "transfer", "forward", "shuffle",
		"spawn_outfile", "reportfile", "cleanse_on_transfer_failure")
	for opt_name in all_options:
		v = getattr(options, opt_name)
		opts[opt_name] = v
	return opts

def run_command(args):
	opts = parse_args(sys.argv[1:])

	if opts["spawn_outfile"]:
		fd = os.dup(1)
		sys.stdout = os.fdopen(fd, 'w')
		fd = os.dup(2)
		sys.stderr = os.fdopen(fd, 'w')
		f = open_file(opts["spawn_outfile"])
		os.dup2(f.fileno(), 1)
		os.dup2(f.fileno(), 2)
		del fd, f

	console = ConsoleUpdate()
	if not opts["progress"] or not sys.stdout.isatty():
		console.quiet = True
	job = None
	import signal, thread, threading
	shutdown_initiated = threading.Event()
	shutdown_complete = threading.Event()
	def shutdown_console():
		console.acquire()
		try:
			console.update("Interrupted.")
			console.newLine()
			console.quiet = True
			shutdown_complete.set()
			# Kill the main thread if necessary.
			# This causes the SIGINT signal handler to be invoked in the
			# main thread.  The signal handler needs to be an actual
			# callable object (rather than something like signal.SIG_DFL)
			# in order to avoid TypeError: 'int' object is not callable.
			thread.interrupt_main()
			thread.exit()
		finally:
			console.release()

	def handle_interrupt(*args):
		if shutdown_complete.isSet():
			sys.exit(1)
		# Lock the console from a new thread so that the main thread is allowed
		# to cleanly complete any console interaction that may have been in
		# progress when this interrupt arrived.
		if not shutdown_initiated.isSet():
			thread.start_new_thread(shutdown_console, ())
			shutdown_initiated.set()

	signal.signal(signal.SIGINT, handle_interrupt)
	signal.signal(signal.SIGTERM, handle_interrupt)

	try:
		import datetime
		datestamp = str(datetime.datetime.now())
		time_begin = time.time()
		log = create_log(name="MetadataGenerate",
			logfile=opts["logfile"], loglevel=int(opts["loglevel"]))
		if opts["reportfile"]:
			reportfile = open_file(opts["reportfile"])
		portdb = create_portdb(**opts)
		try:
			os.nice(int(portdb.mysettings.get("PORTAGE_NICENESS", "0")))
		except (OSError, ValueError), e:
			log.error("PORTAGE_NICENESS failed: '%s'" % str(e))
			del e

		job = ListPackages(portdb, log, shuffle=opts["shuffle"])
		console.update("Listing packages in repository...")
		job.run()
		cpv_all = job.cpv_all
		total_count = len(cpv_all)
		if opts["generate"]:
			job = MetadataGenerate(portdb, cpv_all, log)
			name = "Cache generation"
			complete_msg = "Metadata generation is complete."
		elif opts["transfer"]:
			job = MetadataTransfer(portdb, cpv_all, opts["forward"],
			opts["cleanse_on_transfer_failure"], log)
			if opts["forward"]:
				name = "Forward transfer"
				complete_msg = "Forward metadata transfer is complete."
			else:
				name = "Reverse transfer"
				complete_msg = "Reverse metadata transfer is complete."
		else:
			sys.stderr.write("required options: --generate || --transfer\n")
			sys.exit(os.EX_USAGE)
		job.opts = opts

		onProgress = None
		if not console.quiet:
			ui = ConsoleProgress(name=name, console=console)
			progressHandler = ProgressHandler()
			onProgress = progressHandler.onProgress
			def display():
				ui.displayProgress(progressHandler.curval, progressHandler.maxval)
			progressHandler.display = display

		job.run(onProgress=onProgress)

		if not console.quiet:
			# make sure the final progress is displayed
			progressHandler.display()

		update_count = None
		if opts["transfer"]:
			update_count = job.update_count
		target_cache = job.target_cache
		dead_nodes = job.dead_nodes
		cleanse_count = len(dead_nodes)
		console.update("Cleansing cache...")
		job = CacheCleanse(target_cache, dead_nodes, log)
		job.run()
		console.update(complete_msg)
		console.newLine()
		time_end = time.time()
		if opts["reportfile"]:
			width = 20
			reportfile.write(name.ljust(width) + "%s\n" % datestamp)
			reportfile.write("Elapsed seconds".ljust(width) + "%f\n" % (time_end - time_begin))
			reportfile.write("Total packages".ljust(width) + "%i\n" % total_count)
			if update_count is not None:
				reportfile.write("Updated packages".ljust(width) + "%i\n" % update_count)
			reportfile.write("Cleansed packages".ljust(width) + "%i\n" % cleanse_count)
			reportfile.write(("-"*50)+"\n")
	except Exception, e:
		if not is_interrupt(e):
			raise
		del e
		handle_interrupt()
	sys.exit(0)

if __name__ == "__main__":
	run_command(sys.argv[1:])
