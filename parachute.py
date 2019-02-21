# timesheet main program.
from parachuteCore import menulist, menu
from parachuteCore.tstools import getcmdxandy


class InvalidRunMenuReturn(Exception):
    pass


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
        raise InvalidRunMenuReturn("Invalid return from the runmenu method.")
    return choice


# main runner (No touchy!)
if __name__ == "__main__":
    launch()
