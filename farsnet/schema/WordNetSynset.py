class WordNetSynset(object):

    def __init__(self, id, wn_pos, wn_offset, example, gloss, synset, type_):
        self.id = id
        self.wn_pos = wn_pos
        self.wn_offset = wn_offset
        self.example = example
        self.gloss = gloss
        self.synset = synset
        self.type_ = type_