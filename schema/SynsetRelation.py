#!/usr/bin/env python
import farsnet.schema.Synset

import farsnet.service.SynsetService


class SynsetRelation(object):

    id = int()
    type_ = str()
    synsetWords1 = str()
    synsetWords2 = str()
    synsetId1 = int()
    synsetId2 = int()
    reverseType = str()

    def __init__(
        self, id, type_, synsetWords1, synsetWords2, synsetId1, synsetId2, reverseType
    ):
        self.id = id
        self.type_ = type_
        self.synsetWords1 = synsetWords1
        self.synsetWords2 = synsetWords2
        self.synsetId1 = synsetId1
        self.synsetId2 = synsetId2
        self.reverseType = reverseType

    def getId(self):
        return self.id

    def getType(self):
        return self.type_

    def getSynsetWords1(self):
        return self.synsetWords1

    def getSynsetWords2(self):
        return self.synsetWords2

    def getSynsetId1(self):
        return self.synsetId1

    def getSynsetId2(self):
        return self.synsetId2

    def getReverseType(self):
        return self.reverseType

    def getSynset1(self):
        return SynsetService.getSynsetById(self.synsetId1)

    def getSynset2(self):
        return SynsetService.getSynsetById(self.synsetId2)

    def setType(self, type_):
        self.type_ = type_

    def setSynsetWords1(self, synsetWords1):
        self.synsetWords1 = synsetWords1

    def setSynsetWords2(self, synsetWords2):
        self.synsetWords2 = synsetWords2

    def setSynsetId1(self, synsetId1):
        self.synsetId1 = synsetId1

    def setSynsetId2(self, synsetId2):
        self.synsetId2 = synsetId2

    def setReverseType(self, reverseType):
        self.reverseType = reverseType
