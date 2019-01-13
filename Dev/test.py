# this program will test new modules and characteristics for software.
import os
import sys
import importlib
import colorama

colorama.init(convert=True)

'''
    # dev -> development proccess.
    # dbg -> Debuging/Sharpenning.
    # mrg -> Ready for merging.
    # hlt -> halted/delayed.
    # zzz -> canceled.
    # ooo -> feature completed
'''
# global values
colorscheme = {"dev":"\033[32;1m", "dbg":"\033[32m", "mrg":"\033[35;1m", "hlt":"\033[33;1m", "zzz":"\033[31;1m", "ooo":"\033[36;1m"}
statuscode = {"dev":"Development:", "dbg":"Debugging:", "mrg":"Ready to merge:", "hlt":"Halted:", "zzz":"Canceled:", "ooo":"Completed:"}

def organizebystatus(modulelist):
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

    for key, val in statlist.items():
        print("{0}{1}".format(colorscheme[key],statuscode[key]))
        if val:
            for mdl in val:
                print("\t\t    {0} ({1})".format(mdl[6:],mdl))
        else:
            print("\t\t    No modules found.")
        sys.stdout.write("\033[0m")
    exit(0)




def setup():
    moduledir = dict()
    dirlist = [item for item in os.listdir() if os.path.isdir(item)]
    for dir in dirlist:
        if (dir.find("module") != -1):
            sys.path.append("{0}/".format(dir))
            module = importlib.import_module(dir)
            moduledir[dir] = [module.modulestatus()['status'], module]
    organizebystatus(moduledir)

def launch():
    setup()


if __name__ == "__main__":
    launch()
