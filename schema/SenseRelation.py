#!/usr/bin/env python
""" generated source for module SenseRelation """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
import farsnet.schema.Sense

import farsnet.service.SenseService

class SenseRelation(object):
    """ generated source for class SenseRelation """
    id = int()
    senseId1 = int()
    senseId2 = int()
    senseWord1 = str()
    senseWord2 = str()
    type_ = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, int, int, str, str, str)
    def __init___0(self, id, senseId1, senseId2, senseWord1, senseWord2, type_):
        """ generated source for method __init___0 """
        self.id = id
        self.senseId1 = senseId1
        self.senseId2 = senseId2
        self.senseWord1 = senseWord1
        self.senseWord2 = senseWord2
        self.type_ = type_

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getSenseId1(self):
        """ generated source for method getSenseId1 """
        return self.senseId1

    def getSenseId2(self):
        """ generated source for method getSenseId2 """
        return self.senseId2

    def getSenseWord1(self):
        """ generated source for method getSenseWord1 """
        return self.senseWord1

    def getSenseWord2(self):
        """ generated source for method getSenseWord2 """
        return self.senseWord2

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getSense1(self):
        """ generated source for method getSense1 """
        return SenseService.getSenseById(self.senseId1)

    def getSense2(self):
        """ generated source for method getSense2 """
        return SenseService.getSenseById(self.senseId2)

    def setId(self, id):
        """ generated source for method setId """
        self.id = id

    def setSenseId1(self, senseId1):
        """ generated source for method setSenseId1 """
        self.senseId1 = senseId1

    def setSenseId2(self, senseId2):
        """ generated source for method setSenseId2 """
        self.senseId2 = senseId2

    def setSenseWord1(self, senseWord1):
        """ generated source for method setSenseWord1 """
        self.senseWord1 = senseWord1

    def setSenseWord2(self, senseWord2):
        """ generated source for method setSenseWord2 """
        self.senseWord2 = senseWord2

    def setType(self, type_):
        """ generated source for method setType """
        self.type_ = type_

