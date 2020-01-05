import farsnet
class Synset(object):
    def __init__(self, id, pos, semantic_category, example, gloss, nofather, no_mapping
    ):
        self.id = id
        self.semantic_category = semantic_category
        self.nofather = nofather
        self.no_mapping = no_mapping
        self.pos = pos

    def examples(self):
        return farsnet.synset_service.get_synset_examples(self.id)

    def glosses(self):
        return farsnet.synset_service.get_synset_glosses(self.id)

    def senses(self):
        return farsnet.sense_service.get_senses_by_synset(self.id)

    def wordnet_synsets(self):
        return farsnet.synset_service.get_wordnet_synsets(self.id)

    
    def synset_relations(self, relation_type = None):
        if relation_type is None:
            return farsnet.synset_service.get_synset_relations_by_id(self.id)
        elif type(relation_type)!=list:
            relation_type = [relation_type]
        return farsnet.synset_service.get_synset_relations_by_type(self.id, relation_type)
