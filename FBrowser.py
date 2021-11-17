import os
import shutil
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
        if checkAvailable(fname):
            print ("Файл с таким именем уже существует")
        else:
            try:
                with open (pathFileString(fname), 'w+') as file:
                    print(f'Файл {fname} создан.')
                file.close()
            except:
                print('Недопустимое имя файла')
    
    def wf(fname): #write to file
        fname = fname[3:]
        if checkAvailable(fname):
            try:
                with open (pathFileString(fname), 'w+') as file:
                    text = input("Введите текст для записи: ")
                    file.write(text)
            except:
                print('Недопустимое имя файла')

    def rf(fname): #read file
        fname = fname[3:]
        if checkAvailable(fname):
            try:
                with open (pathFileString(fname), 'r') as file:
                    while True:
                        line = file.readline()
                        if not line : 
                            break
                        print(line.strip())
                file.close()
            except:
                print('Недопустимое имя файла')

    def df(fname): #delete file
        fname = fname[3:]
        if checkAvailable(fname):
            try:
                os.remove(pathFileString(fname))
            except:
                print('Недопустимое имя файла')

    def copyf(fname):
        fname = fname[6:]
        if checkAvailable(fname):
            try:
                pathto = input("Введите папку назначения (введите '--' для отмены)\n/")
                if pathto == '--' : return 0
                if checkAvailable(pathto):
                    try:
                        shutil.copyfile(pathFileString(fname), f'{outPath}/{pathto}/{fname}')
                    except:
                        print('Недопустимый путь')
            except:
                print('Недопустимое имя файла')
    def renf(fname):
        fname = fname[5:]
        if checkAvailable(fname):
            try:
                newfname = input(f"Введите новое имя файла (введите '--' для отмены)\n{fname} > ")
                if newfname == '--' : return 0
                try:
                    os.rename(pathFileString(fname),pathFileString(newfname))
                except FileExistsError:
                    print("Файл с таким именем уже существует")
            except:
                print('Недопустимое имя файла')
        


def processInput(str):
    if (str == 'help'): cmds.help()
    if (str[:2] == 'ap'): cmds.ap(str)
    if (str[:2] == 'dp'): cmds.dp(str)
    if (str[:2] == 'cp'): cmds.cp(str)
    if (str[:2] == 'af'): cmds.af(str)
    if (str[:2] == 'wf'): cmds.wf(str)
    if (str[:2] == 'rf'): cmds.rf(str)
    if (str[:2] == 'df'): cmds.df(str)
    if (str[:5] == 'copyf'): cmds.copyf(str)
    if (str[:4] == 'renf'): cmds.renf(str)


while 1:
    cmd = input()
    result = processInput(cmd)

