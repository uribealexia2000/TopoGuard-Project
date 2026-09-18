#-*-coding: utf-8 -*-

from Autodesk.Revit.DB import *
from snapshot import TopographySnapshot

def get_topographies(doc):
    """Devuelve todas las topografías del modelo."""

    collector = (
        FilteredElementCollector(doc)
        .OfClass(Architecture.TopographySurface)
    )

    resultado= []


    #eementos = list(collector)

    #print("Cantidad encontrada:", len(elementos))

    for topo in collector:
        
        #Ignorar las subregiones
        if topo.IsSiteSubRegion:
            continue
            
        #Obtener el nombre del subproyecto (Workset)
        parametro = topo.get_Parameter(
            BuiltInParameter.ELEM_PARTITION_PARAM
        )

        subproyecto = ""

        if parametro:
            subproyecto = parametro.AsValueString() or ""

        #Ignora superficies de plataforma
        if subproyecto.upper().startswith(("PLT", "P")):
            continue
     

#---------------------------------------------------
#Imprime informacion
#---------------------------------------------------

        print("------------------------")
        print("Nombre:", topo.Name)
        print("Es subregion:", topo.IsSiteSubRegion)
        print("Es elemento:", topo.Id.IntegerValue)
        #print("ID:", topo.Id.IntegerValue)
        #print("UniqueId:", topo.UniqueId)
        #print("PARAMETROS:")

        for p in topo.Parameters:

            try:
                nombre = p.Definition.Name
            except:
                continue

            if "reg" in nombre.lower() or "sub" in nombre.lower():
                print("  ", nombre, ":", p.AsValueString())
        

            try:
                print("Puntos:", topo.NumberOfPoints)
            except:
                pass

        if topo.Category:
            print("Categoria:", topo.Category.Name)

        print("Workset:", topo.WorksetId.IntegerValue)
        print("Subproyecto:", subproyecto)

        area = topo.get_Parameter(
            BuiltInParameter.HOST_AREA_COMPUTED
        )

        if area:
            print("Area:", area.AsDouble())

        else: 
            print("Area:", None)

        print("=====================================")
           #Guarda las plataformas que si interesan
        resultado.append(topo)
        print("=====================================")

    return resultado



def get_all_data(doc):
    #Devuelve la informacion de todas las topografias

    snapshots = []

    topografias = get_topographies(doc)
    print("Topografias encontradas:", len(topografias))

    for topo in topografias:
        snapshots.append(
            create_snapshot(topo)
        )
    print("Snapshots creados:", len(snapshots))
    return snapshots


def create_snapshot(topo):
    """
    Convierte una TopographySurface en un TopographySnapshot.
    """

    snap = TopographySnapshot()

    snap.UniqueId = topo.UniqueId

    snap.ElementId = topo.Id.IntegerValue

    snap.Name = topo.Name

    #Obtener el nombre del subproyecto (Workset)
    parametro = topo.get_Parameter(
        BuiltInParameter.ELEM_PARTITION_PARAM
    )
    if parametro:
        snap.Subproject = parametro.AsValueString() or ""

    bbox = topo.get_BoundingBox(None)

    if bbox:

        center = (bbox.Min + bbox.Max) / 2.0

        snap.Center["X"] = center.X
        snap.Center["Y"] = center.Y
        snap.Center["Z"] = center.Z

        snap.BoundingBox["MinX"] = bbox.Min.X
        snap.BoundingBox["MinY"] = bbox.Min.Y
        snap.BoundingBox["MinZ"] = bbox.Min.Z

        snap.BoundingBox["MaxX"] = bbox.Max.X
        snap.BoundingBox["MaxY"] = bbox.Max.Y
        snap.BoundingBox["MaxZ"] = bbox.Max.Z

    return snap