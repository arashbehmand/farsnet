import farsnet.schema
from ._utils import _java_string_hashcode


class SynsetService(object):
    class __SynsetService(object):
        def __init__(self, con):
            self.con = con

        def getSynsetsByWord(self, searchStyle, searchKeyword):
            results = list()
            sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset WHERE synset.id IN (SELECT synset.id as synset_id FROM word INNER JOIN sense ON sense.word = word.id INNER JOIN synset ON sense.synset = synset.id LEFT OUTER JOIN value ON value.word = word.id WHERE word.search_value @SearchStyle '@SearchValue' OR (value.search_value) @SearchStyle '@SearchValue')  OR synset.id IN (SELECT sense.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') OR synset.id IN (SELECT sense_2.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue')"
            searchKeyword = self.SecureValue(self.NormalValue(searchKeyword))
            if searchStyle == "LIKE" or searchStyle == "START" or searchStyle == "END":
                sql = sql.replace("@SearchStyle", "LIKE")
                if searchStyle == "LIKE":
                    searchKeyword = "%" + searchKeyword + "%"
                if searchStyle == "START":
                    searchKeyword = searchKeyword + "%"
                if searchStyle == "END":
                    searchKeyword = "%" + searchKeyword
            if searchStyle == "EXACT":
                sql = sql.replace("@SearchStyle", "=")
            sql = sql.replace("@SearchValue", searchKeyword)
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.Synset(
                        row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    )
                )
            return results

        def getAllSynsets(self):
            results = list()
            sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset "
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.Synset(
                        row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    )
                )
            return results

        def getSynsetById(self, synsetId):
            sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset WHERE id=" + str(synsetId);
            result = None
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                result = farsnet.schema.Synset(
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                )
            return result

        def getSynsetRelationsById(self, synsetId):
            results = list()
            sql = (
                "SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE synset="
                + str(synsetId)
                + " OR synset2="
                + str(synsetId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.SynsetRelation(
                        row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    )
                )

            resultsArr = list()
            for res in results:
                if res.synsetId1 != synsetId:
                    type_ = res.type_
                    reverseType = res.reverseType
                    synsetId2 = res.synsetId2
                    synsetId1 = res.synsetId1
                    synsetWords2 = res.synsetWords1
                    synsetWords1 = res.synsetWords2
                    res.reverseType = type_
                    res.type_ = reverseType
                    res.synsetId1 = synsetId2
                    res.synsetId2 = synsetId1
                    res.synsetWord1 = synsetWords2
                    res.synsetWord2 = synsetWords1
                resultsArr.append(res)
            return resultsArr

        def getSynsetRelationsByType(self, synsetId, types):
            results = list()
            _types = ""
            _revTypes = ""
            for type_ in types:
                _types = str(_types) + "'" + self.RelationValue(type_) + "',"
                _revTypes = (
                    str(_revTypes)
                    + "'"
                    + self.RelationValue(self.ReverseRelationType(type_))
                    + "',"
                )
            _types = str(_types) + "'not_type'"
            _revTypes = str(_revTypes) + "'not_type'"
            sql = (
                "SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE (synset = "
                + str(synsetId)
                + " AND type in ("
                + _types
                + ")) OR (synset2 = "
                + str(synsetId)
                + " AND type in ("
                + _revTypes
                + "))"
                + " ORDER BY synset"
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.SynsetRelation(
                        row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    )
                )

            resultsArr = list()
            for res in results:
                if res.synsetId1 != synsetId:
                    type_ = res.type_
                    reverseType = res.reverseType
                    synsetId2 = res.synsetId2
                    synsetId1 = res.synsetId1
                    synsetWords2 = res.synsetWords1
                    synsetWords1 = res.synsetWords2
                    res.reverseType = type_
                    res.type_ = reverseType
                    res.synsetId1 = synsetId2
                    res.synsetId2 = synsetId1
                    res.synsetWord1 = synsetWords2
                    res.synsetWord2 = synsetWords1
                resultsArr.append(res)
            return resultsArr

        def getWordNetSynsets(self, synsetId):
            results = list()
            sql = (
                "SELECT id, wnPos, wnOffset, example, gloss, synset, type FROM wordnetsynset WHERE synset="
                + str(synsetId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.WordNetSynset(
                        row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    )
                )
            return results

        def getSynsetExamples(self, synsetId):
            results = list()
            sql = (
                "SELECT gloss_and_example.id, content, lexicon.title FROM gloss_and_example INNER JOIN lexicon ON gloss_and_example.lexicon=lexicon.id WHERE type='EXAMPLE' and synset="
                + str(synsetId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(farsnet.schema.SynsetExample(row[1], row[2], row[3]))
            return results

        def getSynsetGlosses(self, synsetId):
            results = list()
            sql = (
                "SELECT gloss_and_example.id, content, lexicon.title FROM gloss_and_example INNER JOIN lexicon ON gloss_and_example.lexicon=lexicon.id WHERE type='GLOSS' and synset="
                + str(synsetId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(farsnet.schema.SynsetGloss(row[1], row[2], row[3]))
            return results

        def NormalValue(self, Value):
            NormalValue = (
                Value.replace("\u06cc", "\u064a")
                .replace("\u0649", "\u064a")
                .replace("\u0643", "\u06a9")
                .replace("'", "")
                .replace('"', "")
                .replace(" ", "")
                .replace("\u200c", "")
                .replace("\u200c\u200c\u0621", "")
                .replace("\u200c\u200c\u0654", "")
                .replace("\u200c\u200c\u0624", "\u0648")
                .replace("\u200c\u200c\u0626", "\u064a")
                .replace("\u0622", "\u0627")
                .replace("\u200c\u200c\u0623", "\u0627")
                .replace("\u0625", "\u0627")
                .replace("\u06c0", "\u0647")
                .replace("\u0629", "\u0647")
                .replace("\u064e", "")
                .replace("\u064f", "")
                .replace("\u0650", "")
                .replace("\u064b", "")
                .replace("\u064c", "")
                .replace("\u064d", "")
                .replace("\u0651", "")
                .replace("\u0652", "")
                .replace("\u0651\u0650", "")
                .replace("\u0651\u064d", "")
                .replace("\u0651\u064e", "")
                .replace("\u0651\u064b", "")
                .replace("\u0651\u064f", "")
                .replace("\u0651\u064c", "")
                .replace("u200D", "%")
                .replace("\u0621", "")
                .replace("\u0623", "\u0627")
                .replace("\u0626", "\u064a")
            )
            return NormalValue

        def SecureValue(self, Value):
            if Value == None:
                return ""
            Value = (
                Value.replace("\u0000", "")
                .replace("'", "")
                .replace('"', "")
                .replace("\b", "")
                .replace("\n", "")
                .replace("\r", "")
                .replace("\t", "")
                .replace("\\", "")
                .replace("/", "")
                .replace("%", "")
                .replace("_", "")
                .replace("\u0640", "")
                .replace("!", "")
                .replace(";", "")
                .replace("?", "")
                .replace("=", "")
                .replace("<", "")
                .replace(">", "")
                .replace("&", "")
                .replace("#", "")
                .replace("@", "")
                .replace("$", "")
                .replace("^", "")
                .replace("*", "")
                .replace("+", "")
            )
            return Value

        def RelationValue(self, type_):
            if (
                type_ == "Related_to"
                or type_ == "Has-Unit"
                or type_[:3] == "Is_"
            ):
                return type_.replace("_", "-")
            if type_ == "Has_Salient_defining_feature":
                return "Has-Salient defining feature"
            return type_.replace("_", " ")

        def ReverseRelationType(self, type_):
            if type_ == farsnet.schema.SynsetRelationType.Agent:
                return farsnet.schema.SynsetRelationType.Is_Agent_of
            if type_ == farsnet.schema.SynsetRelationType.Is_Agent_of:
                return farsnet.schema.SynsetRelationType.Agent
            if type_ == farsnet.schema.SynsetRelationType.Hypernym:
                return farsnet.schema.SynsetRelationType.Hyponym
            if type_ == farsnet.schema.SynsetRelationType.Hyponym:
                return farsnet.schema.SynsetRelationType.Hypernym
            if type_ == farsnet.schema.SynsetRelationType.Instance_hyponym:
                return farsnet.schema.SynsetRelationType.Instance_hypernym
            if type_ == farsnet.schema.SynsetRelationType.Instance_hypernym:
                return farsnet.schema.SynsetRelationType.Instance_hyponym
            if type_ == farsnet.schema.SynsetRelationType.Part_holonym:
                return farsnet.schema.SynsetRelationType.Part_meronym
            if type_ == farsnet.schema.SynsetRelationType.Part_meronym:
                return farsnet.schema.SynsetRelationType.Part_holonym
            if type_ == farsnet.schema.SynsetRelationType.Member_holonym:
                return farsnet.schema.SynsetRelationType.Member_meronym
            if type_ == farsnet.schema.SynsetRelationType.Member_meronym:
                return farsnet.schema.SynsetRelationType.Member_holonym
            if type_ == farsnet.schema.SynsetRelationType.Substance_holonym:
                return farsnet.schema.SynsetRelationType.Substance_meronym
            if type_ == farsnet.schema.SynsetRelationType.Substance_meronym:
                return farsnet.schema.SynsetRelationType.Substance_holonym
            if type_ == farsnet.schema.SynsetRelationType.Portion_holonym:
                return farsnet.schema.SynsetRelationType.Portion_meronym
            if type_ == farsnet.schema.SynsetRelationType.Portion_meronym:
                return farsnet.schema.SynsetRelationType.Portion_holonym
            if type_ == farsnet.schema.SynsetRelationType.Domain:
                return farsnet.schema.SynsetRelationType.Is_Domain_of
            if type_ == farsnet.schema.SynsetRelationType.Is_Domain_of:
                return farsnet.schema.SynsetRelationType.Domain
            if type_ == farsnet.schema.SynsetRelationType.Cause:
                return farsnet.schema.SynsetRelationType.Is_Caused_by
            if type_ == farsnet.schema.SynsetRelationType.Is_Caused_by:
                return farsnet.schema.SynsetRelationType.Cause
            if type_ == farsnet.schema.SynsetRelationType.Is_Instrument_of:
                return farsnet.schema.SynsetRelationType.Instrument
            if type_ == farsnet.schema.SynsetRelationType.Instrument:
                return farsnet.schema.SynsetRelationType.Is_Instrument_of
            if type_ == farsnet.schema.SynsetRelationType.Is_Entailed_by:
                return farsnet.schema.SynsetRelationType.Entailment
            if type_ == farsnet.schema.SynsetRelationType.Entailment:
                return farsnet.schema.SynsetRelationType.Is_Entailed_by
            if type_ == farsnet.schema.SynsetRelationType.Location:
                return farsnet.schema.SynsetRelationType.Is_Location_of
            if type_ == farsnet.schema.SynsetRelationType.Is_Location_of:
                return farsnet.schema.SynsetRelationType.Location
            if type_ == farsnet.schema.SynsetRelationType.Has_Salient_defining_feature:
                return farsnet.schema.SynsetRelationType.Salient_defining_feature
            if type_ == farsnet.schema.SynsetRelationType.Salient_defining_feature:
                return farsnet.schema.SynsetRelationType.Has_Salient_defining_feature
            if type_ == farsnet.schema.SynsetRelationType.Is_Attribute_of:
                return farsnet.schema.SynsetRelationType.Attribute
            if type_ == farsnet.schema.SynsetRelationType.Attribute:
                return farsnet.schema.SynsetRelationType.Is_Attribute_of
            if type_ == farsnet.schema.SynsetRelationType.Unit:
                return farsnet.schema.SynsetRelationType.Has_Unit
            if type_ == farsnet.schema.SynsetRelationType.Has_Unit:
                return farsnet.schema.SynsetRelationType.Unit
            if type_ == farsnet.schema.SynsetRelationType.Is_Patient_of:
                return farsnet.schema.SynsetRelationType.Patient
            if type_ == farsnet.schema.SynsetRelationType.Patient:
                return farsnet.schema.SynsetRelationType.Is_Patient_of
            return type_

    instance = None

    def __new__(self, con):
        if not SynsetService.instance:
            SynsetService.instance = SynsetService.__SynsetService(con)

        return SynsetService.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)
