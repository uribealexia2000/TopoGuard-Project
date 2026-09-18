# -*- coding: utf-8 -*-

import os
import datetime

import settings
import json_manager


_initialized = False


def initialize():
    """
    Crea la carpeta y el archivo de log si aun no existen.
    """

    global _initialized

    if _initialized:
        return

    json_manager.ensure_data_folder()

    if not os.path.exists(settings.LOG_FILE):
        with open(settings.LOG_FILE, "w") as fp:
            fp.write("========== TOPOGUARD ==========\n")

    _initialized = True


def write(message):

    initialize()

    now = datetime.datetime.now()

    line = "[{}] {}\n".format(
        now.strftime("%Y-%m-%d %H:%M:%S"),
        message
    )

    with open(settings.LOG_FILE, "a") as fp:
        fp.write(line)


def info(message):
    write("[INFO] " + message)


def warning(message):
    write("[WARNING] " + message)


def error(message):
    write("[ERROR] " + message)