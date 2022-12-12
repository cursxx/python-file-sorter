from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
from os import path
import os
import re

extension = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'rar', 'zip', '7z', 'exe', 'txt', 'xlsx', 'xls']
current_path = os.getcwd()

class FileActions():
    
    # Заглавная стартующая функция
    def __init__():
        getCurrentState()
        fileControl()
    
    # Основной цикл сортировки файлов
    def fileControl():
        if os.path.exists(current_path):
            if os.path.exists(current_path):
                askExists()
                moveFile()
                print("% s перемещен в указанное место,% s" % (source_path , new_location))
            elif os.path.isfile(current_path):
                askExists()
                moveFile()
                print("% s перемещен в указанное место,% s" % (source_path , new_location))
            elif os.path.isdir(current_path):
                askExists()
                moveFile()
                print("% s перемещен в указанное место,% s" % (source_path , new_location))
        else:
            # Распечатать сообщение, если файл не существует
            print ("Файлов pdf не существует.")
            print ("Ухожу в ожидание...")
        
# Вспомогательные функции

    # Отображаем текущую директорию и содержимое
    def getCurrentState():
        for dirs, folders, files in os.walk(current_path):
            print('Текущий каталог:', dirs)
            print('Вложенные папки:', folder)
            print('Файлы в папке:', files)
            print('\n')
            # Отобразит только файлы и папки в текущей директории
            break
    
    # Функция перемещения файлов 
    def moveFile():
        new_location = shutil.move(source_path, destination_path)
    
    # Проверка существования файлов с определенными расширениями и объявление переменных
    def askExists():
        for fileNumber in extension.split:
            if os.path.exists('^.{3,20}$\.' + extension.split[fileNumber]):
                # Задайте имя файла с путем
                source_path = "/home/ubuntu/to_sort/^.{3,20}$\." + extension[fileNumber]
                # Задайте путь к каталогу, в который будет перемещен файл
                destination_path = "/home/ubuntu/sorted/" + extension[fileNumber]
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)