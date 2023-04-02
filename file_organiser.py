import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from dir = "C:/Users/Ishaq Pasha/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_create(self, event):
        print(f"Hey, {event.src_path} Has been created!")

    def on_create(self, event):
        print(f"Oops! someone deleted {event.src_path}!")

    def on_create(self, event):
        print(f"Hey there!, {event.src_path} has been modified")

    def on_create(self, event):
        print(f"Someone moved {event.src_path} to {event.dest_path}")



event_handler =FileElementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)


observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()