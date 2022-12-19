from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import time
import os

# объявляем глобальные переменные
global source_path
global destination_path
global new_location
global current_path

current_path = os.getcwd()
# задайте имя файла с путем
source_path = current_path + "/to_sort/"
# задайте путь к каталогу, в который будет перемещен файл
destination_path = current_path + "/sorted/"    # эта директория не существует

extensions = ["pdf", "html", "htm", "jpg", "png", "docx", "svg", "avi", "xlsx", "xls", "txt"]

class Watcher:
    # Set the directory on watch
    watchDirectory = os.getcwd()

    def __init__(self):
        self.observer = Observer()
        
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
            fileMover()
                        
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)
            fileMover()
                        
        elif event.event_type == 'on_deleted':
            print(f"what the f**k! Someone deleted {event.src_path}!")
            fileMover()

        elif event.event_type == 'on_moved':
            print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
            fileMover()
            
def fileMover():
    # для root, директорий и файлов в текущей директории
    for root, dirs, files in os.walk(source_path): 
        for file in files: 
            for extensionType in extensions:
                # если файл имеет в названии .pdf, то перемещаем его в целевую директорию
                if file.endswith("." + extensionType):
                    if not os.path.exists(destination_path + extensionType):
                        os.makedirs(destination_path + extensionType)
                    # перемещаем файл в директорию, назначенную файлам с определенным расширением
                    shutil.move(source_path + file, destination_path + extensionType)


if __name__ == '__main__':
    watch = Watcher()
    watch.run()