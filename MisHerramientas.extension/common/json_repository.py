# -*- coding: utf-8 -*-

import settings
import json_manager
import os
import project_manager

from snapshot import TopographySnapshot

def save_snapshots(doc, snapshots):

    #Guarda una lista de TopographySnapshot en el archivo JSON

    data = []

    for snap in snapshots:
        data.append(snap.to_dict())
    json_manager.save_json(   #Fuera del bucle
        project_manager.get_state_file(doc),
        data
        )

def load_snapshots(doc):

    data = json_manager.load_json(
        project_manager.get_state_file(doc)
    )

    if not data:
        return []

    snapshots = []

    for item in data:

        snap = TopographySnapshot()

        snap.UniqueId = item["UniqueId"]
        snap.ElementId = item["ElementId"]
        snap.Name = item["Name"]
        snap.Subproject = item["Subproject"]

        snap.Center = item["Center"]
        snap.BoundingBox = item["BoundingBox"]
        snapshots.append(snap)
    return snapshots


def has_snapshot(doc):

    return json_manager.file_exists(
        project_manager.get_state_file(doc)
    )

def delete_snapshot(doc):
    if has_snapshot():
        os.remove(
            project_manager.get_project_id(doc)
            )