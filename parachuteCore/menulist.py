# menulist.py contains all menus used in timesheet.py

from parachuteCore import menu
from parachuteCore.tstools import getcmdxandy, _Getch
# --- personalized classes ---
import sys
import os
import colorama


colorama.init(convert=True)
getch = _Getch()


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
            return choice
        elif key == 27:
            exit(0)
        elif key == 13:
            return str(choice)
        else:
            return choice

    def menu(self):
        os.system('cls')
        sys.stdout.write("\t\t\t\033[38;2;20;10;100mWelcome to OU's Offline timesheets!\033[0m \n\n\n")
        sys.stdout.write("    ->  \033[32mLog In\033[0m\n")
        sys.stdout.write("\t\033[32mRegister\033[0m\n")
        sys.stdout.write("\t\033[32mexit\033[0m\n")


class registerMenu(menu.Menu):
    def __init__(self):
        pass

    def getchoice(self, choice):
        key = ord(getch())
        if key == 72:
            if choice > 0:
                choice = choice - 1
            sys.stdout.write("\033[{0};5H  ".format(6 + (choice + 1)))
            sys.stdout.write("\033[{0};5H->".format(6 + choice))
            return choice
        elif key == 80:
            if choice < 4:
                choice = choice + 1
            sys.stdout.write("\033[{0};5H  ".format(6 + (choice - 1)))
            sys.stdout.write("\033[{0};5H->".format(6 + choice))
            return choice
        elif key == 27:
            exit(0)
        elif key == 13:
            return str(choice)
        else:
            return choice

    def menu(self):
        os.system('cls')
        sys.stdout.write("\t\t\t\033[34;1m User registration window\033[0m\n\n")
        sys.stdout.write("\n\n\n")
        sys.stdout.write("    ->  \033[35;1mEmployee Name: \033[0m\n")
        sys.stdout.write("\t\033[35;1mDepartment: \033[0m\n")
        sys.stdout.write("\t\033[35;1mUsername: \033[0m\n")
        sys.stdout.write("\t\033[35;1mPassword: \033[0m\n")
        sys.stdout.write("\t\033[36;1mSubmit\033[0m\n")


class loginMenu(menu.Menu):

    def __init__(self):
        pass

    def getchoice(self, choice):
        key = ord(getch())
        if key == 72:
            if choice > 0:
                choice = choice - 1
            sys.stdout.write("\033[{0};5H  ".format(6 + (choice + 1)))
            sys.stdout.write("\033[{0};5H\033[33m->\033[0;0m".format(6 + choice))
            return choice
        elif key == 80:
            if choice < 2:
                choice = choice + 1
            sys.stdout.write("\033[{0};5H  ".format(6 + (choice - 1)))
            sys.stdout.write("\033[{0};5H\033[33m->\033[0;0m".format(6 + choice))
            return choice
        elif key == 27:
            exit(0)
        elif key == 13:
            return str(choice)
        else:
            return choice

    def menu(self):
        os.system('cls')
        sys.stdout.write("\t\t\t\033[34;1m Log In window\033[0m\n\n")
        sys.stdout.write("\n\n\n")
        sys.stdout.write("\033[33m    ->  \033[0;0m\033[35;1mUsername: \033[0m\n")
        sys.stdout.write("\t\033[35;1mPassword: \033[0m\n")
        sys.stdout.write("\t\033[36;1mSubmit\033[0m\n")
