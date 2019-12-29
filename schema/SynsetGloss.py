class SynsetGloss(object):
    id = int()
    content = str()
    lexicon = str()

    @overloaded
    def __init__(self, id, content, lexicon):
        self.id = id
        self.content = content
        self.lexicon = lexicon

    def getId(self):
        return self.id

    def getContent(self):
        return self.content

    def getLexicon(self):
        return self.lexicon
