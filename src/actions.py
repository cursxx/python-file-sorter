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
    global current_path
    
    current_path = os.getcwd()
    # задайте имя файла с путем
    source_path = "/home/markus/devops/personal/file-sorter/src/to_sort/"
    # задайте путь к каталогу, в который будет перемещен файл
    destination_path = "/home/markus/devops/personal/file-sorter/src/sorted/pdf/"    # эта директория не существует
    
    # заглавная стартующая функция
    def __init__(self):
        self.getCurrentState()
        
        if os.path.exists(current_path):
            self.askExists()
            print("файлы из директории % s скопированы в % s" % (source_path , destination_path))
            
        elif os.path.isfile(current_path):
            self.askExists()
            print("файлы из директории % s скопированы в % s" % (source_path , destination_path))
            
        # elif os.path.isdir(current_path):
        #     self.askExists()
        #     print("файлы из директории % s скопированы в % s" % (source_path , destination_path))
        else:
            # распечатать сообщение, если файл не существует
            print ("Файлов pdf не существует.")
            print ("Ухожу в ожидание...")

    # отображаем текущую директорию и содержимое
    def getCurrentState(self):
        for dirs, folders, files in os.walk(current_path):
            print('Текущий каталог:', dirs)
            print('Вложенные папки:', folders)
            print('Файлы в папке:', files)
            print('\n')
            # отобразит только файлы и папки в текущей директории
            break
        
    # проверка существования файлов с определенными расширениями и объявление переменных
    def askExists(self):
        # если файл существует, то перемещаем его в целевую директорию
        if os.path.exists(source_path):
            # если целевая директория не существует, то создаем ее
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # для root, директорий и файлов в текущей директории
            for root, dirs, files in os.walk(current_path): 
                for file in files: 
                    # если файл имеет в названии .pdf, то перемещаем его в целевую директорию
                    if file.endswith(".pdf"):
                        shutil.copyfile(source_path + file, destination_path + file)