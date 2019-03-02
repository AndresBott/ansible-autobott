#!/usr/bin/env bash
# this scrip assumes to be in a sub-folder of the ansible project, path handling could be improved

command -v ansible-autodoc >/dev/null 2>&1 || { echo >&2 "I require ansible-autodoc but it's not installed.  Aborting."; exit 1; }

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOTDIR=`realpath "$DIR/.."`

echo "ROLES: "
for d in $ROOTDIR/roles/*/
do
if [ -d "$d" ]; then

    ( cd "$d" && echo "$d" && ansible-autodoc -y )

fi
done
