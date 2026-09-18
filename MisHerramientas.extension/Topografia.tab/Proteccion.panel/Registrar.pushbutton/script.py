# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os
import sys

from pyrevit import forms
from pyrevit import script

doc = __revit__.ActiveUIDocument.Document

# ----------------------------------------------------
# Localizar carpeta common
# ----------------------------------------------------

current = script.get_script_path()

while not current.endswith(".extension"):

    parent = os.path.dirname(current)

    if parent == current:
        raise Exception("No se encontró la extensión.")

    current = parent

common = os.path.join(current, "common")

if common not in sys.path:
    sys.path.insert(0, common)

# ----------------------------------------------------

import bootstrap

bootstrap.initialize()

import state_manager

cantidad = state_manager.register(doc)

forms.alert(
    "Se registraron {} topografías.".format(cantidad),
    title="TopoGuard"
)