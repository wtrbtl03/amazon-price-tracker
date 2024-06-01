from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if (event.src_path == ".\\products_file.csv"):
            print("edited")


observer = Observer()
observer.schedule(Handler(), ".")
observer.start()

try:
    while(True):
        pass
except KeyboardInterrupt:
    observer.stop()


