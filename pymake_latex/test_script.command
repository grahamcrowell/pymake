pymake_latex="/Users/grahamcrowell/Dropbox/DOCS/eclipse_workspace/pymake_latex/pymake_latex.py"

test_project0="/Users/grahamcrowell/Dropbox/DOCS/MISC/resume/tester resume.finance.2014-05-14 copy/the_straight_goods.tex"
test_project1="/Users/grahamcrowell/Dropbox/DOCS/MISC/resume/tester resume.finance.2014-05-14 copy/main.tex"
test_project2="/Users/grahamcrowell/Dropbox/DOCS/MISC/resume/tester resume.finance.2014-05-14 copy"

latex_src="the_straight_goods.tex"

cd "$test_project2"

python -O "$pymake_latex" "$test_project0"


