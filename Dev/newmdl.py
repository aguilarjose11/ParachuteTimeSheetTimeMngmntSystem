# this program creates a new module.
import os
import datetime

def launch():
    print("module setup program vercion 1.0.0.0\n")
    name = input("module name >>>: ")
    setup(name)
    exit(0)


# name shall always be a string
def setup(name):
    modulehome = "module{0}".format(name)
    os.mkdir(modulehome)
    os.chdir(modulehome)
    dir1 = os.getcwd()
    dir2 = dir1.split('\\')
    n = len(dir2)
    proj = dir2[n-3]
    mdlfile = open("{0}.py".format(modulehome), "w+")
    text = "# module {0}\ndef modulestatus():\n    status = {{'status' : 'dev',\n              'project' : '{1}',\n              'version' : '1.0.0.0',\n              'last' : '{2}'}}\n    return status\n\ndef main_dev():\n    pass # code to run.\n".format(name, proj, datetime.datetime.now())
    mdlfile.write(text)
    mdlfile.close()
    print("module succesfully setup at {0}".format(os.getcwd()))

if __name__ == "__main__":
    launch()
