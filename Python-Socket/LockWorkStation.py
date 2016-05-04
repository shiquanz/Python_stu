from ctypes import *
from sys import *
def lock_work_station():
    num = raw_input('input \'lock\' to lock: \n ')
    if num == 'lock':
        user32 = windll.LoadLibrary('user32.dll')
        user32.LockWorkStation()
    else:
        exit()
if __name__ == '__main__':
    lock_work_station()

