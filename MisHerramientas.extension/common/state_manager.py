# -*- coding: utf-8 -*-

import topo_repository
import json_repository
import logger
import comparison
import report


def register(doc):
    """
    Registra el estado actual de las topografías.
    """

    snapshots = topo_repository.get_all_data(doc)

    print("Cantidad de snapshots:", len(snapshots))

    for s in snapshots[:10]:
        print(s.ElementId, s.Name, s.Subproject)


    json_repository.save_snapshots(doc, snapshots)

    logger.info(
        "Se registraron {} topografías.".format(len(snapshots))
    )

    return len(snapshots)


def validate(doc):
    """
    Compara el estado actual con el estado registrado.
    """

    # Verificar que exista un registro
    if not json_repository.has_snapshot(doc):

        logger.warning("No existe un estado registrado.")

        raise Exception(
            "Primero debes registrar el estado del proyecto."
        )

    # Leer estado guardado
    old_snapshots = json_repository.load_snapshots(doc)

    # Leer estado actual
    new_snapshots = topo_repository.get_all_data(doc)

    # Comparar
    result = comparison.compare(
        old_snapshots,
        new_snapshots
    )

    #Construir reporte
    texto = report.build(result)

    print(texto)

    logger.info("Validación completada.")

    return result