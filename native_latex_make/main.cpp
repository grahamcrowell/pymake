/*

USAGE:  ./main project_dir

*/

// STANDARD C HEADERS
#include <stdio.h>
// #include <tchar.h>

// STANDARD C HEADERS
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
// #include <conio.h>
// #include <process.h>
// STANDARD C++ HEADERS
#include <iostream> 
#include <sstream>
#include <fstream>
#include <algorithm>
#include <chrono>
#include <vector>
#include <string>
#include <map>
// POSIX dirent.h API
#include <dirent.h>

#include "../../util/path.h"
using namespace std;

bool copy_template(string dst_dir)
{
	string src_path("/Users/grahamcrowell/Dropbox/github_local/sublime_build_redirect/templates/LaTeX_template copy.tex");
	ifstream src_file(src_path.c_str());
	if (!src_file.is_open())
	{
		cout << "ERROR: unable to open LaTeX_template at\n" << src_path << endl;
		return false;
	}
	string dst_path(dst_dir+"/main.tex");
	ofstream dst_file(dst_path.c_str());
	if (!dst_file.is_open())
	{
		cout << "ERROR: unable to open dest file at\n" << dst_path << endl;
		return false;
	}	

	cout << "COPYING TEMPLATE" << endl;
	string line;

	while(getline(src_file,line))
	{
		cout << line << endl;
		if (line.find("--------------------------------------------------------------------") != string::npos)
		{
			dst_file << line;
			dst_file << "\t\\input{" << "_____" << "}\n";
		}
		else dst_file << line;
	}


	dst_file.close();
	src_file.close();
	return false;
}

int parse_arg(Path p)
{
	cout << "parsing path: " << p << endl;
	cout << p.name() << endl;
	// string parent(string.substr(arg,i));
	// cout << parent << endl;

	// struct dirent *entry;
	// DIR *dp;

	// dp = opendir(arg.c_str());

	// if (dp == NULL) {
 //    	printf("opendir");
 //    	return -1;
 //  	}

	// while((entry = readdir(dp)))
 //    	puts(entry->d_name);

	return 0;
}


void foo(char* x){}

int main(int argc, char* argv[]) 
{
	cout << "\n\nTYPESETTING LATEX PROJECT . . .\n\n";

	// printf("%s\n",argv[0]);	
	Path p;
	if (argc > 1)
	{
		string arg_str(argv[1]);
		p = Path(arg_str);
		// parse_arg(arg_str);
		// copy_template(arg_str);
	}
	else
	{
		string arg_str("/Users/grahamcrowell/Desktop/test_pdf/resume.tex");
		p = Path(arg_str);
		// parse_arg(arg_str);
	}
	parse_arg(p);
	// if (argc == 1)
	// {
	// 	cout << "ERROR: no arguement sent" << endl;
	// 	cout << argv[0] << endl;
	// 	return 1;
	// }
	// else foo(argv[1]);
	// cout << "EXECUTION COMPLETE" << endl;
	return 0;
}
