#!/usr/bin/env python
""" generated source for module Word """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
import farsnet.schema.PhoneticForm

import farsnet.schema.WrittenForm

import farsnet.service.SenseService

import java.util.List

class Word(object):
    """ generated source for class Word """
    id = int()
    pos = str()
    defaultPhonetic = str()
    defaultValue = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, str, str, str)
    def __init___0(self, id, pos, defaultPhonetic, defaultValue):
        """ generated source for method __init___0 """
        self.id = id
        self.defaultPhonetic = defaultPhonetic
        self.defaultValue = defaultValue
        self.pos = pos

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getPos(self):
        """ generated source for method getPos """
        return self.pos

    def getDefaultPhonetic(self):
        """ generated source for method getDefaultPhonetic """
        return self.defaultPhonetic

    def getDefaultValue(self):
        """ generated source for method getDefaultValue """
        return self.defaultValue

    def getWrittenForms(self):
        """ generated source for method getWrittenForms """
        return SenseService.getWrittenFormsByWord(self.id)

    def getPhoneticForms(self):
        """ generated source for method getPhoneticForms """
        return SenseService.getPhoneticFormsByWord(self.id)

