import farsnet
class SenseRelation(object):
    def __init__(self, id, senseId1, senseId2, senseWord1, senseWord2, type_):
        self.id = id
        self.senseId1 = senseId1
        self.senseId2 = senseId2
        self.senseWord1 = senseWord1
        self.senseWord2 = senseWord2
        self.type_ = type_

    def getSense1(self):
        return farsnet.sense_service.getSenseById(self.senseId1)

    def getSense2(self):
        return farsnet.sense_service.getSenseById(self.senseId2)