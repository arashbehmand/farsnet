#!/usr/bin/env python
""" generated source for module Sense """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
import farsnet.schema.SenseRelation

import farsnet.schema.SenseRelationType

import farsnet.schema.Synset

import farsnet.schema.Word

import farsnet.service.SenseService

import farsnet.service.SynsetService

import java.util.List

class Sense(object):
    """ generated source for class Sense """
    id = int()
    seqId = str()
    value = str()
    word = Word()
    verbTransitivity = str()
    verbActivePassive = str()
    verbType = str()
    synset = str()
    verbPastStem = str()
    verbPresentStem = str()
    nounCategory = str()
    nounPluralType = str()
    pronoun = str()
    nounNumeralType = str()
    adverbType1 = str()
    adverbType2 = str()
    preNounAdjectiveType = str()
    adjectiveType2 = str()
    nounSpecifityType = str()
    nounType = str()
    adjectiveType1 = str()
    isCausative = bool()
    isIdiomatic = bool()
    transitiveType = str()
    isAbbreviation = bool()
    isColloquial = bool()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, str, str, str, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, bool, bool, str, bool, bool)
    def __init___0(self, id, seqId, pos, defaultValue, wordId, defaultPhonetic, verbTransitivity, verbActivePassive, verbType, synset, verbPastStem, verbPresentStem, nounCategory, nounPluralType, pronoun, nounNumeralType, adverbType1, adverbType2, preNounAdjectiveType, adjectiveType2, nounSpecifityType, nounType, adjectiveType1, isCausative, isIdiomatic, transitiveType, isAbbreviation, isColloquial):
        """ generated source for method __init___0 """
        self.id = id
        self.isColloquial = isColloquial
        self.isAbbreviation = isAbbreviation
        self.transitiveType = transitiveType
        self.isIdiomatic = isIdiomatic
        self.isCausative = isCausative
        self.adjectiveType1 = adjectiveType1
        self.nounType = nounType
        self.nounSpecifityType = nounSpecifityType
        self.adjectiveType2 = adjectiveType2
        self.preNounAdjectiveType = preNounAdjectiveType
        self.adverbType1 = adverbType1
        self.adverbType2 = adverbType2
        self.nounNumeralType = nounNumeralType
        self.pronoun = pronoun
        self.nounPluralType = nounPluralType
        self.nounCategory = nounCategory
        self.verbPastStem = verbPastStem
        self.verbPresentStem = verbPresentStem
        self.synset = synset
        self.verbType = verbType
        self.verbActivePassive = verbActivePassive
        self.verbTransitivity = verbTransitivity
        self.id = id
        self.seqId = seqId
        self.value = defaultValue
        self.word = Word(wordId, pos, defaultPhonetic, defaultValue)

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getSeqId(self):
        """ generated source for method getSeqId """
        return self.seqId

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def getVerbActivePassive(self):
        """ generated source for method getVerbActivePassive """
        return self.verbActivePassive

    def getVerbTransitivity(self):
        """ generated source for method getVerbTransitivity """
        return self.verbTransitivity

    def getVerbType(self):
        """ generated source for method getVerbType """
        return self.verbType

    def getVerbPresentStem(self):
        """ generated source for method getVerbPresentStem """
        return self.verbPresentStem

    def getVerbPastStem(self):
        """ generated source for method getVerbPastStem """
        return self.verbPastStem

    def getNounCategory(self):
        """ generated source for method getNounCategory """
        return self.nounCategory

    def getNounPluralType(self):
        """ generated source for method getNounPluralType """
        return self.nounPluralType

    def getPronoun(self):
        """ generated source for method getPronoun """
        return self.pronoun

    def getNounNumeralType(self):
        """ generated source for method getNounNumeralType """
        return self.nounNumeralType

    def getAdverbType1(self):
        """ generated source for method getAdverbType1 """
        return self.adverbType1

    def getAdverbType2(self):
        """ generated source for method getAdverbType2 """
        return self.adverbType2

    def getPreNounAdjectiveType(self):
        """ generated source for method getPreNounAdjectiveType """
        return self.preNounAdjectiveType

    def getAdjectiveType2(self):
        """ generated source for method getAdjectiveType2 """
        return self.adjectiveType2

    def getNounSpecifityType(self):
        """ generated source for method getNounSpecifityType """
        return self.nounSpecifityType

    def getNounType(self):
        """ generated source for method getNounType """
        return self.nounType

    def getAdjectiveType1(self):
        """ generated source for method getAdjectiveType1 """
        return self.adjectiveType1

    def getIsCausative(self):
        """ generated source for method getIsCausative """
        return self.isCausative

    def getIsIdiomatic(self):
        """ generated source for method getIsIdiomatic """
        return self.isIdiomatic

    def getTransitiveType(self):
        """ generated source for method getTransitiveType """
        return self.transitiveType

    def getIsAbbreviation(self):
        """ generated source for method getIsAbbreviation """
        return self.isAbbreviation

    def getIsColloquial(self):
        """ generated source for method getIsColloquial """
        return self.isColloquial

    def getWord(self):
        """ generated source for method getWord """
        return self.word

    def getSynset(self):
        """ generated source for method getSynset """
        if self.synset != None and not self.synset == "":
            return SynsetService.getSynsetById(Integer.parseInt(self.synset))
        return None

    @overloaded
    def getSenseRelations(self):
        """ generated source for method getSenseRelations """
        return SenseService.getSenseRelationsById(self.id)

    @getSenseRelations.register(object, SenseRelationType)
    def getSenseRelations_0(self, relationType):
        """ generated source for method getSenseRelations_0 """
        types = [None]*
        return SenseService.getSenseRelationsByType(self.id, types)

    @getSenseRelations.register(object, SenseRelationType)
    def getSenseRelations_1(self, relationTypes):
        """ generated source for method getSenseRelations_1 """
        return SenseService.getSenseRelationsByType(self.id, relationTypes)

