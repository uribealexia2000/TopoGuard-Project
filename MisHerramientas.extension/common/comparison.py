# -*- coding: utf-8 -*-

class Movement(object):
#Almacena la informacion del movimiento
    def __init__(self):

        self.Old = None
        self.New = None

        self.DeltaX = 0.0
        self.DeltaY = 0.0
        self.DeltaZ = 0.0

    @property  #Muestra la distancia total que fue movida la topografia
    def Distance(self):

        return (
            self.DeltaX ** 2 +
            self.DeltaY ** 2 +
            self.DeltaZ ** 2 
        ) ** 0.5


class ComparisonResult(object):

    def __init__(self):

        self.New = []
        self.Deleted = []
        self.Moved = []
        self.Unchanged = []

    @property
    def has_changes(self):
        """ Indica si existe al menos un cambio """

        return (
            len(self.New) > 0 or
            len(self.Deleted) > 0 or
            len(self.Moved) > 0
        )

    @property
    def total_changes(self):

        return(
            len(self.New) +
            len(self.Deleted) +
            len(self.Moved) 
        )

    @property
    def total_topographies(self):

        return(
            len(self.New) +
            len(self.Deleted) +
            len(self.Moved) +
            len(self.Unchanged)
        )


#Funciones del modulo

#Coordina el proceso de comparar eliminados, nuevos, movidos y sin cambios
def compare(old_snapshots, new_snapshots):

        result = ComparisonResult()

        old_dict = make_dictionary(old_snapshots)
        new_dict = make_dictionary(new_snapshots)

        detect_deleted(result, old_dict, new_dict)
        detect_new(result, old_dict, new_dict)
        detect_moved(result, old_dict, new_dict)
        detect_unchanged(result, old_dict, new_dict)

        return result


#Detectar eliminados
def detect_deleted(result, old_dict, new_dict):

    for uid in old_dict:
        if uid not in new_dict:
            result.Deleted.append(old_dict[uid])


#Detectar nuevos
def detect_new(result, old_dict, new_dict):

    for uid in new_dict:

        if uid not in old_dict:

            result.New.append(new_dict[uid])

        


#Detectar sin cambios
def detect_unchanged(result, old_dict, new_dict):

    for uid in old_dict:

        if uid not in new_dict:
            continue

        old= old_dict[uid]
        new= new_dict[uid]

        if old.equals (new):

                result.Unchanged.append(new)


#Detectar movidos
def detect_moved(result, old_dict, new_dict):

    for uid in old_dict:

        if uid not in new_dict:
            continue

        old = old_dict[uid]
        new = new_dict[uid]

        if old.equals(new):
            continue

        movement = Movement()

        movement.Old = old
        movement.New = new

        movement.DeltaX = (
            new.Center["X"] -
            old.Center["X"]
        )

        movement.DeltaY = (
            new.Center["Y"] -
            old.Center["Y"]
        )

        movement.DeltaZ = (
            new.Center["Z"] -
            old.Center["Z"]
        )

        result.Moved.append(movement)



#Hacer el diccionario o lista
def make_dictionary(snapshots):

        dic = {}

        for snap in snapshots:
            dic[snap.UniqueId] =snap

        return dic
