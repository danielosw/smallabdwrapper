import os
abdPath = ''
def SetAdbPath(setpath:str):
    adbPath =setpath
def abdCommand(command:str):
    os.system(abdPath+command)
