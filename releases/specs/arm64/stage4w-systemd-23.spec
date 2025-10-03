subarch: arm64
target: stage4
version_stamp: wsl-systemd-@TIMESTAMP@
rel_type: 23.0-default
profile: default/linux/arm64/23.0/desktop/systemd
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-arm64-desktop-systemd-@TIMESTAMP@.tar.xz
compression_mode: pixz
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
binrepo_path: arm64/binpackages/23.0/arm64

stage4/use:
	-passwdqc
	video_cards_d3d12

stage4/packages:
	media-libs/mesa
	sys-apps/gentoo-wsl-config
	sys-auth/pambase

stage4/fsscript: @REPO_DIR@/releases/scripts/wsl.sh
