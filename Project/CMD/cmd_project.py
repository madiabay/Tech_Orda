import datetime
import os
import pathlib
import shutil
from pathlib import Path
from exceptions import *

os.chdir('/')

while True:
    command = input(os.getcwd() + '$ ').split()
    match command:
        case ['ls'] | ['dir']:
            print('Cписок директория/файл: ')
            with os.scandir(os.getcwd()) as entries:
                for entry in entries:
                    print('    ', end='')

                    print(entry.name)
        
        case 'cd', '..':
            if os.getcwd() == '/':
                try:
                    raise TheLastDirectory
                except TheLastDirectory as e:
                    print(e)
            else:
                a = os.getcwd().split('/')

                if len(a) == 2:
                    os.chdir('/')
                else:
                    a.pop()
                    os.chdir('/'.join(a))
                
                print(f'Ваш текущий каталог - {os.getcwd()}')
        
        case 'cd', input_dir:
            dir_list = [dir.name for dir in os.scandir()]
            if input_dir in dir_list:
                os.chdir(os.getcwd() + '/' + input_dir)

                print(f'Ваш текущий каталог - {os.getcwd()}')
            else:
                try:
                    raise DirNotFound
                except DirNotFound as e:
                    print(e)
        
        case 'md' | 'mkdir', dir_name:
            os.mkdir(dir_name)
        
        case 'rm', name:
            try:
                os.remove(name)
            except:
                path_dir = pathlib.Path(name)

                shutil.rmtree(path_dir)
                
                # os.rmdir(name)

        case 'mv', old_name, new_name:
            try:
                os.rename(old_name, new_name)
            except FileNotFoundError as e:
                print(e)
        
        case 'cat', filename:
            path = Path(os.getcwd() + '/' + filename)
            
            if path.is_file():
                with open(file=filename, mode='r') as file:
                    print(file.read())
            else:
                print('No such file or directory')
        
        case ['q']:
            break

        case []:
            continue

        case 'show', 'time':
            print(datetime.datetime.now())

        case _:
            print('Command not found')