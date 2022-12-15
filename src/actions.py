from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
from os import path
import os
import re
import numpy as np



class FileActions():

    global source_path
    global destination_path
    global new_location
    
    # задайте имя файла с путем
    source_path = "/home/markus/devops/personal/file-sorter/src/to_sort/1245.pdf"
    # задайте путь к каталогу, в который будет перемещен файл
    destination_path = "/home/markus/devops/personal/file-sorter/src/sorted/"
    
    # заглавная стартующая функция
    def __init__(self):
        self.getCurrentState()
        current_path = os.getcwd()
        if os.path.exists(current_path):
            self.askExists()
            print("% s перемещен в указанное место,% s" % (source_path , destination_path))
            
        elif os.path.isfile(current_path):
            self.askExists()
            print("% s перемещен в указанное место,% s" % (source_path , destination_path))
            
        elif os.path.isdir(current_path):
            self.askExists()
            print("% s перемещен в указанное место,% s" % (source_path , destination_path))
        else:
            # распечатать сообщение, если файл не существует
            print ("Файлов pdf не существует.")
            print ("Ухожу в ожидание...")

    # отображаем текущую директорию и содержимое
    def getCurrentState(self):
        current_path = os.getcwd()
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
            current_path = os.getcwd()
            shutil.move(source_path, destination_path)
            if 
            