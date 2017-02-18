#!/usr/bin/env
printf "sublime_build batch script: %s" $0
printf "argument: %s" $1
python_version="$(python -c 'import sys; print(".".join(map(str,sys.version_info[:])))')"
printf "python version: %s" $python_version
python ~/Dropbox/sublime_config/pymake.py $1 $2