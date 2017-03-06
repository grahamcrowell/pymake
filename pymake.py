"""
	sublime text build system
	file extension determines execution how file is executed/built

"""
print('-----------------------------------------------------')
print('pymake.py built script\n\t{}'.format(__file__))

import sys, os, subprocess,time,sys
import pymake_latex

if 'linux' in sys.platform:
	browser = "firefox"
	pdflatex = "pdflatex"
	sql = lambda script_file: "mysql --user=root --password=2and2is5 < {0}".format(script_file)
else:
	browser = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe"
	pdflatex = "C:/Program Files/MiKTeX 2.9/miktex/bin/x64/pdflatex.exe"
	if not os.path.exists(pdflatex):
		print('{} not found.'.format(pdflatex))
		pdflatex = "pdflatex"
	powershell_ise = "c:/windows/system32/WindowsPowerShell/v1.0/PowerShell_ISE.exe"
	powershell = "c:/windows/system32/WindowsPowerShell/v1.0/powershell.exe"
	sql = lambda script_file: 'SQLCMD -S{} -E -dtempdb -i "{}"'.format('PC',script_file)
	md_html = lambda arg, dst: 'pandoc "{0}" --toc -f markdown -t html -s -o "{1}"'.format(arg,dst)
	md_pdf = lambda arg, dst: 'pandoc -S "{0}" -o "{1}"'.format(arg,dst)
	# sql = lambda script_file: '"C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\devenv.exe" "{}" /Edit'.format(script_file)

def execute(cmd):
	print('execute:\n\t{}\n- - - - - - - - - - - - - - - - - - - - - - - - - - - \n\n'.format(cmd))
	p = subprocess.Popen(cmd, shell=True)

def open_with(viewer,runme):
	print('open_with:{} <- {}\n- - - - - - - - - - - - - - - - - - - - - - - - - - - \n\n'.format(viewer,runme))
	subprocess.run([viewer,runme])

def find_in_parent(name,folder):
	print('looking for "{}" in "{}"'.format(name, folder))
	while True:
		if os.path.isdir(folder):
			if name in os.listdir(folder):
				print('"{}" found in "{}"'.format(name, folder))
				return folder+'/'+name
			elif folder == os.path.split(folder)[0]:
				print('"{}" not found; root reached.'.format(name))
				break
		else:
			return None
		folder = os.path.split(folder)[0]
	return None

def runit(arg):
	ext = os.path.splitext(arg)[1]
	folder = os.path.split(arg)[0]
	if ext == '.py':
		# print('python script')
		execute('python "{}"'.format(arg))
	elif ext in ('.pdf'):
		browser_cli_arg='file:///{}'.format(arg)
		open_with(browser,browser_cli_arg)
	elif ext in ('.ps1'):
		# print('powershell')
		open_with(powershell_ise,'"'+arg+'"')
	elif ext in ('.ps1'):
		# print('powershell script')
		execute('powershell -file "{}"'.format(arg))
	elif ext in ('.js','.css'):
		print('web assets')
		name = 'index.html'
		print('searching for index.html')
		arg = find_in_parent(name,folder)
		return runit(arg)
	elif ext in ('.bat'):
		# print('cmd batch file')
		return execute(arg)
	elif ext in ('.sql'):
		# print('SQL script')
		cmd = sql(arg)
		print(cmd)
		return execute(cmd)
		# return execute(cmd) # windows???
	elif ext in ('.html'):
		print('local webpage')
		open_with(browser,arg)
	elif ext in ('.md'):
		print('markdown')
		dst = os.path.splitext(arg)[0]+'.pdf'
		execute(md_pdf(arg,dst))
		dst = os.path.splitext(arg)[0]+'.html'
		execute(md_html(arg,dst))
		print(os.getcwd())
		while not os.path.exists(dst):
			time.sleep(0.5)
		runit(dst)
	elif ext in ('.tex'):
		print('latex document source')
		latex_dir = pymake_latex.build_latex_project()
		project_name = os.path.split(folder)[1]
		pdf_out_name='{}/{}.pdf'.format(folder,project_name)
		while not os.path.exists(pdf_out_name):
			time.sleep(0.5)
		browser_cli_arg='file:///{}/{}.pdf'.format(folder,project_name)
		open_with(browser,browser_cli_arg)
		pymake_latex.delete_files(latex_dir)
		# return
		# name = 'main.tex'
		# main_dir = find_in_parent(name,folder)
		# if main_dir is None:
		# 	print('{} not found. using {}'.format(name,arg))
		# 	main_dir = folder
		# 	name = arg
		# main_dir = main_dir.replace('\\','/')
		# print(main_dir)
		# main = os.path.join(folder,name).replace('\\','/')
		# pdflatex_cmd = '"{}"  -halt-on-error -output-directory "{}" -jobname "{}" "{}"'.format(pdflatex,folder, project_name, main)
		# execute(pdflatex_cmd)


def runitalt(arg):
	print('alternate build')
	ext = os.path.splitext(arg)[1]
	print(ext)
	folder = os.path.split(arg)[0]
	if ext in ('.ps1'):
		print('powershell ise')
		open_with(powershell_ise,'"'+arg+'"')
if __name__ == '__main__':
	arg = sys.argv[1]
	# print(list(map(lambda arg: arg.replace(r'\\','/').replace('//','/'),sys.argv)))
	if os.path.split(__file__)[1]==os.path.split(arg)[1]:
		print('pymake called itself.')
		sys.exit()
	if len(sys.argv)>2 and sys.argv[2] == '-alt':
		print('sys.argv[2] = {}'.format(sys.argv[2]))
		 # == '-alt':
		runitalt(arg)
	else:
		runit(arg)