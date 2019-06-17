[![CircleCI](https://circleci.com/gh/aguilarjose11/ParachuteTimeSheetTimeMngmntSystem/tree/develop.svg?style=svg)](https://circleci.com/gh/aguilarjose11/ParachuteTimeSheetTimeMngmntSystem/tree/develop)

Parachute Time management system (aka. OUTimeSheets)
====================================================

Disclaimer
---------

Parachute is a very basic cmd-oriented system that its main purpose is that of providing a basic time-controlling system in the form of bi-weekly timesheets. this program was created with the intention of practicing skills and giving a set of functions that others may find useful on their projects.. everyone is welcome to come and grab code that may be suitable for them. this program is written entirely in `python`.

Structure (Flowcharts).
======================

A flow chart can be found inside of the folder `../about/flowcharts`.
The flowcharts are intended to help on analyzing the location and ideas behind each part of code.

modules.
--------

the program is divided into 4 modules with 3 `menu.py, menulist.py, tstools.py` acting as libraries and 1 `timesheet.py` acting as the main program.

### timesheet.py

timesheet.py contains all of the code in charge of the execution of the program. for organization, no declarations other than `launch()` have been done here.

The program first checks if the file is being run as the main file, if so it launches the launch method which is in charge of all of the execution of the program.

inside of the launch method, a principal method is instantiated (see menulist.py). then, the menu is run the `runmenu()` method. Finally, based on the choice done inside of the menu, if methods test to see the choice that was made. inside the testing choices, menus are instantiated and run.


```python
if __name__ == "__main__":
launch()

def launch():
    main = menulist.mainMenu()
    choice = menu.runmenu(main)
    if choice == "0":
        login = menulist.loginMenu()
        choice = menu.runmenu(login)
    elif choice == "1":
        register = menulist.registerMenu()
        choice = menu.runmenu(register) # menu.menurunner(register)
    elif choice == "2":
        exit(0)
    else:
        pass # shall never get to this!
```

### menu.py

The menu library holds all of the declarations for the menus used by the `timesheet.py` program.

it is important to note that this library only holds the abstract declarations for the base class of the menus. this module also holds a function that runs the menus that were inherited from the Menu class.

```python
# for simplicity, code has been replaced for pass statements.

# this is the abstract class for other classes
class Menu:
  def menu(self):
    pass

  def getchoice(self):
    pass

# this is the method in charged of executing and returning a return choice from the Menu-based menus
def runmenu(exec):
  pass
```
#### method definitions.
* the `menu(self)` function is intended to contain a single-time-print menu.

* the `getchoice(self)` function is intended to control the movement of a cursor on the menu printed by `menu()`.

* `getchoice(self)` should be added a choice argument for the sake of recursivity. left out of the astract deffinition for the sake of flexibility

* the `runmenu(self)`

### menulist.py

The menulist module is in charge of holding the definition of the classes that inherit from the Menu class from `menu.py` module. this classes are to be run by the `runmenu()` method inside of the `timesheet.py` program. inside, there is three definitions:

```python
# for simplicity, code has been replaced for pass statements.
# see the menu.py and tstools.py modules for more information on these imports.
import menu
from tstools import getcmdxandy

class mainMenu(menu.Menu):
  pass

class registerMenu(menu.Menu):
  pass

class loginMenu(menu.Menu):
  pass
```

these classes are to be instantiated inside the `timesheet.py` program.
#### Classes.

* `mainMenu` is in charge of the main menu.

* `registerMenu` is in charge of the registration menu.

* `loginMenu` is in charge of the login process menu.

### tstools.py

this module holds all functions being used by the modules and the program itself that hold a specific job. these methods were defined in a different module for the sake of organization, for these methods could be used y multiple modules at once.

```python
# for simplicity, code has been replaced for pass statements. also, imports have been left out.
def getcmdxandy():
  pass
```

#### Methods.

* `getcmdxandy()` method returns the x and y size of the current cmd window in characters of length.

About DevDelta environment.
==========================

Inside the Dev folder, a version development tester program resides. as of Jan 15, 2019, the testing program (namely DevDelta) is in work in version 1.0 and can be used and installed by moving the files `Dev\newmdl.py`, `Dev\test.py`, and `Dev\devdelta.pyd` into your module and version development environment.

Running DevDelta.
-----------------

In order to run DevDelta, we must first create a module using the `newmdl.py` program. A new module is created once the `newmdl.py` script is done. a module consists of a folder with the name of the module and "module" attached at the beginning. you can make a module folder by simply naming the folder as `module{module name}`. Secondly, a `.py` file is created with the name of the module folder. Inside of this python file we can find two methods:

`moduleExample\moduleExample.py`

```python
# module Example
def modulestatus():
    status = {'status' : 'dev',
              'project' : '%projectname%',
              'vercion' : '1.0.0.0',
              'last' : '%current date% %curent time%'}
    return status

def main_dev():
  pass #code to run.
```

### `modulestatus()`

This method contains a dictionary with the information related to the current status of the module, version, project name (uses the name of the folder containing the DevDelta enviroment, aka `{this folder}\{DevDelta enviroment}\test.py`), and the creation time.

```python
status = {'status' : 'zzz',
              'project' : 'ParachuteTSMSys',
              'version' : '1.0.0.0',
              'last' : '2019-01-15 18:40:57.340831'}
```

The status of the module can be changed by assigning a new value to the status key inside of the dictionary inside of the method by assigning one of the _six development statuses_:

* `"dev"`: Module is on development.

* `"dbg"`: Module is on debugging.

* `"mrg"`: Module is ready to merge.

* `"hlt"`: Module has be brought to a halt.

* `"zzz"`: Module has become deprecated/canceled.

* `"ooo"`: Module is completed and merged with main program.

Important: _Note that the merging process has to be done by hand, the program DOES NOT touch any code outside of the environment where DevDelta is installed_

### `main_dev()`

This method will contain all of the code to be developed and be tested. this is _the only method being called by test.py._ code does not have to be contained only on this file though, folders can be made inside of the module folder as well as adding files to the folder that are to be used by the module.
