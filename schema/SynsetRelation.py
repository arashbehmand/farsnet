#!/usr/bin/env python
import farsnet.schema
import farsnet


class SynsetRelation(object):

    def __init__(
        self, id, type_, synset_words1, synset_words2, synset_id1, synset_id2, reverse_type
    ):
        self.id = id
        self.type_ = type_
        self.synset_words1 = synset_words1
        self.synset_words2 = synset_words2
        self.synset_id1 = synset_id1
        self.synset_id2 = synset_id2
        self.reverse_type = reverse_type

    
    def synset1(self):
        return farsnet.synset_service.get_synset_by_id(self.synset_id1)

    def synset2(self):
        return farsnet.synset_service.get_synset_by_id(self.synset_id2)