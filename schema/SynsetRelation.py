#!/usr/bin/env python
""" generated source for module SynsetRelation """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
import farsnet.schema.Synset

import farsnet.service.SynsetService

class SynsetRelation(object):
    """ generated source for class SynsetRelation """
    id = int()
    type_ = str()
    synsetWords1 = str()
    synsetWords2 = str()
    synsetId1 = int()
    synsetId2 = int()
    reverseType = str()

    @overloaded
    def __init__(self, id, type_, synsetWords1, synsetWords2, synsetId1, synsetId2, reverseType):
        """ generated source for method __init__ """
        self.id = id
        self.type_ = type_
        self.synsetWords1 = synsetWords1
        self.synsetWords2 = synsetWords2
        self.synsetId1 = synsetId1
        self.synsetId2 = synsetId2
        self.reverseType = reverseType

    @__init__.register(object)
    def __init___0(self):
        """ generated source for method __init___0 """

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def getSynsetWords1(self):
        """ generated source for method getSynsetWords1 """
        return self.synsetWords1

    def getSynsetWords2(self):
        """ generated source for method getSynsetWords2 """
        return self.synsetWords2

    def getSynsetId1(self):
        """ generated source for method getSynsetId1 """
        return self.synsetId1

    def getSynsetId2(self):
        """ generated source for method getSynsetId2 """
        return self.synsetId2

    def getReverseType(self):
        """ generated source for method getReverseType """
        return self.reverseType

    def getSynset1(self):
        """ generated source for method getSynset1 """
        return SynsetService.getSynsetById(self.synsetId1)

    def getSynset2(self):
        """ generated source for method getSynset2 """
        return SynsetService.getSynsetById(self.synsetId2)

    def setType(self, type_):
        """ generated source for method setType """
        self.type_ = type_

    def setSynsetWords1(self, synsetWords1):
        """ generated source for method setSynsetWords1 """
        self.synsetWords1 = synsetWords1

    def setSynsetWords2(self, synsetWords2):
        """ generated source for method setSynsetWords2 """
        self.synsetWords2 = synsetWords2

    def setSynsetId1(self, synsetId1):
        """ generated source for method setSynsetId1 """
        self.synsetId1 = synsetId1

    def setSynsetId2(self, synsetId2):
        """ generated source for method setSynsetId2 """
        self.synsetId2 = synsetId2

    def setReverseType(self, reverseType):
        """ generated source for method setReverseType """
        self.reverseType = reverseType

