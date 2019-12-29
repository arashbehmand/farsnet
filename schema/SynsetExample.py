#!/usr/bin/env python
""" generated source for module SynsetExample """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
class SynsetExample(object):
    """ generated source for class SynsetExample """
    id = int()
    content = str()
    lexicon = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, str, str)
    def __init___0(self, id, content, lexicon):
        """ generated source for method __init___0 """
        self.id = id
        self.content = content
        self.lexicon = lexicon

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getContent(self):
        """ generated source for method getContent """
        return self.content

    def getLexicon(self):
        """ generated source for method getLexicon """
        return self.lexicon

