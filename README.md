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
