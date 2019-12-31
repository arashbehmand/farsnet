import farsnet.schema

import farsnet


class Word(object):

    def __init__(self, id, pos, defaultPhonetic, defaultValue):
        self.id = id
        self.defaultPhonetic = defaultPhonetic
        self.defaultValue = defaultValue
        self.pos = pos

    def getWrittenForms(self):
        return farsnet.sense_service.getWrittenFormsByWord(self.id)

    def getPhoneticForms(self):
        return farsnet.sense_service.getPhoneticFormsByWord(self.id)
