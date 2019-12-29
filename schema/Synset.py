class Synset(object):
    id = int()
    pos = str()
    semanticCategory = str()
    nofather = str()
    noMapping = str()

    @overloaded
    def __init__(self, id, pos, semanticCategory, example, gloss, nofather, noMapping
    ):
        self.id = id
        self.semanticCategory = semanticCategory
        self.nofather = nofather
        self.noMapping = noMapping
        self.pos = pos

    def getId(self):
        return self.id

    def getSemanticCategory(self):
        return self.semanticCategory

    def getNoMapping(self):
        return self.noMapping

    def getNofather(self):
        return self.nofather

    def getPos(self):
        return self.pos

    def getExamples(self):
        return SynsetService.getSynsetExamples(self.id)

    def getGlosses(self):
        return SynsetService.getSynsetGlosses(self.id)

    def getSenses(self):
        return SenseService.getSensesBySynset(self.id)

    def getWordNetSynsets(self):
        return SynsetService.getWordNetSynsets(self.id)

    @overloaded
    def getSynsetRelations(self):
        return SynsetService.getSynsetRelationsById(self.id)

    @getSynsetRelations.register(object, SynsetRelationType)
    def getSynsetRelations_0(self, relationType):
        # types = [None]*
        return SynsetService.getSynsetRelationsByType(self.id, types)

    @getSynsetRelations.register(object, SynsetRelationType)
    def getSynsetRelations_1(self, relationTypes):
        return SynsetService.getSynsetRelationsByType(self.id, relationTypes)
