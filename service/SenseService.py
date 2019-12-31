import sqlite3
import farsnet.schema
from ._utils import _java_string_hashcode
class SenseService(object):
    class __SenseService(object):
        def __init__(self, con):
            self.con = con
        def getSensesByWord(self, searchStyle, searchKeyword):
            results = list()
            sql = "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.id IN (SELECT sense.id FROM word INNER JOIN sense ON sense.word = word.id LEFT OUTER JOIN value ON value.word = word.id WHERE word.search_value @SearchStyle '@SearchValue' OR value.search_value @SearchStyle '@SearchValue') OR sense.id IN (SELECT sense.id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') OR sense.id IN (SELECT sense_2.id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') "
            searchKeyword = self.SecureValue(
                self.NormalValue(searchKeyword)
            )
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
                    farsnet.schema.Sense(
                        row["id"],
                        row["seqId"],
                        row["pos"],
                        row["defaultValue"],
                        row["wordId"],
                        row["avaInfo"],
                        self.getVtansivity(row["vtansivity"]),
                        self.getVactivity(row["vactivity"]),
                        self.getVtype(row["vtype"]),
                        self.getNormalValue(row["synset"]),
                        self.getNormalValue(row["vpastStem"]),
                        self.getNormalValue(row["vpresentStem"]),
                        self.getCategory(row["category"]),
                        self.getGoupOrMokassar(row["goupOrMokassar"]),
                        self.getEsmeZamir(row["esmeZamir"]),
                        self.getAdad(row["adad"]),
                        self.getAdverbType1(row["adverb_type_1"]),
                        self.getAdverbType2(row["adverb_type_2"]),
                        self.getAdjPishinVijegi(
                            row["adj_pishin_vijegi"]
                        ),
                        self.getAdjType(row["adj_type"]),
                        self.getNoeKhas(row["noe_khas"]),
                        self.getNounType(row["nounType"]),
                        self.getAdjTypeSademorakkab(
                            row["adj_type_sademorakkab"]
                        ),
                        row["vIssababi"],
                        row["vIsIdiom"],
                        self.getVGozaraType(row["vGozaraType"]),
                        row["kootah_nevesht"],
                        row["mohavere"],
                    )
                )
            return results

        def getSensesBySynset(self, synsetId):
            results = list()
            sql = (
                "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.synset = "
                + str(synsetId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.Sense(
                        row["id"],
                        row["seqId"],
                        row["pos"],
                        row["defaultValue"],
                        row["wordId"],
                        row["avaInfo"],
                        self.getVtansivity(row["vtansivity"]),
                        self.getVactivity(row["vactivity"]),
                        self.getVtype(row["vtype"]),
                        self.getNormalValue(row["synset"]),
                        self.getNormalValue(row["vpastStem"]),
                        self.getNormalValue(row["vpresentStem"]),
                        self.getCategory(row["category"]),
                        self.getGoupOrMokassar(row["goupOrMokassar"]),
                        self.getEsmeZamir(row["esmeZamir"]),
                        self.getAdad(row["adad"]),
                        self.getAdverbType1(row["adverb_type_1"]),
                        self.getAdverbType2(row["adverb_type_2"]),
                        self.getAdjPishinVijegi(
                            row["adj_pishin_vijegi"]
                        ),
                        self.getAdjType(row["adj_type"]),
                        self.getNoeKhas(row["noe_khas"]),
                        self.getNounType(row["nounType"]),
                        self.getAdjTypeSademorakkab(
                            row["adj_type_sademorakkab"]
                        ),
                        row["vIssababi"],
                        row["vIsIdiom"],
                        self.getVGozaraType(row["vGozaraType"]),
                        row["kootah_nevesht"],
                        row["mohavere"],
                    )
                )
            return results

        def getSenseById(self, senseId):
            result = None
            sql = (
                "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.id = "
                + str(senseId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                result = farsnet.schema.Sense(
                    row["id"],
                    row["seqId"],
                    row["pos"],
                    row["defaultValue"],
                    row["wordId"],
                    row["avaInfo"],
                    self.getVtansivity(row["vtansivity"]),
                    self.getVactivity(row["vactivity"]),
                    self.getVtype(row["vtype"]),
                    self.getNormalValue(row["synset"]),
                    self.getNormalValue(row["vpastStem"]),
                    self.getNormalValue(row["vpresentStem"]),
                    self.getCategory(row["category"]),
                    self.getGoupOrMokassar(row["goupOrMokassar"]),
                    self.getEsmeZamir(row["esmeZamir"]),
                    self.getAdad(row["adad"]),
                    self.getAdverbType1(row["adverb_type_1"]),
                    self.getAdverbType2(row["adverb_type_2"]),
                    self.getAdjPishinVijegi(row["adj_pishin_vijegi"]),
                    self.getAdjType(row["adj_type"]),
                    self.getNoeKhas(row["noe_khas"]),
                    self.getNounType(row["nounType"]),
                    self.getAdjTypeSademorakkab(
                        row["adj_type_sademorakkab"]
                    ),
                    row["vIssababi"],
                    row["vIsIdiom"],
                    self.getVGozaraType(row["vGozaraType"]),
                    row["kootah_nevesht"],
                    row["mohavere"],
                )
            return result

        def getAllSenses(self):
            results = list()
            sql = "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id"
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.Sense(
                        row["id"],
                        row["seqId"],
                        row["pos"],
                        row["defaultValue"],
                        row["wordId"],
                        row["avaInfo"],
                        self.getVtansivity(row["vtansivity"]),
                        self.getVactivity(row["vactivity"]),
                        self.getVtype(row["vtype"]),
                        self.getNormalValue(row["synset"]),
                        self.getNormalValue(row["vpastStem"]),
                        self.getNormalValue(row["vpresentStem"]),
                        self.getCategory(row["category"]),
                        self.getGoupOrMokassar(row["goupOrMokassar"]),
                        self.getEsmeZamir(row["esmeZamir"]),
                        self.getAdad(row["adad"]),
                        self.getAdverbType1(row["adverb_type_1"]),
                        self.getAdverbType2(row["adverb_type_2"]),
                        self.getAdjPishinVijegi(
                            row["adj_pishin_vijegi"]
                        ),
                        self.getAdjType(row["adj_type"]),
                        self.getNoeKhas(row["noe_khas"]),
                        self.getNounType(row["nounType"]),
                        self.getAdjTypeSademorakkab(
                            row["adj_type_sademorakkab"]
                        ),
                        row["vIssababi"],
                        row["vIsIdiom"],
                        self.getVGozaraType(row["vGozaraType"]),
                        row["kootah_nevesht"],
                        row["mohavere"],
                    )
                )
            return results

        def getSenseRelationsById(self, senseId):
            results = list()
            sql = (
                "SELECT id, type, sense, sense2, senseWord1, senseWord2 FROM sense_relation WHERE sense = "
                + str(senseId)
                + " OR sense2 = "
                + str(senseId)
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.SenseRelation(
                        row["id"],
                        row["sense"],
                        row["sense2"],
                        row["senseWord1"],
                        row["senseWord2"],
                        row["type"],
                    )
                )

            resultsArr = list()
            for res in results:
                if res.senseId1 != senseId:
                    type_ = res.type_
                    senseId2 = res.senseId2
                    senseId1 = res.senseId1
                    senseWord2 = res.senseWord1
                    senseWord1 = res.senseWord2
                    res.type = self.ReverseSRelationType(type_)
                    res.senseId1 = senseId2
                    res.senseId2 = senseId1
                    res.senseWord1 = senseWord2
                    res.senseWord2 = senseWord1
                resultsArr.append(res)
            return resultsArr

        def getSenseRelationsByType(self, senseId, types):
            results = list()
            _types = ""
            _revTypes = ""
            for type_ in types:
                _types = (
                    str(_types) + "'" + self.RelationValue(type_) + "',"
                )
                _revTypes = (
                    str(_revTypes)
                    + "'"
                    + self.RelationValue(self.ReverseRelationType(type_))
                    + "',"
                )
            _types = str(_types) + "'not_type'"
            _revTypes = str(_revTypes) + "'not_type'"
            sql = (
                "SELECT id, type, sense, sense2, senseWord1, senseWord2 FROM sense_relation WHERE (sense = "
                + senseId
                + " AND type in ("
                + _types
                + ")) OR (sense2 = "
                + senseId
                + " AND type in ("
                + _revTypes
                + "))"
                + " ORDER BY sense"
            )
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(
                    farsnet.schema.SenseRelation(
                        row["id"],
                        row["sense"],
                        row["sense2"],
                        row["senseWord1"],
                        row["senseWord2"],
                        row["type"],
                    )
                )


            resultsArr = list()
            for res in results:
                if res.senseId1 != senseId:
                    type_ = res.type_
                    senseId2 = res.senseId2
                    senseId1 = res.senseId1
                    senseWord2 = res.senseWord1
                    senseWord1 = res.senseWord2
                    res.type = self.ReverseSRelationType(type_)
                    res.senseId1 = senseId2
                    res.senseId2 = senseId1
                    res.senseWord1 = senseWord2
                    res.senseWord2 = senseWord1
                resultsArr.append(res)
            return resultsArr

        def getPhoneticFormsByWord(self, wordId):
            results = list()
            sql = "SELECT id, value FROM speech WHERE word = " + str(wordId)
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(farsnet.schema.PhoneticForm(row["id"], row["value"]))
            return results

        def getWrittenFormsByWord(self, wordId):
            results = list()
            sql = "SELECT id, value FROM value WHERE word = " + str(wordId)
            cur = self.con.cursor()
            cur.execute(sql)
            for row in cur:
                results.append(farsnet.schema.WrittenForm(row["id"], row["value"]))
            return results

        def NormalValue(self, Value):
            NormalValue = Value.replace("\u06cc", "\u064a").\
                                replace("\u0649", "\u064a").\
                                replace("\u0643", "\u06a9").\
                                replace("'", "").\
                                replace('"', "").\
                                replace(" ", "").\
                                replace("\u200c", "").\
                                replace("\u200c\u200c\u0621", "").\
                                replace("\u200c\u200c\u0654", "").\
                                replace("\u200c\u200c\u0624", "\u0648").\
                                replace("\u200c\u200c\u0626", "\u064a").\
                                replace("\u0622", "\u0627").\
                                replace("\u200c\u200c\u0623", "\u0627").\
                                replace("\u0625", "\u0627").\
                                replace("\u06c0", "\u0647").\
                                replace("\u0629", "\u0647").\
                                replace("\u064e", "").\
                                replace("\u064f", "").\
                                replace("\u0650", "").\
                                replace("\u064b", "").\
                                replace("\u064c", "").\
                                replace("\u064d", "").\
                                replace("\u0651", "").\
                                replace("\u0652", "").\
                                replace("\u0651\u0650", "").\
                                replace("\u0651\u064d", "").\
                                replace("\u0651\u064e", "").\
                                replace("\u0651\u064b", "").\
                                replace("\u0651\u064f", "").\
                                replace("\u0651\u064c", "").\
                                replace("u200D", "%").\
                                replace("\u0621", "").\
                                replace("\u0623", "\u0627").\
                                replace("\u0626", "\u064a")
            return NormalValue

        def SecureValue(self, Value):
            if Value == None:
                return ""
            Value = Value.replace("\u0000", "").\
                          replace("'", "").\
                          replace('"', "").\
                          replace("\b", "").\
                          replace("\n", "").\
                          replace("\r", "").\
                          replace("\t", "").\
                          replace("\\", "").\
                          replace("/", "").\
                          replace("%", "").\
                          replace("_", "").\
                          replace("\u0640", "").\
                          replace("!", "").\
                          replace(";", "").\
                          replace("?", "").\
                          replace("=", "").\
                          replace("<", "").\
                          replace(">", "").\
                          replace("&", "").\
                          replace("#", "").\
                          replace("@", "").\
                          replace("$", "").\
                          replace("^", "").\
                          replace("*", "").\
                          replace("+", "")
            return Value

        def getVtansivity(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -1724158427:
                if string == "transitive":
                    return "Transitive"
                return value
            elif _java_string_hashcode(string) == 841936170:
                if string == "inTransitive":
                    return "Intransitive"
                return value
            elif _java_string_hashcode(string) == 1845861045:
                if not string == "dovajhi":
                    return value
                return "Causative/Anticausative"
            return value

        def getVactivity(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -1422950650:
                if string == "active":
                    return "Active"
                return value
            elif _java_string_hashcode(string) == -792039641:
                if string == "passive":
                    return "Passive"
                return value
            return value

        def getVtype(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -1431524879:
                if string == "simpleVerb":
                    return "Simple"
                return value
            elif _java_string_hashcode(string) == -1054772775:
                if string == "pishvandiVerb":
                    return "Phrasal"
                return value
            elif _java_string_hashcode(string) == -570810619:
                if string == "auxiliaryVerb":
                    return "Auxiliary"
                return value
            elif _java_string_hashcode(string) == 530219749:
                if string == "copulaVerb":
                    return "Copula"
                return value
            elif _java_string_hashcode(string) == 1665965418:
                if string == "compoundVerb":
                    return "Complex"
                return value
            return value

        def getCategory(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -49458414:
                if string == "category_masdari":
                    return "Infinitival"
                return value
            elif _java_string_hashcode(string) == 318357937:
                if string == "category_esmZamir":
                    return "Pronoun"
                return value
            elif _java_string_hashcode(string) == 338298407:
                if string == "category_adad":
                    return "Numeral"
                return value
            elif _java_string_hashcode(string) == 338599184:
                if string == "category_khAs":
                    return "Specific"
                return value
            elif _java_string_hashcode(string) == 1537779501:
                if string == "category_Am":
                    return "General"
                return value
            return value

        def getGoupOrMokassar(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -826418989:
                if string == "am_khas_esmejam":
                    return "MassNoun"
                return value
            elif _java_string_hashcode(string) == 134174425:
                if string == "am_khas_jam":
                    return "Regular"
                return value
            elif _java_string_hashcode(string) == 1892681254:
                if string == "am_khas_mokassar":
                    return "Irregular"
                return value
            return value

        def getEsmeZamir(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -969140441:
                if string == "gheir_moshakhas":
                    return "Indefinite"
                return value
            elif _java_string_hashcode(string) == 534797624:
                if string == "motaghabel":
                    return "Reciprocal"
                return value
            elif _java_string_hashcode(string) == 714990811:
                if string == "noun_type_morakab":
                    return ""
                return value
            elif _java_string_hashcode(string) == 1224364290:
                if not string == "moakkad":
                    return value
                return "Emphatic"
            return value

        def getAdad(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -1537886559:
                if string == "tartibi":
                    return "Ordinal"
                return value
            elif _java_string_hashcode(string) == 3003695:
                if not string == "asli":
                    return value
                return "Cardinal"
            return value

        def getAdverbType1(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            string = value
            if _java_string_hashcode(string) == -1609563487:
                if string == "moshtagh_morakab":
                    return "DerivationalCompound"
                return value
            elif _java_string_hashcode(string) == -221942702:
                if string == "morakkab":
                    return "Compound"
                return value
            elif _java_string_hashcode(string) == -186590203:
                if string == "moshtagh":
                    return "Derivative"
                return value
            elif _java_string_hashcode(string) == 109191060:
                if string == "saade":
                    return "Simple"
                return value
            return value

        def getNormalValue(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            return value

        def getAdverbType2(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            res = " "
            if value[0] == "1":
                res += "AdjectiveModifying,"
            elif value[0] == "0":
                res = str(res)
            else:
                res += value[0] + ","
            if value[1] == "1":
                res += "AdverbModifying,"
            elif value[1] == "0":
                res = str(res)
            else:
                res += value[1] + ","
            if value[2] == "1":
                res += "VerbModifying,"
            elif value[2] == "0":
                res = str(res)
            else:
                res += value[2] + ","
            if value[3] == "1":
                res += "SentenceModifying,"
            elif value[3] == "0":
                res = str(res)
            else:
                res += value[3] + ","
            return res[:-1]

        def getAdjPishinVijegi(self, value):
            if value == None or value == "" or value == "Nothing" or value == "No":
                return ""
            string = value
            if _java_string_hashcode(string) == -282395544:
                if string == "Yes_taajobi":
                    return "Exclamatory"
                return value
            elif _java_string_hashcode(string) == 770492981:
                if string == "Yes_Nothing":
                    return "Simple"
                return value
            elif _java_string_hashcode(string) == 1795033874:
                if string == "Yes_eshare":
                    return "Demonstrative"
                return value
            elif _java_string_hashcode(string) == 2020200460:
                if not string == "Yes_mobham":
                    return value
                return "Indefinite"
            return value

        def getAdjType(self, value):
            if value == None or value == "" or value == "Nothing" or value == "No":
                return ""
            string = value
            if _java_string_hashcode(string) == -1735880873:
                if string == "bartarin":
                    return "Superlative"
                return value
            elif _java_string_hashcode(string) == -1396218190:
                if string == "bartar":
                    return "Comparative"
                return value
            elif _java_string_hashcode(string) == 1241931560:
                if string == "motlagh":
                    return "Absolute"
                return value
            return value

        def getNoeKhas(self, value):
            if value == None or value == "" or value == "Nothing" or value == "No":
                return ""
            string = value
            if _java_string_hashcode(string) == -533828350:
                if string == "noe_khas_ensan":
                    return "Human"
                return value
            elif _java_string_hashcode(string) == -526835153:
                if string == "noe_khas_makan":
                    return "Place"
                return value
            elif _java_string_hashcode(string) == -514827458:
                if string == "noe_khas_zaman":
                    return "Time"
                return value
            elif _java_string_hashcode(string) == 708964732:
                if string == "noe_khas_heyvan":
                    return "Animal"
                return value
            return value

        def getAdjTypeSademorakkab(self, value):
            if value == None or value == "" or value == "Nothing" or value == "No":
                return ""
            string = value
            if _java_string_hashcode(string) == -1398986386:
                if string == "adj_type_morakab":
                    return "Compound"
                return value
            elif _java_string_hashcode(string) == -383542830:
                if string == "adj_type_moshtagh":
                    return "Derivative"
                return value
            elif _java_string_hashcode(string) == -264504089:
                if string == "adj_type_saade":
                    return "Simple"
                return value
            elif _java_string_hashcode(string) == 1930601326:
                if string == "adj_type_moshtagh_morakab":
                    return "DerivatinalCompound"
                return value
            return value

        def getVGozaraType(self, value):
            if value == None or value == "" or value == "Nothing":
                return ""
            res = " "
            if value[0] == "1":
                res += "WithComplement,"
            elif value[0] != "0":
                res += value[0] + ","
            if value[1] == "1":
                res += "WithObject,"
            elif value[1] != "0":
                res += value[1] + ","
            if value[2] == "1":
                res += "WithPredicate,"
            elif value[2] != "0":
                res += value[2] + ","
            return res[:-1]

        def getNounType(self, value):
            if value == None or value == "" or value == "Nothing" or value == "No":
                return ""
            string = value
            if _java_string_hashcode(string) == -1881033151:
                if string == "noun_type_ebarat":
                    return "Phrasal"
                return value
            elif _java_string_hashcode(string) == -601968748:
                if string == "noun_type_saade":
                    return "Simple"
                return value
            elif _java_string_hashcode(string) == 714990811:
                if string == "noun_type_morakab":
                    return "Compound"
                return value
            elif _java_string_hashcode(string) == 725240837:
                if string == "noun_type_moshtagh":
                    return "Derivative"
                return value
            elif _java_string_hashcode(string) == 1576628897:
                if string == "noun_type_moshtagh_morakab":
                    return "DerivatinalCompound"
                return value
            return value

        def RelationValue(self, type_):
            if type_ == "Derivationally_related_form":
                return "Derivationally related form"
            return type_.replace("_", "-")

        def ReverseRelationType(self, type_):
            if type_ == farsnet.schema.SenseRelationType.Refer_to:
                return farsnet.schema.SenseRelationType.Is_Referred_by
            if type_ == farsnet.schema.SenseRelationType.Is_Referred_by:
                return farsnet.schema.SenseRelationType.Refer_to
            if type_ == farsnet.schema.SenseRelationType.Verbal_Part:
                return farsnet.schema.SenseRelationType.Is_Verbal_Part_of
            if type_ == farsnet.schema.SenseRelationType.Is_Verbal_Part_of:
                return farsnet.schema.SenseRelationType.Verbal_Part
            if type_ == farsnet.schema.SenseRelationType.Is_Non_Verbal_Part_of:
                return farsnet.schema.SenseRelationType.Non_Verbal_Part
            if type_ == farsnet.schema.SenseRelationType.Non_Verbal_Part:
                return farsnet.schema.SenseRelationType.Is_Non_Verbal_Part_of
            return type_

        def ReverseSRelationType(self, type_):
            if type_ == "Refer-to":
                return "Is-Referred-by"
            if type_ == "Is-Referred-by":
                return "Refer-to"
            if type_ == "Verbal-Part":
                return "Is-Verbal-Part-of"
            if type_ == "Is-Verbal-Part-of":
                return "Verbal-Part"
            if type_ == "Non-Verbal-Part":
                return "Is-Non-Verbal-Part-of"
            if type_ == "Is-Non-Verbal-Part-of":
                return "Non-Verbal-Part"
            return type_

    instance = None
    def __new__(self, con):
        if not self.instance:
            self.instance = self.__SenseService(con)

        return self.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)