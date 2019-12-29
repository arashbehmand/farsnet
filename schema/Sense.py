class Sense(object):
    """ generated source for class Sense """

    id = int()
    seqId = str()
    value = str()
    word = Word()
    verbTransitivity = str()
    verbActivePassive = str()
    verbType = str()
    synset = str()
    verbPastStem = str()
    verbPresentStem = str()
    nounCategory = str()
    nounPluralType = str()
    pronoun = str()
    nounNumeralType = str()
    adverbType1 = str()
    adverbType2 = str()
    preNounAdjectiveType = str()
    adjectiveType2 = str()
    nounSpecifityType = str()
    nounType = str()
    adjectiveType1 = str()
    isCausative = bool()
    isIdiomatic = bool()
    transitiveType = str()
    isAbbreviation = bool()
    isColloquial = bool()

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
        self.word = Word(wordId, pos, defaultPhonetic, defaultValue)

    def getId(self):
        return self.id

    def getSeqId(self):
        return self.seqId

    def getValue(self):
        return self.value

    def getVerbActivePassive(self):
        return self.verbActivePassive

    def getVerbTransitivity(self):
        return self.verbTransitivity

    def getVerbType(self):
        return self.verbType

    def getVerbPresentStem(self):
        return self.verbPresentStem

    def getVerbPastStem(self):
        return self.verbPastStem

    def getNounCategory(self):
        return self.nounCategory

    def getNounPluralType(self):
        return self.nounPluralType

    def getPronoun(self):
        return self.pronoun

    def getNounNumeralType(self):
        return self.nounNumeralType

    def getAdverbType1(self):
        return self.adverbType1

    def getAdverbType2(self):
        return self.adverbType2

    def getPreNounAdjectiveType(self):
        return self.preNounAdjectiveType

    def getAdjectiveType2(self):
        return self.adjectiveType2

    def getNounSpecifityType(self):
        return self.nounSpecifityType

    def getNounType(self):
        return self.nounType

    def getAdjectiveType1(self):
        return self.adjectiveType1

    def getIsCausative(self):
        return self.isCausative

    def getIsIdiomatic(self):
        return self.isIdiomatic

    def getTransitiveType(self):
        return self.transitiveType

    def getIsAbbreviation(self):
        return self.isAbbreviation

    def getIsColloquial(self):
        return self.isColloquial

    def getWord(self):
        return self.word

    def getSynset(self):
        if self.synset != None and not self.synset == "":
            return SynsetService.getSynsetById(Integer.parseInt(self.synset))
        return None

    @overloaded
    def getSenseRelations(self):
        return SenseService.getSenseRelationsById(self.id)

    @getSenseRelations.register(object, SenseRelationType)
    def getSenseRelations_0(self, relationType):
        # types = [None]*
        return SenseService.getSenseRelationsByType(self.id, types)

    @getSenseRelations.register(object, SenseRelationType)
    def getSenseRelations_1(self, relationTypes):
        return SenseService.getSenseRelationsByType(self.id, relationTypes)
