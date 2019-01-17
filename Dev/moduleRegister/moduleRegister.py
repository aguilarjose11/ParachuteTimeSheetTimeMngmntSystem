# module xyz
def modulestatus():
    status = {'status' : 'mrg',
              'project' : '%projectname%',
              'version' : '1.0.0.0',
              'last' : '%current date% %curent time%'}
    return status

def main_dev():
    print("this is a module in development")
