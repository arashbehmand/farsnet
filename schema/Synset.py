#!/usr/bin/env python
""" generated source for module Synset """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
import farsnet.schema.Sense

import farsnet.schema.SynsetExample

import farsnet.schema.SynsetGloss

import farsnet.schema.SynsetRelation

import farsnet.schema.SynsetRelationType

import farsnet.schema.WordNetSynset

import farsnet.service.SenseService

import farsnet.service.SynsetService

import java.util.List

class Synset(object):
    """ generated source for class Synset """
    id = int()
    pos = str()
    semanticCategory = str()
    nofather = str()
    noMapping = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, str, str, str, str, str, str)
    def __init___0(self, id, pos, semanticCategory, example, gloss, nofather, noMapping):
        """ generated source for method __init___0 """
        self.id = id
        self.semanticCategory = semanticCategory
        self.nofather = nofather
        self.noMapping = noMapping
        self.pos = pos

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getSemanticCategory(self):
        """ generated source for method getSemanticCategory """
        return self.semanticCategory

    def getNoMapping(self):
        """ generated source for method getNoMapping """
        return self.noMapping

    def getNofather(self):
        """ generated source for method getNofather """
        return self.nofather

    def getPos(self):
        """ generated source for method getPos """
        return self.pos

    def getExamples(self):
        """ generated source for method getExamples """
        return SynsetService.getSynsetExamples(self.id)

    def getGlosses(self):
        """ generated source for method getGlosses """
        return SynsetService.getSynsetGlosses(self.id)

    def getSenses(self):
        """ generated source for method getSenses """
        return SenseService.getSensesBySynset(self.id)

    def getWordNetSynsets(self):
        """ generated source for method getWordNetSynsets """
        return SynsetService.getWordNetSynsets(self.id)

    @overloaded
    def getSynsetRelations(self):
        """ generated source for method getSynsetRelations """
        return SynsetService.getSynsetRelationsById(self.id)

    @getSynsetRelations.register(object, SynsetRelationType)
    def getSynsetRelations_0(self, relationType):
        """ generated source for method getSynsetRelations_0 """
        types = [None]*
        return SynsetService.getSynsetRelationsByType(self.id, types)

    @getSynsetRelations.register(object, SynsetRelationType)
    def getSynsetRelations_1(self, relationTypes):
        """ generated source for method getSynsetRelations_1 """
        return SynsetService.getSynsetRelationsByType(self.id, relationTypes)

