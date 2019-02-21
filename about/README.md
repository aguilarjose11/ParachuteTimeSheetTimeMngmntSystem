Important notes.
================

> to test whether python is running in virtual environment, run this:

'''python
import sys

# if using python < 3.3 use real_prefix.
if hasattr(sys, 'base_prefix'):
  print("Running in virtual enviroment.")
else:
  print("not running in virtual environment, dont forget to run .\venv\Scripts\Activate.ps1")
'''

> to run for testing:

'''shell
pip install virtualenv
python -m venv env
.\venv\Scripts\activate  (..\Activate.ps1 for microsoft PowerShell/)
python -m pip install --upgrade pip
flake8 --exclude=.\env --statistics
'''

> to install all the packages in requirements.txt:

'''shell
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
'''
