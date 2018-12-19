# menulist.py
'''
    this module contains all of the menus being used at timesheet.py.
'''

import menu
from tstools import getcmdxandy
# --- personalized classes ---
import sys
import os
import colorama
from msvcrt import getch

colorama.init(convert=True)

class mainMenu(menu.Menu):
    def getchoice(self, choice):
        key = ord(getch())
        if key == 72:
            if choice > 0:
                choice = choice - 1
            sys.stdout.write("\033[{0};5H  ".format(4 + (choice + 1)))
            sys.stdout.write("\033[{0};5H->".format(4 + choice))
            return choice
        elif key == 80:
            if choice < 2:
                choice = choice + 1
            sys.stdout.write("\033[{0};5H  ".format(4 + (choice - 1)))
            sys.stdout.write("\033[{0};5H->".format(4 + choice))
            return  choice
        elif key == 27:
            exit(0)
        elif key == 13:
            return str(choice)
        else:
            return choice

    def menu(self):
        os.system('cls')
        sys.stdout.write("\t\t\t\033[38;2;20;10;100mWelcome to OU's Offline timesheets!\033[0m \n\n\n")
        sys.stdout.write("    ->  \033[32mLog In\033[0m\n" )
        sys.stdout.write("\t\033[32mRegister\033[0m\n" )
        sys.stdout.write("\t\033[32mexit\033[0m\n" )
