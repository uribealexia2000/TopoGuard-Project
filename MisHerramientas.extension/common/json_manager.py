# -*- coding: utf-8 -*-

import os
import json
import codecs
import settings


def ensure_data_folder():
    """Create data folders if they do not exist."""

    if not os.path.exists(settings.DATA_FOLDER):
        os.makedirs(settings.DATA_FOLDER)

    if not os.path.exists(settings.BACKUP_FOLDER):
        os.makedirs(settings.BACKUP_FOLDER)


def file_exists(path):
    return os.path.exists(path)


def load_json(path):

    if not file_exists(path):
        return None

    with codecs.open(path, "r", "utf-8") as fp:
        return json.load(fp)


def save_json(path, data):

    ensure_data_folder()

    with codecs.open(path, "w", "utf-8") as fp:
        json.dump(
            data,
            fp,
            indent=4,
            ensure_ascii=False
        )