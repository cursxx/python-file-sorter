# импортируем необходимые для работы модули
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import time
import os

# объявляем глобальные переменные для использования их внутри любой функции и класса
global source_path
global destination_path
global new_location
global current_path

# присваиваем текущую директорию переменной
current_path = os.getcwd()
# задаем имя файла с путем
source_path = current_path + "/to_sort/"
# задаем путь к каталогу, в который будет перемещен файл
destination_path = current_path + "/sorted/"    # эта директория не существует

# назначаем список расширений, которые будут использоваться для сортировки
extensions = ["pdf", "html", "htm", "jpg", "png", "docx", "svg", "avi", "xlsx", "xls", "txt"]

# объявляем класс, в котором инициализируем модуль watchdog и запускаем мониторинг
class Watcher:
    # функция инициализации метода Observer, присвоение метода кастомной переменной для упрощенного использования
    def __init__(self):
        self.observer = Observer()
    
    # функция, переводящая скрипт в режим мониторинга
    def run(self):
        event_handler = Handler()
        # задаем правила для работы(
        # event_handler - запускает методы из класса Handler, которые означают события, которые будут отслеживаться; 
        # current_path - указывает рабочую директорию, в которой будет запущен скрипт,
        # recursive = True - запускаем код рекурсивно )
        self.observer.schedule(event_handler, current_path, recursive = True)
        # запускаем нашу функцию
        self.observer.start()
        # переводим ее в режим вечного ожидания
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()

# объявляем класс, в котором описываем методы для отслеживания событий в рабочей директории
class Handler(FileSystemEventHandler):

    @staticmethod
    # для любого события
    def on_any_event(event):
        # если событие произошло с директорией, то возвращаем None, т.к. наша цель - файлы
        if event.is_directory:
            return None

        # если файл создан, то выводим сообщение об этом и запускаем функцию файлов и перемещения
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Someone created - % s." % event.src_path)
            fileMover()
                        
        # если файл изменен, то выводим сообщение об этом и запускаем функцию файлов и перемещения
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Someone modified - % s." % event.src_path)
            fileMover()
        
        # если файл удален, то выводим сообщение об этом и запускаем функцию файлов и перемещения
        elif event.event_type == 'on_deleted':
            print(f"Someone deleted {event.src_path}!")
            fileMover()

        # если файл перемещен, то выводим сообщение об этом и запускаем функцию поиска файлов и перемещения
        elif event.event_type == 'on_moved':
            print(f"Someone moved {event.src_path} to {event.dest_path}")
            fileMover()
            
            
# функция перебора файлов, соответствующих условиям
def fileMover():
    # для root, директорий и файлов в текущей директории
    for root, dirs, files in os.walk(source_path): 
        # перебираем файлы в директории
        for file in files: 
            # перебираем расширения для этих файлов
            for extensionType in extensions:
                # если файл имеет в названии одно из искомых расширенний, то перемещаем его в целевую директорию
                if file.endswith("." + extensionType):
                    # если целевая директория не существует, то создаем ее
                    if not os.path.exists(destination_path + extensionType):
                        os.makedirs(destination_path + extensionType)
                    # перемещаем файл в директорию, назначенную файлам с определенным расширением
                    shutil.move(source_path + file, destination_path + extensionType)

# запускаем скрипт
if __name__ == '__main__':
    watch = Watcher()
    watch.run()