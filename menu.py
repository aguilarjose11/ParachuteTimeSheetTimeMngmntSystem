# menu.py

# abstract class. do not define. leave AS IT IS.
class Menu:
    def __init__():
        pass
    # returns a String with the final choice.
    def getchoice(choice):
        pass
    # print out entire menu ONCE.
    def menu():
        pass

# this method should be fully defined.
def runmenu(exec):
    exec.menu()
    choice = 0
    while(not(type(choice) == str)):
        choice = exec.getchoice()
    return choice
