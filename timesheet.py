# timesheet main program.
import menu
from tstools import getcmdxandy
import menulist
# --- personalized classes ---

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

# main runner (No touchy!)
if __name__ == "__main__":
    launch()
