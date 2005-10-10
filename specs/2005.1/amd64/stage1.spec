# $Id: stage1.spec,v 1.1 2005-10-10 19:07:10 kugelfang Exp $

subarch: amd64
version_stamp: 2005.1
target: stage1
rel_type: default
rel_verson: 2005.1
profile: default-linux/amd64/2005.1
snapshot: official
source_subpath: default/stage3-amd64-2005.0

distcc_hosts:
	pitr-int/2 localhost
