__author__ = 'grahamcrowell'

"""
this script recieves fullpath of a latex file, or latex project folder

# python -O "C:/Users/user/Dropbox/sublime_config/pymake_latex/pymake_latex.py" "C:/Users/user/Source/Repos/reference_sheets/cpp/cpp_general/cpp_general.tex"

Mac OSX sublime text 2: build-system:
    /Users/grahamcrowell/Library/Application/ Support/Sublime/ Text/ 2/Packages/User/latex.sublime-build 
    {
        "cmd": ["python", "-O", "/Users/grahamcrowell/Dropbox/pymake/pymake_latex/pymake_latex.py", "$file"],
        "working_dir": "${project_path:${folder}}",
        "selector": "source.latex"
    }
"""



import os, sys, string, itertools, shutil, inspect, subprocess, time, traceback, datetime

_latex_main_name = 'main.tex'
_input_line = '--------------------------------------------------------------------'
_input_cmd_format = lambda latex_src: '\t\\input{' + '{}'.format(latex_src) + '}\n'
_input_cmd = '\\input{'
_biblio_cmd = '\\bibliography{'
_esc_seq_latex = '%'

_config_name = 'pymake.config'
_esc_seq_config = '//'

def show_splash():
    print('\n\npymake_latex building latex project\n\n')

def parse_param_line(line):
    if __debug__:
        # print('parsing parameter line:\n\t{}'.format(line))
        pass
    if isinstance(line, str) and '=' in line:
        line = (line.strip())
        esc_pos = line.find(_esc_seq_config)
        if esc_pos > -1:
            if __debug__:
                # print('line contains _esc_seq_config (esc_pos at: {})\n\tnew line: {}'.format(esc_pos, line[0:esc_pos]))
                pass
            line = line[0:esc_pos]
            return parse_param_line(line[0:esc_pos])
        elif '=' in line:
            key = (line.split('=')[0].strip())
            val = (line.split('=')[1].strip())
            if val[0:2] == './':
                val = os.path.join(os.path.split(sys.argv[0])[0], val[2:])
            if __debug__:
                print('valid parameter: {}={}'.format(key, val))
            return key, val
        else:
            return False
    else:
        return False

class Parameter(dict):
    def __init__(self, path):
        dict.__init__(self)
        self.path = os.path.normpath(path)
        assert(os.path.isfile(path))
        with open(path) as param_file:
            self.update(dict(map(parse_param_line, filter(parse_param_line, param_file.readlines()))))


def create_bib(param_dict, bib_path):
    if os.path.isfile(bib_path):
        return 
    message = '\t\t!!!copying template {}!!!'.format(param_dict['bib_template'])
    if os.path.split(bib_path)[1] != param_dict['bib_template']:
        message += ' (as {})'.format(os.path.split(bib_path)[1])
    print(message)
    bib_template_path = os.path.join(param_dict['latex_template_dir'], param_dict['bib_template'])
    assert os.path.isfile(bib_template_path)
    shutil.copyfile(bib_template_path, bib_path)

def detect_biblio(param_dict, project_main):
    with open(project_main) as main_file:
        lines = main_file.readlines()
        bib_lines = list(filter(lambda line: _biblio_cmd in line, lines))
    if len(bib_lines) == 0:
        return False
    else:
        bib_line = bib_lines[0]
#     print(bib_line)
    esc_pos = bib_line.find(_esc_seq_latex)
#     print('esc_pos = {}'.format(esc_pos))
    bib_cmd_pos = bib_line.find(_biblio_cmd)
#     print('bib_cmd_pos = {}'.format(bib_cmd_pos))
    if esc_pos > -1 and esc_pos < bib_cmd_pos:
        return False
    else:
        bib_file_pos = bib_cmd_pos + len(_biblio_cmd)
        bib_file_len = bib_line[bib_file_pos:].find('}')
        bib_name = bib_line[bib_file_pos:bib_file_pos + bib_file_len]
        if os.path.splitext(bib_name)[1].lower() != '.bib':
            bib_name = bib_name + '.bib'
            bib_path = os.path.join(project_dir, bib_name)
            if __debug__:
                print('\tbibTeX execution required (ref file: {}). . .'.format(os.path.split(bib_path)[1]))
            if not os.path.isfile(bib_path):
                create_bib(param_dict, bib_path)
            else:
                if __debug__:
                    print('\t\t{} found'.format(os.path.split(bib_path)[1]))
        return True



# not working ... os issue (used to work on mac)
def execute(cmd):
    print(cmd)
    if __debug__:
        print('!!!executing:\n\t{}!!!'.format(cmd))
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    
    # c = time.clock()
    
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            if __debug__:
                print('process execution complete')
            break
        if str(out) != b'':
            sys.stdout.write(str(out))
            sys.stdout.flush()
    ret_code = p.wait()
    if ret_code != 0:
        raise Exception()
    else:
        return ret_code
    # print('\n\n\n\treturn code: {}\n\n\n'.format(ret_code))

def execute(cmd):
    print('{}\n\n\n'.format(cmd))
    p = subprocess.Popen(cmd, shell=True)

def quiet_execute(cmd):
    if __debug__:
        print('!!!quietly executing:\n\t{}!!!'.format(cmd))
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    ret_code = p.wait()
    if ret_code != 0:
        raise Exception()
    else:
        return ret_code

def fast_execute(cmd):
    if __debug__:
        print('!!!quietly executing:\n\t{}!!!'.format(cmd))
    p = subprocess.Popen(cmd)
    # ret_code = p.wait()
    if ret_code != 0:
        raise Exception()
    else:
        return ret_code

def preview(param_dict, pdf_path):
    if __debug__:
        print('!!!previewing!!!')
    cmd = '"open -a /Applications/Preview.app {}"'.format(pdf_path)
    cmd = 'open "{}"'.format(pdf_path)
    cmd = '/usr/bin/qlmanage -p "{}"'.format(pdf_path)
    args = ['/usr/bin/qlmanage', ' -p ' , '"{}"'.format(pdf_path)]
#     subprocess.call(cmd)
    quiet_execute(cmd)

def delete_files(directory, exts=['.aux', '.log', '.out']):
    if __debug__:
        print('\n\nCLEANING PROJECT DIRECTORY\n\n')
    assert os.path.isdir(directory)
    del_names = list(filter(lambda filename: os.path.splitext(filename)[1] in exts, os.listdir(directory)))
    del_paths = map(lambda del_name: os.path.join(directory,del_name), del_names)
    if __debug__:
        print('\n\n\n\t****\nfiles to be deleted:\n\t{}\n\n'.format(list(del_paths)))
    for del_path in del_paths:
        os.remove(del_path)
    # map(os.remove, del_names)
    
def typeset(param_dict, latex_project):
    if __debug__:
        print('!!!typesetting!!!')
    if param_dict['tex_bin_dir'] == '':
        pdflatex_cmd = 'pdflatex'
    else:
        pdflatex_cmd = '"{}"'.format(os.path.join(param_dict['tex_bin_dir'], 'pdflatex'))
    pdflatex_cmd += '  -halt-on-error -output-directory "{}" -jobname "{}" "{}"'.format(latex_project.dir, latex_project.job_name, latex_project.main);
    if __debug__:
        print('pdflatex_cmd = {}'.format(pdflatex_cmd))
    
    execute(pdflatex_cmd)

    is_bib = detect_biblio(param_dict, latex_project.main)
    if is_bib:
        raise NotImplementError()
    
    
    return latex_project.pdf_path


def create_main(param_dict, latex_src_path):
    project_dir = os.path.split(latex_src_path)[0]
    project_main = os.path.join(project_dir, _latex_main_name)
    latex_template_path = os.path.join(param_dict['latex_template_dir'], param_dict['latex_template_std'])
    assert os.path.isfile(latex_template_path)
    with open(latex_template_path) as template_file:
        lines = template_file.readlines()
        with open(project_main, 'w') as main_file:
            for line in lines:
                main_file.write(line)
                if _input_line in line:
                    latex_src_name = os.path.split(latex_src_path)[1]
                    main_file.write(_input_cmd_format(latex_src_name))


class LatexProject:
    def __init__(self,latex_main_fullpath):
        self.main = latex_main_fullpath
        self.dir = os.path.split(self.main)[0]
        self.job_name = os.path.split(self.dir)[1]
        self.pdf_path = os.path.join(self.dir, self.job_name + '.pdf')

def handle_cmd_args():
    """ parse command line arguments for latex project return dict Parameter, object LatexProject """
#     pymake_dir = os.path.split(inspect.getframeinfo(inspect.currentframe()).filename)[0]
    pymake_dir = os.path.split(sys.argv[0])[0]
    config_path = os.path.join(pymake_dir, _config_name)
    if __debug__:
        print('sys.argv: {}'.format(sys.argv))
        print('os.getcwd(): {}'.format(os.getcwd()))
    param_dict = Parameter(config_path)
    if __debug__:
        print(param_dict)
    if len(sys.argv) == 1:
        project_dir = os.getcwd()
        project_main = os.path.join(project_dir, _latex_main_name)
        assert os.path.isfile(project_main)
    else:
        # recieved full path (latex.sublime-build does this)
        if os.path.isfile(sys.argv[1]):
            latex_src = sys.argv[1]
            project_dir = os.path.split(latex_src)[0]
            assert os.path.splitext(latex_src)[1].lower() == '.tex'
            project_main = os.path.join(project_dir, _latex_main_name)
            if not os.path.isfile(project_main):
                create_main(param_dict, latex_src)
            assert os.path.isfile(project_main)
        elif os.path.isdir(sys.argv[1]):
            project_dir = sys.argv[1]
            project_main = os.path.join(project_dir, _latex_main_name)
            assert os.path.isfile(project_main)
        else:
            # received filename but no path
            project_dir = os.getcwd()
            latex_src = os.path.join(project_dir, sys.argv[1])
            assert os.path.isfile(latex_src)
            project_main = os.path.join(project_dir, _latex_main_name)
            if not os.path.isfile(project_main):
                create_main(param_dict, latex_src)
            assert os.path.isfile(project_main)
    
    return param_dict, LatexProject(project_main)

def clean_comments(path,comment_char):
    with open(path) as txt_file:
        lines = list(map(lambda line: line.split(comment_char)[0],txt_file.readlines()))
    return lines

def extract_inputs(project_main):
    latex_project = LatexProject(project_main)
    lines = clean_comments(project_main, _esc_seq_latex)
    input_lines = list(filter(lambda line: _input_cmd in line, lines))
    input_cmds = map(lambda line: line.split(_input_cmd)[1],input_lines)
    input_names = list(map(lambda line: line.split('}')[0], input_cmds))
    input_paths = map(lambda name: os.path.join(latex_project.dir, name), input_names)
    return input_paths

def get_creation_time(path):
    p = subprocess.Popen(['stat', '-f%B', path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.wait():
        raise OSError(p.stderr.read().rstrip())
    else:
        return int(p.stdout.read())

def filetimes(path):
    ctimes = lambda path: list(map(time.ctime,[get_creation_time(path),os.path.getctime(path),os.path.getatime(path),os.path.getmtime(path)]))
    filetime_str = lambda path: '{}\n\tstime:{}\n\tctime:{}\n\tatime:{}\n\tmtime:{}'.format(path,*ctimes(path))
    return filetime_str(path)

# not working... don't care tho
def isoutdated(project_main):
    latex_project = LatexProject(project_main)
    if not os.path.isfile(latex_project.pdf_path):
        return True
    files = extract_inputs(latex_project.main)
    files.append(latex_project.main)
    files.append(latex_project.pdf_path)
    
    files = sorted(files, key=lambda path: os.path.getmtime(path),reverse=True)

    if __debug__:
        print('\n'.join(list(map(filetimes,files))))

    tm = datetime.datetime.fromtimestamp

    if files[0] != latex_project.pdf_path:
        if __debug__:
            print('out of date by (last file change: {})'.format(tm(os.path.getmtime(files[0])) - tm(os.path.getmtime(latex_project.pdf_path))))
        return True
    else:
        if __debug__:
            print('up to date (last file change: {})'.format(tm(time.time()) - tm(os.path.getmtime(files[0]))))
        return False

def isoutdated(project_main):
    return True


def build_latex_project():
    param_dict, latex_project = handle_cmd_args()
    if isoutdated(latex_project.main):
        pdf_filename = typeset(param_dict, latex_project)
    # preview(param_dict, latex_project.pdf_path)
    delete_files(latex_project.dir)
    return latex_project.dir
        
if __name__ == '__main__':
    show_splash()
    try:
        build_latex_project()
    except Exception:
        ex_type, ex, tb = sys.exc_info()
        # print(ex_type)
        # print(type(ex_type))
        # print(ex)
        # print(type(ex))
        # print(tb)
        # print(type(tb))
        # print(ex)
        tb_str= '\n'+''.join(traceback.format_tb(tb))+str(ex)
        print(tb_str)
        # for line in tb_lines:
            # print(line)
