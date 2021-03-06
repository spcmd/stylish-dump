import os
import time

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import config
from database import Model


class Style(Model):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True)
    url = Column(Text)
    updateUrl = Column(Text)
    md5Url = Column(Text)
    name = Column(Text)
    code = Column(Text)
    enabled = Column(Boolean)
    originalCode = Column(Text)
    idUrl = Column(Text)
    applyBackgroundUpdates = Column(Boolean)
    originalMd5 = Column(Text)

class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path not in files:
            return
        print event.src_path
        style = Style.query.filter(Style.id==files[event.src_path]).first()
        with open(event.src_path, 'r') as f:
            style.code = f.read()
            style.save()

styles = Style.query.all()
files = {}

for style in styles:
    path = '%s/%s.css' % (config.OUTPUT_DIR, style.name)
    files[path] = style.id
    f = open(path, 'w')
    f.write(style.code)
    f.close()

if __name__ == '__main__':
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, config.OUTPUT_DIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
