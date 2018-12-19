# timesheet main program.
import menu
from tstools import getcmdxandy
import menulist
# --- personalized classes ---

def launch():
    main = menulist.mainMenu()
    choice = menu.runmenu(main)
    if choice == "2":
        exit(0)
    elif choice == "1":
        pass
    elif choice == "0":
        pass
    else:
        pass # shall never get to this!

# main runner (No touchy!)
if __name__ == "__main__":
    launch()
