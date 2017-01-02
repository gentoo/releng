MUSL_DIR="$( cd "$( dirname ${BASH_SOURCE[0]} )" && pwd )"
cp "${MUSL_DIR}"/stage4-hardened-amd64.spec "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec
sed -i "s|@REPO_DIR@|${MUSL_DIR}|g" "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec

catalyst -f "${MUSL_DIR}"/stage4-hardened-amd64-configured.spec | tee -a "${MUSL_DIR}"/zzz.log
