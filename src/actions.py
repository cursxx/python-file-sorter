from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
from os import path
import os
import re
import numpy as np



class FileActions():
    
    # Заглавная стартующая функция
    def __init__(self):
        self.getCurrentState()
        if os.path.exists(self.current_path):
            if os.path.exists(self.current_path):
                self.askExists()
                self.moveFile()
                print("% s перемещен в указанное место,% s" % (source_path , new_location))
            elif os.path.isfile(self.current_path):
                self.askExists()
                self.moveFile()
                print("% s перемещен в указанное место,% s" % (source_path , new_location))
            elif os.path.isdir(self.current_path):
                self.askExists()
                self.moveFile()
                print("% s перемещен в указанное место,% s" % (source_path , new_location))
        else:
            # Распечатать сообщение, если файл не существует
            print ("Файлов pdf не существует.")
            print ("Ухожу в ожидание...")
        
# Вспомогательные функции

    # Отображаем текущую директорию и содержимое
    def getCurrentState(self):
        self.current_path = os.getcwd()
        for dirs, folders, files in os.walk(self.current_path):
            print('Текущий каталог:', dirs)
            print('Вложенные папки:', folders)
            print('Файлы в папке:', files)
            print('\n')
            # Отобразит только файлы и папки в текущей директории
            break
    
    # Функция перемещения файлов 
    def moveFile(self):
        new_location = shutil.move(source_path, destination_path)
    
    # Проверка существования файлов с определенными расширениями и объявление переменных
    def askExists(self):
        self.extension = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'rar', 'zip', '7z', 'exe', 'txt', 'xlsx', 'xls']
        extension_alone = np.array_split(self.extension, 13)
        for fileNumber in self.extension:
            if os.path.exists('^.{3,20}$\.', self.extension[fileNumber]):
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                self.current_path = os.getcwd()
                # Задайте имя файла с путем
                self.source_path = "/home/markus/devops/personal/file-sorter/src/to_sort/^.{3,20}$\." + extension
                # Задайте путь к каталогу, в который будет перемещен файл
                self.destination_path = "/home/markus/devops/personal/file-sorter/src/sorted/" + extension