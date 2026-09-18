# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import UnitUtils, UnitTypeId


def build(result):
    lines = []

    lines.append("=" * 45)
    lines.append("      VALIDACION DE TOPOGRAFIAS")
    lines.append("=" * 45)
    lines.append("")


    #-----------------------------
    #Movidas
    #-----------------------------


    for movement in result.Moved:

        lines.append("! {}".format(
            movement.New.Subproject

        ))

        lines.append("")

        lines.append(
            "Movimiento detectado"
        )

        #Cambiar las unidades que ve el usuario a metros
        #EjeX
        dx = UnitUtils.ConvertFromInternalUnits(
            movement.DeltaX,
            UnitTypeId.Meters
        )

        #EjeY
        dy = UnitUtils.ConvertFromInternalUnits(
            movement.DeltaY,
            UnitTypeId.Meters
        )

        #EjeZ
        dz = UnitUtils.ConvertFromInternalUnits(
            movement.DeltaZ,
            UnitTypeId.Meters
        )

        #Distancia
        distance = UnitUtils.ConvertFromInternalUnits(
            movement.Distance,
            UnitTypeId.Meters
        )

        lines.append(
            "DX = {:.3f} m".format(dx)
        )

        lines.append(
            "DY = {:.3f} m".format(dy)
        )

        lines.append(
            "DZ = {:.3f} m".format(dz)
        )

        lines.append(
            "Distancia = {:.3f} m".format(distance)
        )

        lines.append("")



        #--------------------------
        #Eliminadas
        #-------------------------

    for topo in result.Deleted:

            lines.append(
                "X {} (Eliminada)".format(
                    topo.Subproject
                )
            )

        # ----------------------------
        # Nuevas
        # ----------------------------

    for topo in result.New:

        lines.append(
            "+ {} (Nueva)".format(
                topo.Subproject
            )
        )

        # ----------------------------
        # Sin cambios
        # ----------------------------

    for topo in result.Unchanged:

        lines.append(
            "-> {} (Sin cambios)".format(
                topo.Subproject
            )
        )

    lines.append("")
    lines.append("=" * 45)
    lines.append(
        "Total: {}".format(
            result.total_topographies
        )
    )

    return "\n".join(lines)



def build_details(item):
    """
    Construye el reporte de un solo elemento.
    Puede ser un Movement o un Snapshot.
    """

    lines = []

    # -----------------------------
    # Topografía movida
    # -----------------------------
    if hasattr(item, "Old"):

        dx = UnitUtils.ConvertFromInternalUnits(
            item.DeltaX,
            UnitTypeId.Meters
        )

        dy = UnitUtils.ConvertFromInternalUnits(
            item.DeltaY,
            UnitTypeId.Meters
        )

        dz = UnitUtils.ConvertFromInternalUnits(
            item.DeltaZ,
            UnitTypeId.Meters
        )

        distance = UnitUtils.ConvertFromInternalUnits(
            item.Distance,
            UnitTypeId.Meters
        )

        lines.append("Topografía")
        lines.append(item.New.Subproject)
        lines.append("")

        lines.append("Movimiento detectado")
        lines.append("")

        lines.append("DX = {:.3f} m".format(dx))
        lines.append("DY = {:.3f} m".format(dy))
        lines.append("DZ = {:.3f} m".format(dz))
        lines.append("")

        lines.append("Distancia = {:.3f} m".format(distance))

        return "\n".join(lines)

    # -----------------------------
    # Eliminada / Nueva / Sin cambios
    # -----------------------------

    lines.append("Topografía")
    lines.append(item.Subproject)
    lines.append("")

    return "\n".join(lines)
