#!/usr/bin/env python
""" generated source for module PhoneticForm """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.schema
class PhoneticForm(object):
    """ generated source for class PhoneticForm """
    id = int()
    value = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int, str)
    def __init___0(self, id, value):
        """ generated source for method __init___0 """
        self.id = id
        self.value = value

    def getId(self):
        """ generated source for method getId """
        return self.id

    def getValue(self):
        """ generated source for method getValue """
        return self.value

