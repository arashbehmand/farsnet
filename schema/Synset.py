import farsnet
class Synset(object):
    id = int()
    pos = str()
    semanticCategory = str()
    nofather = str()
    noMapping = str()

    
    def __init__(self, id, pos, semanticCategory, example, gloss, nofather, noMapping
    ):
        self.id = id
        self.semanticCategory = semanticCategory
        self.nofather = nofather
        self.noMapping = noMapping
        self.pos = pos

    def getExamples(self):
        return farsnet.synset_service.getSynsetExamples(self.id)

    def getGlosses(self):
        return farsnet.synset_service.getSynsetGlosses(self.id)

    def getSenses(self):
        return farsnet.sense_service.getSensesBySynset(self.id)

    def getWordNetSynsets(self):
        return farsnet.synset_service.getWordNetSynsets(self.id)

    
    def getSynsetRelations(self, relationType = None):
        if relationType is None:
            return farsnet.synset_service.getSynsetRelationsById(self.id)
        else:
            return farsnet.synset_service.getSynsetRelationsByType(self.id, relationType)
