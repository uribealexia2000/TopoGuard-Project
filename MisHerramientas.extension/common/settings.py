# -*- coding: utf-8 -*-

import os

# ====================================================
# TopoGuard Settings
# ====================================================

PLUGIN_NAME = "TopoGuard"
VERSION = "1.0.0"

# Carpeta principal donde se guardarán los datos
DATA_FOLDER = r"C:\Temp\TopoGuard"

# Crear la carpeta si no existe
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Archivos principales
STATE_FILE = os.path.join(DATA_FOLDER, "TopoGuard.json")
LOG_FILE = os.path.join(DATA_FOLDER, "TopoGuard.log")

# Carpeta de respaldos
BACKUP_FOLDER = os.path.join(DATA_FOLDER, "Backups")

# Crear carpeta de respaldos si no existe
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)


 # Configuración de comportamiento

MAX_BACKUPS = 20          # Número máximo de respaldos

AUTO_BACKUP = True        # Crear respaldo antes de registrar

DEBUG = False             # Imprimir mensajes de depuració