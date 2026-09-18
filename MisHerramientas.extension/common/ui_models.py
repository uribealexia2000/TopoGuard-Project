# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import UnitUtils, UnitTypeId


class TopographyRow(object):
    """Representa una fila del DataGrid."""

    def __init__(self):

        self.Status = ""
        self.Name = ""
        self.Change = ""
        self.Distance = ""

        #Nuevo
        self.Data = None

def build_rows(result):
    """
    Convierte un ComparisonResult en una lista de filas
    para mostrar en la interfaz.
    """

    rows = []

    # ----------------------------
    # Movidas
    # ----------------------------

    for movement in result.Moved:

        row = TopographyRow()

        row.Status = "🟡"

        # Si agregaste Subproject al Snapshot
        row.Name = getattr(
            movement.New,
            "Subproject",
            movement.New.Name
        )

        row.Change = "Movida"

        distancia = UnitUtils.ConvertFromInternalUnits(
            movement.Distance,
            UnitTypeId.Meters
        )

        row.Distance = "{:.3f}".format(distancia)

        row.Data = movement

        rows.append(row)

    # ----------------------------
    # Eliminadas
    # ----------------------------

    for topo in result.Deleted:

        row = TopographyRow()

        row.Status = "🔴"

        row.Name = getattr(
            topo,
            "Subproject",
            topo.Name
        )

        row.Change = "Eliminada"

        row.Distance = "-"

        row.Data = topo

        rows.append(row)

    # ----------------------------
    # Nuevas
    # ----------------------------

    for topo in result.New:

        row = TopographyRow()

        row.Status = "🔵"

        row.Name = getattr(
            topo,
            "Subproject",
            topo.Name
        )

        row.Change = "Nueva"

        row.Distance = "-"

        row.Data = topo

        rows.append(row)

    # ----------------------------
    # Sin cambios
    # ----------------------------

    for topo in result.Unchanged:

        row = TopographyRow()

        row.Status = "🟢"

        row.Name = getattr(
            topo,
            "Subproject",
            topo.Name
        )

        row.Change = "Sin cambios"

        row.Distance = "-"

        row.Data = topo

        rows.append(row)

    return rows