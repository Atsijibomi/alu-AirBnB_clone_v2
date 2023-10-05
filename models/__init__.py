#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    """Instantiate DBStorage"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    """Instantiate FileStorage"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
