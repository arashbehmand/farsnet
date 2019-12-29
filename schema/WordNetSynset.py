class WordNetSynset(object):
    id = int()
    wnPos = str()
    wnOffset = str()
    example = str()
    gloss = str()
    synset = int()
    type_ = str()

    def __init__(self, id, wnPos, wnOffset, example, gloss, synset, type_):
        self.id = id
        self.wnPos = wnPos
        self.wnOffset = wnOffset
        self.example = example
        self.gloss = gloss
        self.synset = synset
        self.type_ = type_

    def getId(self):
        return self.id

    def getWnPos(self):
        return self.wnPos

    def getWnOffset(self):
        return self.wnOffset

    def getExample(self):
        return self.example

    def getGloss(self):
        return self.gloss

    def getSynset(self):
        return self.synset

    def getType(self):
        return self.type_
