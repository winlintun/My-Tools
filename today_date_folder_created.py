import os
import datetime



def strrr():
    a = str(datetime.datetime.now().date())
    return a


path = os.path.join(os.getcwd(), strrr())

try:
    os.mkdir(path)
except (Exception, FileExistsError) as e:
    print(e)
    input("Press Any Key!!!")