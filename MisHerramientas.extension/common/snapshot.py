# -*- coding: utf-8 -*-

class TopographySnapshot(object):
    """
    Representa el estado de una TopographySurface.
    """

    def __init__(self):

        self.UniqueId = ""
        self.ElementId = -1
        self.Name = ""
        self.Subproject = ""

        self.Center = {
            "X": 0.0,
            "Y": 0.0,
            "Z": 0.0
        }

        self.BoundingBox = {
            "MinX": 0.0,
            "MinY": 0.0,
            "MinZ": 0.0,

            "MaxX": 0.0,
            "MaxY": 0.0,
            "MaxZ": 0.0
        }

    def to_dict(self):

        return {

            "UniqueId": self.UniqueId,

            "ElementId": self.ElementId,

            "Name": self.Name,

            "Center": self.Center,

            "BoundingBox": self.BoundingBox,

            "Subproject": self.Subproject

        }


    def equals(self, other, tolerance=0.001):
        """Compara dos snapshots con una tolerancia"""

        if self.UniqueId != other.UniqueId:
            return False

        #Centro
        for axis in ("X", "Y", "Z"):
            if abs(self.Center[axis] - other.Center[axis]) > tolerance:
                return False

        #Bounding Box minimo
        for axis in ("MinX", "MinY", "MinZ"):
            if abs(self.BoundingBox[axis] - other.BoundingBox[axis]) > tolerance:
                return False

        #Bounding Box maximo
        for axis in ("MaxX", "MaxY", "MaxZ"):
            if abs(self.BoundingBox[axis] - other.BoundingBox[axis]) > tolerance:
                return False

        return True