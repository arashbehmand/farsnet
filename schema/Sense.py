import farsnet
import farsnet.schema

class Sense(object):

    def __init__(self,
        id,
        seqId,
        pos,
        defaultValue,
        wordId,
        defaultPhonetic,
        verbTransitivity,
        verbActivePassive,
        verbType,
        synset,
        verbPastStem,
        verbPresentStem,
        nounCategory,
        nounPluralType,
        pronoun,
        nounNumeralType,
        adverbType1,
        adverbType2,
        preNounAdjectiveType,
        adjectiveType2,
        nounSpecifityType,
        nounType,
        adjectiveType1,
        isCausative,
        isIdiomatic,
        transitiveType,
        isAbbreviation,
        isColloquial,
    ):
        self.id = id
        self.isColloquial = isColloquial
        self.isAbbreviation = isAbbreviation
        self.transitiveType = transitiveType
        self.isIdiomatic = isIdiomatic
        self.isCausative = isCausative
        self.adjectiveType1 = adjectiveType1
        self.nounType = nounType
        self.nounSpecifityType = nounSpecifityType
        self.adjectiveType2 = adjectiveType2
        self.preNounAdjectiveType = preNounAdjectiveType
        self.adverbType1 = adverbType1
        self.adverbType2 = adverbType2
        self.nounNumeralType = nounNumeralType
        self.pronoun = pronoun
        self.nounPluralType = nounPluralType
        self.nounCategory = nounCategory
        self.verbPastStem = verbPastStem
        self.verbPresentStem = verbPresentStem
        self.synset = synset
        self.verbType = verbType
        self.verbActivePassive = verbActivePassive
        self.verbTransitivity = verbTransitivity
        self.id = id
        self.seqId = seqId
        self.value = defaultValue
        self.word = farsnet.schema.Word(wordId, pos, defaultPhonetic, defaultValue)

    
    def getSynset(self):
        if self.synset != None and not self.synset == "":
            return farsnet.synset_service.getSynsetById(int(self.synset))
        return None

    def getSenseRelations(self, relationType = None):
        if relationType is None:
            return farsnet.sense_service.getSenseRelationsById(self.id)
        else:
            return farsnet.sense_service.getSenseRelationsByType(self.id, relationType)
        
