import os
import settings as sett

outPath = sett.workPath
inPath = [""]
print("Файловый менеджер.\nВведите help для отображения команд.")

def pathFileString(fileName):
    return str (f'{outPath}{getFullPath()}{fileName}')

def checkAvailable(f):
    if os.path.isfile(pathFileString(f)) | os.path.isdir(pathFileString(f)):
        return 1
    else:
        print("Файл/папка не существует или введено недопустимое имя")

def checkAFolder(f):
    if os.path.isdir(f'{outPath}{f}'):
        return 1
    else:
        print("Путь недоступен")

def getFullPath():
    fullpath = ""
    for part in inPath:
        fullpath+= part + '/'
    return fullpath

class cmds():

    def help(): #help
        print("Помощь")

    def ap(fname): # add folder
        fname = fname[3:]
        os.mkdir(pathFileString(fname))

    def dp(fname): #delete folder
        fname = fname[3:]
        if checkAvailable(fname):
            try:
                os.rmdir(pathFileString(fname))
            except:
                print("Невозможно удалить: папка не пуста или не достаточно прав")
    
    def cp(fname): #change folder
        fname = fname[3:]
        if (fname == '-'):
            if len(inPath) == 1:
                print("Вы в корневой папке")
            else:
                inPath.pop()
            return 1
        elif (fname == '/'):
            inPath.clear()
        else:
            if checkAvailable(fname):
                inPath.append(fname)

    def af(fname): #add file
        fname = fname[3:]
        try:
            with open (pathFileString(fname), 'w+') as file:
                print(f'Файл {fname} создан.')
            file.close()
        except:
            print('Недопустимое название файла')

        


def processInput(str):
    if (str == 'help'): cmds.help()
    if (str[:2] == 'ap'): cmds.ap(str)
    if (str[:2] == 'dp'): cmds.dp(str)
    if (str[:2] == 'cp'): cmds.cp(str)
    if (str[:2] == 'af'): cmds.af(str)


while 1:
    cmd = input()
    result = processInput(cmd)
