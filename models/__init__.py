#!/usr/bin/python3
"""initialize the models package"""

from os import getenv

<<<<<<< HEAD
=======

>>>>>>> c498d92c4d55add0dbea5dfea46a43cbc7c8f45d
storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
