#!/usr/bin/env

# """
# SUBLIME TEXT 2 build system:
# {
#     "cmd": ["bash","/Users/grahamcrowell/run_me.sh", "$file"]
# }
# """

echo sublime_build batch script: 
echo 	$0

echo argument: 
echo 	$1

# echo "welcome to my bash redirector"

# python=/usr/local/bin/python
# mysql="/usr/local/mysql-5.6.23-osx10.8-x86_64/bin/mysql -h localhost -u quant -p2and2is5 stock_stat"
#  # -h "localhost" -u "quant" -p2and2is5 "stock_stat"'
# qmlviewer=/usr/local/Cellar/qt/4.8.6/QMLViewer.app
# pyside_uic=/usr/local/bin/pyside-uic
# qmake="/usr/local/Cellar/qt5/5.4.1/bin/qmake"
# tex_bin_dir=/usr/texbin
# latex=$tex_bin_dir/pdflatex
# preview="/usr/bin/qlmanage -p"
# browser="/Applications/Safari.app/Contents/MacOS/Safari"

# ext="${1##*.}"
# fullname="${1##*/}"
# name="${fullname%%.*}"
# dirpath="${1%/*}"
# parentpath="${dirpath%/*}"
# dirname="${dirpath##*/}"



# printf "* fullpath: %s\n\tdirpath: %s\n\tparentpath: %s\n\tdirname: %s\n\tfullname: %s\n\tname: %s\n\text: %s\n" $1 $dirpath $parentpath $dirname $fullname $name $ext
# printf " - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"

# # LaTeX variables
# main_latex="$dirpath/main.tex"
# pymake=/Users/grahamcrowell/Dropbox/github_local/sublime_build_redirect/pymake_latex/pymake_latex.py
# latex_template_dir=/Users/grahamcrowell/Dropbox/TEMPLATES/LaTeX/
# latex_template_std="LaTeX_template copy.tex"
# bib_template=myrefs.bib



# # echo $0
# # echo "extension is $ext"
# # echo "name is $name"
# # echo "${1%%.*}"
# # echo "${1%.*}"
# # echo "${1#*.}"
# # echo "${1##*.}"
# # echo "${1##*/}"
# # echo "${1%/*}"
# # echo
# # echo


# function typeset {
# 	$latex "$main_latex"
# }

# function starting_message {
# 	echo "--------------------------------"
# 	echo
# 	echo
# }
# function build_qt {
# 	echo "Qt5 project detected"
# 	$qmake $dirpath/$dirname.pro -r -spec macx-g++ CONFIG+=x86_64
# 	# check if make failed
# 	if [ "$?" != 0 ]
# 	then
# 		echo "ERROR qmake failed (error code $?)"
# 		exit "$?"
# 	fi
# 	make
# 	# check if make failed
# 	if [ "$?" != 0 ]
# 	then
# 		echo "ERROR make failed (error code $?)"
# 		exit $?
# 	else
# 		echo "executing . . ."
# 		open $dirname.app
# 	fi
# 	# make clean
# 	# rm -f .qmake.stash
# }
# function build_cpp {
# 	echo "cpp project detected"
# 	# execute make on project
# 	make
# 	# check if make failed
# 	if [ "$?" != 0 ]
# 	then
# 		echo "ERROR make failed (error code $?)"
# 		exit $?
# 	else
# 		echo "executing . . ."
# 		./main
# 	fi
# }

# # files=(*.zip)
# # echo ${#files[*]}
# # files=(*.cpp)
# # echo ${#files[*]}
# # make array (http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_10_02.html)
# # cpp_exts=(log zip cpp h)
# # qt_exts=(pro qml)
# # for cpp_ext in ${qt_exts[@]}; do
# # 	echo ${cpp_ext}
# # 	tmp=${cpp_ext}
# # 	files=(*.$tmp)
# # 	# echo ${#files[*]}
# # 	# echo ${files[0]}
# # 	if [ ${files[0]} != "*.$tmp" ]
# # 	then
# # 		echo "file with $tmp exists"
# # 	fi
# # done



# if [ "$ext" = "py" ]
# then
# 	echo
# 	echo "python script detected"
# 	starting_message
# 	$python "$1"
# elif [ "$ext" = "sql" ]
# then
# 	echo "MySQL script"
# 	# $sql < $1
# 	# /Users/grahamcrowell/Dropbox/github_local/pyfolio/src/stock_stat_ddl.sql
# 	# $sql <
# 	echo
# 	echo
# 	$mysql < "$1"
# elif [ "$ext" = "sh" ]
# then
# 	echo "bash script detected"
# 	if [ "$name" = "run_me" ]
# 	then
# 		echo "ERROR: run_me called itself"
# 		exit 0
# 	fi
# 	echo
# 	echo
# 	chmod 777 "$1"
# 	"$1"
# elif [ "$ext" = "tex" ]
# then
# 	echo "latex project detected $pwd"

# 	# if [ -f "$main_latex" ]
# 	#
# 	# then
# 	# 	echo "main.tex exists"
# 	# 	typeset
# 	# else
# 	# 	$python $pymake "$1"
# 	# fi
# 	# if [ -f  ]
# 	echo
# 	echo
# 	$python -O $pymake "$1"
# elif [ -f "$dirpath/$dirname.pro" ]
# then
# 	echo "Qt project file found: $dirpath/$dirname.pro . . ."
# 	build_qt
# elif [ "$ext" = "cpp" ] || [ "$ext" = "h" ] || [ "$name" = "makefile" ]
# then
# 	build_cpp
# elif [ "$ext" = "qml" ]
# then
# 	echo "Qt/QML project detected"
# 	echo
# 	echo
# 	open -a $qmlviewer "$1"
# 	# $python -O /Users/grahamcrowell/Dropbox/pymake/pymake_latex/pymake_latex.py $1
# elif [ "$ext" = "ui" ]
# then
# 	echo "Qt Designer UI project detected (converting with pyside_uic)"
# 	echo
# 	echo
# 	$pyside_uic "$1" -o "$dirpath$name.py"
# 	open -a $qmlviewer "$dirpath$name.py"
# elif [ "$ext" = "r" ]
# then
# 	echo "R script detected"
# 	RScript "$1"
# 	if [ -f "Rplots.pdf" ]
# 	then
# 		if [ "Rplots.pdf" -nt "$1" ]
# 		then
# 			$preview "Rplots.pdf"
# 		fi
# 	fi
# elif [ "$ext" = "svg" ]
# then
# 	echo "SVG detected"
# 	if [ -f "$dirpath/index.html" ]
# 	then
# 		echo "index.html detected opening webpage"
# 		$browser "$dirpath/index.html"
# 	else
# 		$browser "$1"
# 	fi

# elif [ "$ext" = "js" ]
# then
# 	echo "javascript detected"
# 	if [ -f "$dirpath/index.html" ]
# 	then
# 		$browser "$dirpath/index.html"
# 		# TODO: execute javascript is a console
# 	else
# 		echo "ERROR: index.html not found"
# 		# TODO: execute javascript is a console
# 		exit 1
# 	fi

# elif [ "$ext" = "html" ]
# then
# 	echo "HTML webpage detected"
# 	$browser "$1"
# else
# 	printf "ERROR invalid filename:\nrun_me.sh doesn't handle: $1"
# fi

# echo
# echo
# echo "EXECUTION COMPLETE"
# echo $date
# # echo $0
# # echo $1
# # ext="${arg#*.}"
# # echo $ext
