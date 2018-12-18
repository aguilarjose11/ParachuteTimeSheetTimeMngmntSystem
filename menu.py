# menu.py

# abstract class. do not define. leave AS IT IS.
class Menu:
    def __init__(self):
        pass
    # returns a String with the final choice.
    def getchoice(self):
        pass
    # print out entire menu ONCE.
    def menu(self):
        pass

# this method should be fully defined.
def runmenu(exec):
    exec.menu()
    choice = 0
    while(not(type(choice) == str)):
        # testing line
        input("Click enter to continue . . . (will crash if enter)")
        choice = exec.getchoice()
    return choice
