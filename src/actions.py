from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
from os import path
import os
import re
import numpy as np
import glob


class FileActions():

    global source_path
    global destination_path
    global new_location
    global files_to_copy
    # Задайте имя файла с путем
    source_path = "/home/markus/devops/personal/file-sorter/src/to_sort/*.pdf"
    # Задайте путь к каталогу, в который будет перемещен файл
    destination_path = "/home/markus/devops/personal/file-sorter/src/sorted/pdf"
    new_location = shutil.move(source_path, destination_path)
    
    files_to_copy = glob.glob("/home/markus/devops/personal/file-sorter/src/to_sort/1245.pdf")
    # Заглавная стартующая функция
    
    
    
    def __init__(self):
        self.getCurrentState()
        current_path = os.getcwd()
        
        if os.path.exists(current_path):
            self.askExists()
            # self.moveFile()
            #print("% s перемещен в указанное место,% s" % (source_path , new_location))
        elif os.path.isfile(current_path):
            self.askExists()
            # self.moveFile()
            #print("% s перемещен в указанное место,% s" % (source_path , new_location))
        elif os.path.isdir(current_path):
            self.askExists()
            # self.moveFile()
            #print("% s перемещен в указанное место,% s" % (source_path , new_location))
        else:
            # Распечатать сообщение, если файл не существует
            print ("Файлов pdf не существует.")
            print ("Ухожу в ожидание...")

    # Отображаем текущую директорию и содержимое

    def getCurrentState(self):
        current_path = os.getcwd()
        for dirs, folders, files in os.walk(current_path):
            print('Текущий каталог:', dirs)
            print('Вложенные папки:', folders)
            print('Файлы в папке:', files)
            print('\n')
            # Отобразит только файлы и папки в текущей директории
            break
        
    # Проверка существования файлов с определенными расширениями и объявление переменных

    def askExists(self):
        # self.extension = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'rar', 'zip', '7z', 'exe', 'txt', 'xlsx', 'xls']
        # extension_alone = np.array_split(self.extension, 13)
        
        if os.path.exists('^.{3,20}$\.pdf'):
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            current_path = os.getcwd()
            