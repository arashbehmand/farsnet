#!/usr/bin/env python
import farsnet.schema
import farsnet


class SynsetRelation(object):

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

    
    def getSynset1(self):
        return farsnet.synset_service.getSynsetById(self.synsetId1)

    def getSynset2(self):
        return farsnet.synset_service.getSynsetById(self.synsetId2)