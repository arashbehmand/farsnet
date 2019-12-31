class WordNetSynset(object):

    def __init__(self, id, wnPos, wnOffset, example, gloss, synset, type_):
        self.id = id
        self.wnPos = wnPos
        self.wnOffset = wnOffset
        self.example = example
        self.gloss = gloss
        self.synset = synset
        self.type_ = type_