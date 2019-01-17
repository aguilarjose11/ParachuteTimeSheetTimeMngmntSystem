# this program will test new modules and characteristics for software.
import os
import sys
import importlib
import colorama
from msvcrt import getch
from ctypes import windll, create_string_buffer
import win32api
from devdelta import getx, gety

colorama.init(convert=True)

'''
    development stages featured:
--------------------------------------
    # dev -> development proccess.
    # dbg -> Debuging/Sharpenning.
    # mrg -> Ready for merging.
    # hlt -> halted/delayed.
    # zzz -> canceled.
    # ooo -> feature completed
'''
# change keys for output color and text legends.
colorscheme = {"dev":"\033[32;1m", "dbg":"\033[32m", "mrg":"\033[35;1m", "hlt":"\033[33;1m", "zzz":"\033[31;1m", "ooo":"\033[36;1m"}
statuscode = {"dev":"Development:", "dbg":"Debugging:", "mrg":"Ready to merge:", "hlt":"Halted:", "zzz":"Canceled:", "ooo":"Completed:"}

'''
 * called by setup().
 * if new features are to be added, add inside for loop as elif.
 ** do not forget to add value with key used in colorscheme and statuscode.
'''
def organizebystatus(modulelist):
    map = dict()
    statlist = {"dev":list(), "dbg":list(), "mrg":list(), "hlt":list(), "zzz":list(), "ooo":list()}
    for key, value in modulelist.items():
        if value[0] == "dev":
            statlist["dev"].append(key)
        elif value[0] == "dbg":
            statlist["dbg"].append(key)
        elif value[0] == "mrg":
            statlist["mrg"].append(key)
        elif value[0] == "hlt":
            statlist["hlt"].append(key)
        elif value[0] == "zzz":
            statlist["zzz"].append(key)
        elif value[0] == "ooo":
            statlist["ooo"].append(key)
        else:
            print("Error at {0}. \nno status for module.".format(key))
            exit(1)
    step = 1 # step per option.
    os.system('cls')
    for key, val in statlist.items():
        print("{0}{1}".format(colorscheme[key],statuscode[key]))
        temp = 0 # counter of options possibles for each tag
        if val:
            for mdl in val:
                print("\t\t    {0} ({1})".format(mdl[6:],mdl))
                map[step] = gety()
                step += 1
        else:
            print("\033[0m - No modules found.")
        sys.stdout.write("\033[0m")
    return map

''' setup of module data '''
def setup():
    moduledir = dict()
    modulecallstack = list()
    dirlist = [item for item in os.listdir() if os.path.isdir(item)]
    for dir in dirlist:
        if (dir.find("module") != -1):
            sys.path.append("{0}/".format(dir))
            module = importlib.import_module(dir)
            moduledir[dir] = [module.modulestatus()['status'], module]
            modulecallstack.append(module)
    return organizebystatus(moduledir), modulecallstack

def launch():
    map, modules = setup()
    step = 1
    sys.stdout.write("\033[{0};17H->".format(map[step]))
    # main infinite loop. * break with esc key.
    while True:
        key = ord(getch())
        if key == 27:
            os.system('cls')
            exit(0)
        elif key == 72: # arrow up.
            if step == 1:
                pass
            else:
                sys.stdout.write("\033[{0};17H  ".format(map[step]))
                step -= 1
                sys.stdout.write("\033[{0};17H\033[37;1m->\033[0m".format(map[step]))
        elif key == 80: # down arrow.
            if step == len(map):
                pass
            else:
                sys.stdout.write("\033[{0};17H  ".format(map[step]))
                step += 1
                sys.stdout.write("\033[{0};17H\033[37;1m->\033[0m".format(map[step]))
        elif key == 13:
            if modules[step - 1]:
                os.system('cls')
                modules[step - 1].main_dev()
                input("\n\033[36;1mclick enter to end testing...\033[0m")
                os.system('cls')
                setup()
                sys.stdout.write("\033[{0};17H->".format(map[1]))
                step = 1

if __name__ == "__main__":
    launch()
