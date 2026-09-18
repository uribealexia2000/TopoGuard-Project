
# -*- coding: utf-8 -*-

import os
import sys

from pyrevit import forms
from pyrevit import script



doc = __revit__.ActiveUIDocument.Document

current = script.get_script_path()

while not current.endswith(".extension"):

    parent = os.path.dirname(current)

    if parent == current:
        raise Exception("No se encontró la extensión.")

    current = parent

#Agrega la carpeta common en el sys.path
common = os.path.join(current, "common")

if common not in sys.path:
    sys.path.insert(0, common)


#Agrega la carpeta ui en el sys.path
ui = os.path.join(current, "ui")

if ui not in sys.path:
    sys.path.insert(0, ui)


import report
import bootstrap
import ValidationWindow

bootstrap.initialize()

import state_manager

resultado = state_manager.validate(doc)

ventana = ValidationWindow.ValidationWindow(
    doc,
    resultado,
    report.build(resultado)
)
ventana.ShowDialog()


