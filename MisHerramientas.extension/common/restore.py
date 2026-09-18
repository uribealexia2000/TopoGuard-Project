# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import *

def restore(doc, movement):
    """
    Restaura una topografía movida a su posición original.
    """

    if movement is None:
        raise Exception("Movimiento inválido.")

    # Buscar el elemento en el modelo
    topo = doc.GetElement(
        ElementId(movement.New.ElementId)
    )

    if topo is None:
        raise Exception("No se encontró la topografía.")

    # Vector desde la posición actual hacia la original
    vector = XYZ(
        movement.Old.Center["X"] - movement.New.Center["X"],
        movement.Old.Center["Y"] - movement.New.Center["Y"],
        movement.Old.Center["Z"] - movement.New.Center["Z"]
    )

    t = Transaction(doc, "TopoGuard - Restaurar topografía")

    t.Start()

    ElementTransformUtils.MoveElement(
        doc,
        topo.Id,
        vector
    )

    t.Commit()