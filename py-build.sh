current_dir=$(realpath "$(dirname "$0")")
pushd $current_dir
rm -fr ./dist/*
python -m build
popd