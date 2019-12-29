import farsnet.database.SqlLiteDbUtility
import farsnet.schema.PhoneticForm
import farsnet.schema.Sense
import farsnet.schema.SenseRelation
import farsnet.schema.SenseRelationType
import farsnet.schema.WrittenForm


class SenseService(object):
    @classmethod
    def getSensesByWord(cls, searchStyle, searchKeyword):
        results = ArrayList()
        sql = "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.id IN (SELECT sense.id FROM word INNER JOIN sense ON sense.word = word.id LEFT OUTER JOIN value ON value.word = word.id WHERE word.search_value @SearchStyle '@SearchValue' OR value.search_value @SearchStyle '@SearchValue') OR sense.id IN (SELECT sense.id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') OR sense.id IN (SELECT sense_2.id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') "
        searchKeyword = SenseService.SecureValue(
            SenseService.NormalValue(searchKeyword)
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
        try:
            while rs.next():
                results.add(
                    Sense(
                        rs.getInt("id"),
                        rs.getString("seqId"),
                        rs.getString("pos"),
                        rs.getString("defaultValue"),
                        rs.getInt("wordId"),
                        rs.getString("avaInfo"),
                        SenseService.getVtansivity(rs.getString("vtansivity")),
                        SenseService.getVactivity(rs.getString("vactivity")),
                        SenseService.getVtype(rs.getString("vtype")),
                        SenseService.getNormalValue(rs.getString("synset")),
                        SenseService.getNormalValue(rs.getString("vpastStem")),
                        SenseService.getNormalValue(rs.getString("vpresentStem")),
                        SenseService.getCategory(rs.getString("category")),
                        SenseService.getGoupOrMokassar(rs.getString("goupOrMokassar")),
                        SenseService.getEsmeZamir(rs.getString("esmeZamir")),
                        SenseService.getAdad(rs.getString("adad")),
                        SenseService.getAdverbType1(rs.getString("adverb_type_1")),
                        SenseService.getAdverbType2(rs.getString("adverb_type_2")),
                        SenseService.getAdjPishinVijegi(
                            rs.getString("adj_pishin_vijegi")
                        ),
                        SenseService.getAdjType(rs.getString("adj_type")),
                        SenseService.getNoeKhas(rs.getString("noe_khas")),
                        SenseService.getNounType(rs.getString("nounType")),
                        SenseService.getAdjTypeSademorakkab(
                            rs.getString("adj_type_sademorakkab")
                        ),
                        rs.getBoolean("vIssababi"),
                        rs.getBoolean("vIsIdiom"),
                        SenseService.getVGozaraType(rs.getString("vGozaraType")),
                        rs.getBoolean("kootah_nevesht"),
                        rs.getBoolean("mohavere"),
                    )
                )
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getSensesBySynset(cls, synsetId):
        results = ArrayList()
        sql = (
            "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.synset = "
            + synsetId
        )
        try:
            while rs.next():
                results.add(
                    Sense(
                        rs.getInt("id"),
                        rs.getString("seqId"),
                        rs.getString("pos"),
                        rs.getString("defaultValue"),
                        rs.getInt("wordId"),
                        rs.getString("avaInfo"),
                        SenseService.getVtansivity(rs.getString("vtansivity")),
                        SenseService.getVactivity(rs.getString("vactivity")),
                        SenseService.getVtype(rs.getString("vtype")),
                        SenseService.getNormalValue(rs.getString("synset")),
                        SenseService.getNormalValue(rs.getString("vpastStem")),
                        SenseService.getNormalValue(rs.getString("vpresentStem")),
                        SenseService.getCategory(rs.getString("category")),
                        SenseService.getGoupOrMokassar(rs.getString("goupOrMokassar")),
                        SenseService.getEsmeZamir(rs.getString("esmeZamir")),
                        SenseService.getAdad(rs.getString("adad")),
                        SenseService.getAdverbType1(rs.getString("adverb_type_1")),
                        SenseService.getAdverbType2(rs.getString("adverb_type_2")),
                        SenseService.getAdjPishinVijegi(
                            rs.getString("adj_pishin_vijegi")
                        ),
                        SenseService.getAdjType(rs.getString("adj_type")),
                        SenseService.getNoeKhas(rs.getString("noe_khas")),
                        SenseService.getNounType(rs.getString("nounType")),
                        SenseService.getAdjTypeSademorakkab(
                            rs.getString("adj_type_sademorakkab")
                        ),
                        rs.getBoolean("vIssababi"),
                        rs.getBoolean("vIsIdiom"),
                        SenseService.getVGozaraType(rs.getString("vGozaraType")),
                        rs.getBoolean("kootah_nevesht"),
                        rs.getBoolean("mohavere"),
                    )
                )
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getSenseById(cls, senseId):
        result = None
        sql = (
            "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.id = "
            + senseId
        )
        try:
            while rs.next():
                result = Sense(
                    rs.getInt("id"),
                    rs.getString("seqId"),
                    rs.getString("pos"),
                    rs.getString("defaultValue"),
                    rs.getInt("wordId"),
                    rs.getString("avaInfo"),
                    SenseService.getVtansivity(rs.getString("vtansivity")),
                    SenseService.getVactivity(rs.getString("vactivity")),
                    SenseService.getVtype(rs.getString("vtype")),
                    SenseService.getNormalValue(rs.getString("synset")),
                    SenseService.getNormalValue(rs.getString("vpastStem")),
                    SenseService.getNormalValue(rs.getString("vpresentStem")),
                    SenseService.getCategory(rs.getString("category")),
                    SenseService.getGoupOrMokassar(rs.getString("goupOrMokassar")),
                    SenseService.getEsmeZamir(rs.getString("esmeZamir")),
                    SenseService.getAdad(rs.getString("adad")),
                    SenseService.getAdverbType1(rs.getString("adverb_type_1")),
                    SenseService.getAdverbType2(rs.getString("adverb_type_2")),
                    SenseService.getAdjPishinVijegi(rs.getString("adj_pishin_vijegi")),
                    SenseService.getAdjType(rs.getString("adj_type")),
                    SenseService.getNoeKhas(rs.getString("noe_khas")),
                    SenseService.getNounType(rs.getString("nounType")),
                    SenseService.getAdjTypeSademorakkab(
                        rs.getString("adj_type_sademorakkab")
                    ),
                    rs.getBoolean("vIssababi"),
                    rs.getBoolean("vIsIdiom"),
                    SenseService.getVGozaraType(rs.getString("vGozaraType")),
                    rs.getBoolean("kootah_nevesht"),
                    rs.getBoolean("mohavere"),
                )
        except SQLException as e:
            e.printStackTrace()
        return result

    @classmethod
    def getAllSenses(cls):
        results = ArrayList()
        sql = "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id"
        try:
            while rs.next():
                results.add(
                    Sense(
                        rs.getInt("id"),
                        rs.getString("seqId"),
                        rs.getString("pos"),
                        rs.getString("defaultValue"),
                        rs.getInt("wordId"),
                        rs.getString("avaInfo"),
                        SenseService.getVtansivity(rs.getString("vtansivity")),
                        SenseService.getVactivity(rs.getString("vactivity")),
                        SenseService.getVtype(rs.getString("vtype")),
                        SenseService.getNormalValue(rs.getString("synset")),
                        SenseService.getNormalValue(rs.getString("vpastStem")),
                        SenseService.getNormalValue(rs.getString("vpresentStem")),
                        SenseService.getCategory(rs.getString("category")),
                        SenseService.getGoupOrMokassar(rs.getString("goupOrMokassar")),
                        SenseService.getEsmeZamir(rs.getString("esmeZamir")),
                        SenseService.getAdad(rs.getString("adad")),
                        SenseService.getAdverbType1(rs.getString("adverb_type_1")),
                        SenseService.getAdverbType2(rs.getString("adverb_type_2")),
                        SenseService.getAdjPishinVijegi(
                            rs.getString("adj_pishin_vijegi")
                        ),
                        SenseService.getAdjType(rs.getString("adj_type")),
                        SenseService.getNoeKhas(rs.getString("noe_khas")),
                        SenseService.getNounType(rs.getString("nounType")),
                        SenseService.getAdjTypeSademorakkab(
                            rs.getString("adj_type_sademorakkab")
                        ),
                        rs.getBoolean("vIssababi"),
                        rs.getBoolean("vIsIdiom"),
                        SenseService.getVGozaraType(rs.getString("vGozaraType")),
                        rs.getBoolean("kootah_nevesht"),
                        rs.getBoolean("mohavere"),
                    )
                )
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getSenseRelationsById(cls, senseId):
        results = ArrayList()
        sql = (
            "SELECT id, type, sense, sense2, senseWord1, senseWord2 FROM sense_relation WHERE sense = "
            + senseId
            + " OR sense2 = "
            + senseId
        )
        try:
            while rs.next():
                results.add(
                    SenseRelation(
                        rs.getInt("id"),
                        rs.getInt("sense"),
                        rs.getInt("sense2"),
                        rs.getString("senseWord1"),
                        rs.getString("senseWord2"),
                        rs.getString("type"),
                    )
                )
        except SQLException as e:
            e.printStackTrace()
        resultsArr = ArrayList()
        i = 0
        while i < len(results):
            if temp.getSenseId1() != senseId:
                temp.setType(SenseService.ReverseSRelationType(type_))
                temp.setSenseId1(senseId2)
                temp.setSenseId2(senseId1)
                temp.setSenseWord1(senseWord2)
                temp.setSenseWord2(senseWord1)
            resultsArr.add(temp)
            i += 1
        return resultsArr

    @classmethod
    def getSenseRelationsByType(cls, senseId, types):
        results = ArrayList()
        _types = ""
        _revTypes = ""
        for type_ in types:
            _types = (
                String.valueOf(_types) + "'" + SenseService.RelationValue(type_) + "',"
            )
            _revTypes = (
                String.valueOf(_revTypes)
                + "'"
                + SenseService.RelationValue(SenseService.ReverseRelationType(type_))
                + "',"
            )
        _types = String.valueOf(_types) + "'not_type'"
        _revTypes = String.valueOf(_revTypes) + "'not_type'"
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
        try:
            while rs.next():
                results.add(
                    SenseRelation(
                        rs.getInt("id"),
                        rs.getInt("sense"),
                        rs.getInt("sense2"),
                        rs.getString("senseWord1"),
                        rs.getString("senseWord2"),
                        rs.getString("type"),
                    )
                )
        except SQLException as e:
            e.printStackTrace()
        resultsArr = ArrayList()
        i = 0
        while i < len(results):
            if temp.getSenseId1() != senseId:
                temp.setType(SenseService.ReverseSRelationType(type_))
                temp.setSenseId1(senseId2)
                temp.setSenseId2(senseId1)
                temp.setSenseWord1(senseWord2)
                temp.setSenseWord2(senseWord1)
            resultsArr.add(temp)
            i += 1
        return resultsArr

    @classmethod
    def getPhoneticFormsByWord(cls, wordId):
        results = ArrayList()
        sql = "SELECT id, value FROM speech WHERE word = " + wordId
        try:
            while rs.next():
                results.add(PhoneticForm(rs.getInt("id"), rs.getString("value")))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getWrittenFormsByWord(cls, wordId):
        results = ArrayList()
        sql = "SELECT id, value FROM value WHERE word = " + wordId
        try:
            while rs.next():
                results.add(WrittenForm(rs.getInt("id"), rs.getString("value")))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def NormalValue(cls, Value):
        NormalValue = Value
        NormalValue = NormalValue.replace("\u06cc", "\u064a")
        NormalValue = NormalValue.replace("\u0649", "\u064a")
        NormalValue = NormalValue.replace("\u0643", "\u06a9")
        NormalValue = NormalValue.replace("'", "")
        NormalValue = NormalValue.replace('"', "")
        NormalValue = NormalValue.replace(" ", "")
        NormalValue = NormalValue.replace("\u200c", "")
        NormalValue = NormalValue.replace("\u200c\u200c\u0621", "")
        NormalValue = NormalValue.replace("\u200c\u200c\u0654", "")
        NormalValue = NormalValue.replace("\u200c\u200c\u0624", "\u0648")
        NormalValue = NormalValue.replace("\u200c\u200c\u0626", "\u064a")
        NormalValue = NormalValue.replace("\u0622", "\u0627")
        NormalValue = NormalValue.replace("\u200c\u200c\u0623", "\u0627")
        NormalValue = NormalValue.replace("\u0625", "\u0627")
        NormalValue = NormalValue.replace("\u06c0", "\u0647")
        NormalValue = NormalValue.replace("\u0629", "\u0647")
        NormalValue = NormalValue.replace("\u064e", "")
        NormalValue = NormalValue.replace("\u064f", "")
        NormalValue = NormalValue.replace("\u0650", "")
        NormalValue = NormalValue.replace("\u064b", "")
        NormalValue = NormalValue.replace("\u064c", "")
        NormalValue = NormalValue.replace("\u064d", "")
        NormalValue = NormalValue.replace("\u0651", "")
        NormalValue = NormalValue.replace("\u0652", "")
        NormalValue = NormalValue.replace("\u0651\u0650", "")
        NormalValue = NormalValue.replace("\u0651\u064d", "")
        NormalValue = NormalValue.replace("\u0651\u064e", "")
        NormalValue = NormalValue.replace("\u0651\u064b", "")
        NormalValue = NormalValue.replace("\u0651\u064f", "")
        NormalValue = NormalValue.replace("\u0651\u064c", "")
        NormalValue = NormalValue.replace("u200D", "%")
        NormalValue = NormalValue.replace("\u0621", "")
        NormalValue = NormalValue.replace("\u0623", "\u0627")
        NormalValue = NormalValue.replace("\u0626", "\u064a")
        return NormalValue

    @classmethod
    def SecureValue(cls, Value):
        if Value == None:
            return ""
        Value = Value.replace("\u0000", "")
        Value = Value.replace("'", "")
        Value = Value.replace('"', "")
        Value = Value.replace("\b", "")
        Value = Value.replace("\n", "")
        Value = Value.replace("\r", "")
        Value = Value.replace("\t", "")
        Value = Value.replace("\\", "")
        Value = Value.replace("/", "")
        Value = Value.replace("%", "")
        Value = Value.replace("_", "")
        Value = Value.replace("\u0640", "")
        Value = Value.replace("!", "")
        Value = Value.replace(";", "")
        Value = Value.replace("?", "")
        Value = Value.replace("=", "")
        Value = Value.replace("<", "")
        Value = Value.replace(">", "")
        Value = Value.replace("&", "")
        Value = Value.replace("#", "")
        Value = Value.replace("@", "")
        Value = Value.replace("$", "")
        Value = Value.replace("^", "")
        Value = Value.replace("*", "")
        Value = Value.replace("+", "")
        return Value

    @classmethod
    def getVtansivity(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -1724158427:
            if string == "transitive":
                return "Transitive"
            return value
        elif string.hashCode() == 841936170:
            if string == "inTransitive":
                return "Intransitive"
            return value
        elif string.hashCode() == 1845861045:
            if not string == "dovajhi":
                return value
            return "Causative/Anticausative"
        return value

    @classmethod
    def getVactivity(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -1422950650:
            if string == "active":
                return "Active"
            return value
        elif string.hashCode() == -792039641:
            if string == "passive":
                return "Passive"
            return value
        return value

    @classmethod
    def getVtype(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -1431524879:
            if string == "simpleVerb":
                return "Simple"
            return value
        elif string.hashCode() == -1054772775:
            if string == "pishvandiVerb":
                return "Phrasal"
            return value
        elif string.hashCode() == -570810619:
            if string == "auxiliaryVerb":
                return "Auxiliary"
            return value
        elif string.hashCode() == 530219749:
            if string == "copulaVerb":
                return "Copula"
            return value
        elif string.hashCode() == 1665965418:
            if string == "compoundVerb":
                return "Complex"
            return value
        return value

    @classmethod
    def getCategory(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -49458414:
            if string == "category_masdari":
                return "Infinitival"
            return value
        elif string.hashCode() == 318357937:
            if string == "category_esmZamir":
                return "Pronoun"
            return value
        elif string.hashCode() == 338298407:
            if string == "category_adad":
                return "Numeral"
            return value
        elif string.hashCode() == 338599184:
            if string == "category_khAs":
                return "Specific"
            return value
        elif string.hashCode() == 1537779501:
            if string == "category_Am":
                return "General"
            return value
        return value

    @classmethod
    def getGoupOrMokassar(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -826418989:
            if string == "am_khas_esmejam":
                return "MassNoun"
            return value
        elif string.hashCode() == 134174425:
            if string == "am_khas_jam":
                return "Regular"
            return value
        elif string.hashCode() == 1892681254:
            if string == "am_khas_mokassar":
                return "Irregular"
            return value
        return value

    @classmethod
    def getEsmeZamir(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -969140441:
            if string == "gheir_moshakhas":
                return "Indefinite"
            return value
        elif string.hashCode() == 534797624:
            if string == "motaghabel":
                return "Reciprocal"
            return value
        elif string.hashCode() == 714990811:
            if string == "noun_type_morakab":
                return ""
            return value
        elif string.hashCode() == 1224364290:
            if not string == "moakkad":
                return value
            return "Emphatic"
        return value

    @classmethod
    def getAdad(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -1537886559:
            if string == "tartibi":
                return "Ordinal"
            return value
        elif string.hashCode() == 3003695:
            if not string == "asli":
                return value
            return "Cardinal"
        return value

    @classmethod
    def getAdverbType1(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        string = value
        if string.hashCode() == -1609563487:
            if string == "moshtagh_morakab":
                return "DerivationalCompound"
            return value
        elif string.hashCode() == -221942702:
            if string == "morakkab":
                return "Compound"
            return value
        elif string.hashCode() == -186590203:
            if string == "moshtagh":
                return "Derivative"
            return value
        elif string.hashCode() == 109191060:
            if string == "saade":
                return "Simple"
            return value
        return value

    @classmethod
    def getNormalValue(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return value

    @classmethod
    def getAdverbType2(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        res = " "
        if value.charAt(0) == "1":
            res = String.valueOf(res) + "AdjectiveModifying,"
        elif value.charAt(0) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(0) + ","
        if value.charAt(1) == "1":
            res = String.valueOf(res) + "AdverbModifying,"
        elif value.charAt(1) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(1) + ","
        if value.charAt(2) == "1":
            res = String.valueOf(res) + "VerbModifying,"
        elif value.charAt(2) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(2) + ","
        if value.charAt(3) == "1":
            res = String.valueOf(res) + "SentenceModifying,"
        elif value.charAt(3) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(3) + ","
        return res.substring(0, len(res) - 1)

    @classmethod
    def getAdjPishinVijegi(cls, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        string = value
        if string.hashCode() == -282395544:
            if string == "Yes_taajobi":
                return "Exclamatory"
            return value
        elif string.hashCode() == 770492981:
            if string == "Yes_Nothing":
                return "Simple"
            return value
        elif string.hashCode() == 1795033874:
            if string == "Yes_eshare":
                return "Demonstrative"
            return value
        elif string.hashCode() == 2020200460:
            if not string == "Yes_mobham":
                return value
            return "Indefinite"
        return value

    @classmethod
    def getAdjType(cls, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        string = value
        if string.hashCode() == -1735880873:
            if string == "bartarin":
                return "Superlative"
            return value
        elif string.hashCode() == -1396218190:
            if string == "bartar":
                return "Comparative"
            return value
        elif string.hashCode() == 1241931560:
            if string == "motlagh":
                return "Absolute"
            return value
        return value

    @classmethod
    def getNoeKhas(cls, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        string = value
        if string.hashCode() == -533828350:
            if string == "noe_khas_ensan":
                return "Human"
            return value
        elif string.hashCode() == -526835153:
            if string == "noe_khas_makan":
                return "Place"
            return value
        elif string.hashCode() == -514827458:
            if string == "noe_khas_zaman":
                return "Time"
            return value
        elif string.hashCode() == 708964732:
            if string == "noe_khas_heyvan":
                return "Animal"
            return value
        return value

    @classmethod
    def getAdjTypeSademorakkab(cls, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        string = value
        if string.hashCode() == -1398986386:
            if string == "adj_type_morakab":
                return "Compound"
            return value
        elif string.hashCode() == -383542830:
            if string == "adj_type_moshtagh":
                return "Derivative"
            return value
        elif string.hashCode() == -264504089:
            if string == "adj_type_saade":
                return "Simple"
            return value
        elif string.hashCode() == 1930601326:
            if string == "adj_type_moshtagh_morakab":
                return "DerivatinalCompound"
            return value
        return value

    @classmethod
    def getVGozaraType(cls, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        res = " "
        if value.charAt(0) == "1":
            res = String.valueOf(res) + "WithComplement,"
        elif value.charAt(0) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(0) + ","
        if value.charAt(1) == "1":
            res = String.valueOf(res) + "WithObject,"
        elif value.charAt(1) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(1) + ","
        if value.charAt(2) == "1":
            res = String.valueOf(res) + "WithPredicate,"
        elif value.charAt(2) == "0":
            res = String.valueOf(res)
        else:
            res = String.valueOf(res) + value.charAt(2) + ","
        return res.substring(0, len(res) - 1)

    @classmethod
    def getNounType(cls, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        string = value
        if string.hashCode() == -1881033151:
            if string == "noun_type_ebarat":
                return "Phrasal"
            return value
        elif string.hashCode() == -601968748:
            if string == "noun_type_saade":
                return "Simple"
            return value
        elif string.hashCode() == 714990811:
            if string == "noun_type_morakab":
                return "Compound"
            return value
        elif string.hashCode() == 725240837:
            if string == "noun_type_moshtagh":
                return "Derivative"
            return value
        elif string.hashCode() == 1576628897:
            if string == "noun_type_moshtagh_morakab":
                return "DerivatinalCompound"
            return value
        return value

    @classmethod
    def RelationValue(cls, type_):
        if type_.__str__() == "Derivationally_related_form":
            return "Derivationally related form"
        return type_.__str__().replace("_", "-")

    @classmethod
    def ReverseRelationType(cls, type_):
        if SenseRelationType.Refer_to == type_:
            return SenseRelationType.Is_Referred_by
        if SenseRelationType.Is_Referred_by == type_:
            return SenseRelationType.Refer_to
        if SenseRelationType.Verbal_Part == type_:
            return SenseRelationType.Is_Verbal_Part_of
        if SenseRelationType.Is_Verbal_Part_of == type_:
            return SenseRelationType.Verbal_Part
        if SenseRelationType.Is_Non_Verbal_Part_of == type_:
            return SenseRelationType.Non_Verbal_Part
        if SenseRelationType.Non_Verbal_Part == type_:
            return SenseRelationType.Is_Non_Verbal_Part_of
        return type_

    @classmethod
    def ReverseSRelationType(cls, type_):
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
