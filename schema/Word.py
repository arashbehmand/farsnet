import farsnet.schema.PhoneticForm

import farsnet.schema.WrittenForm

import farsnet.service.SenseService

import java.util.List


class Word(object):
    id = int()
    pos = str()
    defaultPhonetic = str()
    defaultValue = str()

    def __init__(self, id, pos, defaultPhonetic, defaultValue):
        self.id = id
        self.defaultPhonetic = defaultPhonetic
        self.defaultValue = defaultValue
        self.pos = pos

    def getId(self):
        return self.id

    def getPos(self):
        return self.pos

    def getDefaultPhonetic(self):
        return self.defaultPhonetic

    def getDefaultValue(self):
        return self.defaultValue

    def getWrittenForms(self):
        return SenseService.getWrittenFormsByWord(self.id)

    def getPhoneticForms(self):
        return SenseService.getPhoneticFormsByWord(self.id)
