subarch: amd64
target: stage4
version_stamp: wsl-openrc-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/amd64/23.0/desktop
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-amd64-desktop-openrc-@TIMESTAMP@.tar.xz
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
binrepo_path: amd64/binpackages/23.0/x86-64

stage4/use:
	-passwdqc
	video_cards_d3d12

stage4/packages:
	media-libs/mesa
	sys-apps/gentoo-wsl-config
	sys-auth/pambase

stage4/fsscript: @REPO_DIR@/releases/scripts/wsl.sh
