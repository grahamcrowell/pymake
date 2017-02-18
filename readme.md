# pymake

build system for sublime text

## sublime setup

1. Tools -> Build System -> new build system...
```
	{
	    "cmd": ["C:/Users/user/Source/Repo/pymake/run_me.bat", "$file"],
	    "variants": [
			{ 
				"name": "Run",
				"cmd": ["C:/Users/user/Source/Repo/pymake/run_me.bat", "$file", "--alt"]
			}
	    ]
	}
```


## run_me.sh
bash shell script for redirecting files from Sublime Text 2 on MacOSX for appropiate execution
- python, 
- mysql, 
- bash, 
- latex (required pymake)
- Qt *.qml, 
- pyside *.ui, 
- simple *.cpp
- makefiles

path: "/Users/grahamcrowell/run_me.sh"

# Sublime Text 2 build system:
```python
{
    "cmd": ["bash","/Users/grahamcrowell/run_me.sh", "$file"]
}
```
## get_commands.sh
basic git commands to commit repository to github.com
<!-- $f(x)=\sin(\frac{\textup{d}}{\textup{d}x}g(x^{\int e^{x^2}}))$ -->