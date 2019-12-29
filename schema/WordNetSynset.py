#!/usr/bin/env python
""" generated source for module WordNetSynset """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
class WordNetSynset(object):
    """ generated source for class WordNetSynset """
    id = int()
    wnPos = str()
    wnOffset = str()
    example = str()
    gloss = str()
    synset = int()
    type_ = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, str, str, str, str, int, str)
    def __init___0(self, id, wnPos, wnOffset, example, gloss, synset, type_):
        """ generated source for method __init___0 """
        self.id = id
        self.wnPos = wnPos
        self.wnOffset = wnOffset
        self.example = example
        self.gloss = gloss
        self.synset = synset
        self.type_ = type_

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getWnPos(self):
        """ generated source for method getWnPos """
        return self.wnPos

    def getWnOffset(self):
        """ generated source for method getWnOffset """
        return self.wnOffset

    def getExample(self):
        """ generated source for method getExample """
        return self.example

    def getGloss(self):
        """ generated source for method getGloss """
        return self.gloss

    def getSynset(self):
        """ generated source for method getSynset """
        return self.synset

    def getType(self):
        """ generated source for method getType """
        return self.type_

