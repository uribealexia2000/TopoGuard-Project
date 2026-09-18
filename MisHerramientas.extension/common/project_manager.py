# -*- coding: utf-8 -*-

import os
import hashlib

from Autodesk.Revit.DB import ModelPathUtils


def _get_project_path(doc):
    """
    Devuelve la ruta del proyecto.
    Si es un modelo con Worksharing utiliza la ruta del modelo central.
    """

    if doc.IsWorkshared:

        central = doc.GetWorksharingCentralModelPath()

        return ModelPathUtils.ConvertModelPathToUserVisiblePath(
            central
        )

    return doc.PathName


def get_project_name(doc):
    """
    Devuelve el nombre del proyecto sin extensión.
    """

    path = _get_project_path(doc)

    return os.path.splitext(
        os.path.basename(path)
    )[0]


def get_project_id(doc):
    """
    Devuelve un identificador único del proyecto.
    """

    path = _get_project_path(doc)

    return hashlib.md5(
        path.encode("utf-8")
    ).hexdigest()[:12]


def get_state_file(doc):

    import settings

    return os.path.join(
        settings.DATA_FOLDER,
        "{}_{}.json".format(
            get_project_name(doc),
            get_project_id(doc)
        )
    )