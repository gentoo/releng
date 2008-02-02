# $Id: stage3.spec,v 1.1 2005-10-10 19:07:10 kugelfang Exp $

subarch: amd64
version_stamp: 2005.1
target: stage3
rel_type: default
rel_version: 2005.1
profile: default-linux/amd64/2005.1
snapshot: official
source_subpath: default/stage2-amd64-2005.1

distcc_hosts:
	pitr-int/2 localhost
