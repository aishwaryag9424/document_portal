## Virtual Environment:

To create a virtual env: 
conda create -n document_portal python=3.11
conda activate document_portal

To delete virtual env: 
conda remove --name document_portal --all

To create a env folder for the virtual environment: 
​​conda create -p env python=3.11
conda activate ./env

## Installing Requirements of the project
To install all packages
pip install -r requirements.txt

## setup.py 

setup.py is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. This information is used by the pip tool, which is a package manager for Python that allows users to install and manage Python packages from the command line. By running the setup.py file with the pip tool, you can build and distribute your Python package so that others can use it.

Command to install this document_portal as package into virtual environment. If you run pip list, document_portal will be there as a package with Editable project location as (/Users/user_name/document_portal)
pip install -e. 

## Git
Add a .gitignore file
to initialise it: git init
Anything inside .gitignore will not be visible on git
