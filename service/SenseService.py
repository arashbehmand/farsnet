import farsnet.schema
import farsnet.database

class SenseService(object):
    def __init__(self):
        self.con = farsnet.database.SqlLiteDbUtility.get_connection()

    def get_senses_by_word(self, search_style, search_keyword):
        results = list()
        sql = "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.id IN (SELECT sense.id FROM word INNER JOIN sense ON sense.word = word.id LEFT OUTER JOIN value ON value.word = word.id WHERE word.search_value @SearchStyle '@SearchValue' OR value.search_value @SearchStyle '@SearchValue') OR sense.id IN (SELECT sense.id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') OR sense.id IN (SELECT sense_2.id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') "
        search_keyword = self._secure_value(
            self.normal_value(search_keyword)
        )
        if search_style == "LIKE" or search_style == "START" or search_style == "END":
            sql = sql.replace("@SearchStyle", "LIKE")
            if search_style == "LIKE":
                search_keyword = "%" + search_keyword + "%"
            if search_style == "START":
                search_keyword = search_keyword + "%"
            if search_style == "END":
                search_keyword = "%" + search_keyword
        if search_style == "EXACT":
            sql = sql.replace("@SearchStyle", "=")
        sql = sql.replace("@SearchValue", search_keyword)
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
                    self._get_verb_tansivity(row["vtansivity"]),
                    self._get_verb_activity(row["vactivity"]),
                    self._get_verb_type(row["vtype"]),
                    self._get_normal_value(row["synset"]),
                    self._get_normal_value(row["vpastStem"]),
                    self._get_normal_value(row["vpresentStem"]),
                    self._get_category(row["category"]),
                    self._get_goup_or_mokassar(row["goupOrMokassar"]),
                    self._get_esme_zamir(row["esmeZamir"]),
                    self._get_adad(row["adad"]),
                    self.get_adverb_type1(row["adverb_type_1"]),
                    self.get_adverb_type2(row["adverb_type_2"]),
                    self._get_adj_pishin_vijegi(
                        row["adj_pishin_vijegi"]
                    ),
                    self._get_adj_type(row["adj_type"]),
                    self._get_noe_khas(row["noe_khas"]),
                    self._get_noun_type(row["nounType"]),
                    self._get_adj_type_sademorakkab(
                        row["adj_type_sademorakkab"]
                    ),
                    row["vIssababi"],
                    row["vIsIdiom"],
                    self._get_verb_gozara_type(row["vGozaraType"]),
                    row["kootah_nevesht"],
                    row["mohavere"],
                )
            )
        return results

    def get_senses_by_synset(self, synset_id):
        results = list()
        sql = (
            "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.synset = "
            + str(synset_id)
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
                    self._get_verb_tansivity(row["vtansivity"]),
                    self._get_verb_activity(row["vactivity"]),
                    self._get_verb_type(row["vtype"]),
                    self._get_normal_value(row["synset"]),
                    self._get_normal_value(row["vpastStem"]),
                    self._get_normal_value(row["vpresentStem"]),
                    self._get_category(row["category"]),
                    self._get_goup_or_mokassar(row["goupOrMokassar"]),
                    self._get_esme_zamir(row["esmeZamir"]),
                    self._get_adad(row["adad"]),
                    self.get_adverb_type1(row["adverb_type_1"]),
                    self.get_adverb_type2(row["adverb_type_2"]),
                    self._get_adj_pishin_vijegi(
                        row["adj_pishin_vijegi"]
                    ),
                    self._get_adj_type(row["adj_type"]),
                    self._get_noe_khas(row["noe_khas"]),
                    self._get_noun_type(row["nounType"]),
                    self._get_adj_type_sademorakkab(
                        row["adj_type_sademorakkab"]
                    ),
                    row["vIssababi"],
                    row["vIsIdiom"],
                    self._get_verb_gozara_type(row["vGozaraType"]),
                    row["kootah_nevesht"],
                    row["mohavere"],
                )
            )
        return results

    def get_sense_by_id(self, sense_id):
        result = None
        sql = (
            "SELECT sense.id, seqId, vtansivity, vactivity, vtype, synset, vpastStem, vpresentStem, category, goupOrMokassar, esmeZamir, adad, adverb_type_1, adverb_type_2, adj_pishin_vijegi, adj_type, noe_khas, nounType, adj_type_sademorakkab, vIssababi, vIsIdiom, vGozaraType, kootah_nevesht, mohavere, word.id as wordId, word.defaultValue, word.avaInfo, word.pos FROM sense INNER JOIN word ON sense.word = word.id WHERE sense.id = "
            + str(sense_id)
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
                self._get_verb_tansivity(row["vtansivity"]),
                self._get_verb_activity(row["vactivity"]),
                self._get_verb_type(row["vtype"]),
                self._get_normal_value(row["synset"]),
                self._get_normal_value(row["vpastStem"]),
                self._get_normal_value(row["vpresentStem"]),
                self._get_category(row["category"]),
                self._get_goup_or_mokassar(row["goupOrMokassar"]),
                self._get_esme_zamir(row["esmeZamir"]),
                self._get_adad(row["adad"]),
                self.get_adverb_type1(row["adverb_type_1"]),
                self.get_adverb_type2(row["adverb_type_2"]),
                self._get_adj_pishin_vijegi(row["adj_pishin_vijegi"]),
                self._get_adj_type(row["adj_type"]),
                self._get_noe_khas(row["noe_khas"]),
                self._get_noun_type(row["nounType"]),
                self._get_adj_type_sademorakkab(
                    row["adj_type_sademorakkab"]
                ),
                row["vIssababi"],
                row["vIsIdiom"],
                self._get_verb_gozara_type(row["vGozaraType"]),
                row["kootah_nevesht"],
                row["mohavere"],
            )
        return result

    def get_all_senses(self):
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
                    self._get_verb_tansivity(row["vtansivity"]),
                    self._get_verb_activity(row["vactivity"]),
                    self._get_verb_type(row["vtype"]),
                    self._get_normal_value(row["synset"]),
                    self._get_normal_value(row["vpastStem"]),
                    self._get_normal_value(row["vpresentStem"]),
                    self._get_category(row["category"]),
                    self._get_goup_or_mokassar(row["goupOrMokassar"]),
                    self._get_esme_zamir(row["esmeZamir"]),
                    self._get_adad(row["adad"]),
                    self.get_adverb_type1(row["adverb_type_1"]),
                    self.get_adverb_type2(row["adverb_type_2"]),
                    self._get_adj_pishin_vijegi(
                        row["adj_pishin_vijegi"]
                    ),
                    self._get_adj_type(row["adj_type"]),
                    self._get_noe_khas(row["noe_khas"]),
                    self._get_noun_type(row["nounType"]),
                    self._get_adj_type_sademorakkab(
                        row["adj_type_sademorakkab"]
                    ),
                    row["vIssababi"],
                    row["vIsIdiom"],
                    self._get_verb_gozara_type(row["vGozaraType"]),
                    row["kootah_nevesht"],
                    row["mohavere"],
                )
            )
        return results

    def get_sense_relations_by_id(self, sense_id):
        results = list()
        sql = (
            "SELECT id, type, sense, sense2, senseWord1, senseWord2 FROM sense_relation WHERE sense = "
            + str(sense_id)
            + " OR sense2 = "
            + str(sense_id)
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

        reslut_arr = list()
        for res in results:
            if res.sense_id1 != sense_id:
                type_ = res.type_
                sense_id2 = res.sense_id2
                sense_id1 = res.sense_id1
                sense_word2 = res.sense_word1
                sense_word1 = res.sense_word2
                res.type = self._reverse_str_relation_type(type_)
                res.sense_id1 = sense_id2
                res.sense_id2 = sense_id1
                res.sense_word1 = sense_word2
                res.sense_word2 = sense_word1
            reslut_arr.append(res)
        return reslut_arr

    def get_sense_relations_by_type(self, sense_id, types):
        results = list()
        _types = ""
        _revTypes = ""
        for type_ in types:
            _types = (
                str(_types) + "'" + self._relation_value(type_) + "',"
            )
            _revTypes = (
                str(_revTypes)
                + "'"
                + self._relation_value(self._reverse_relation_type(type_))
                + "',"
            )
        _types = str(_types) + "'not_type'"
        _revTypes = str(_revTypes) + "'not_type'"
        sql = (
            "SELECT id, type, sense, sense2, senseWord1, senseWord2 FROM sense_relation WHERE (sense = "
            + sense_id
            + " AND type in ("
            + _types
            + ")) OR (sense2 = "
            + sense_id
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


        reslut_arr = list()
        for res in results:
            if res.sense_id1 != sense_id:
                type_ = res.type_
                sense_id2 = res.sense_id2
                sense_id1 = res.sense_id1
                sense_word2 = res.sense_word1
                sense_word1 = res.sense_word2
                res.type = self._reverse_str_relation_type(type_)
                res.sense_id1 = sense_id2
                res.sense_id2 = sense_id1
                res.sense_word1 = sense_word2
                res.sense_word2 = sense_word1
            reslut_arr.append(res)
        return reslut_arr

    def get_phonetic_forms_by_word(self, word_id):
        results = list()
        sql = "SELECT id, value FROM speech WHERE word = " + str(word_id)
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            results.append(farsnet.schema.PhoneticForm(row["id"], row["value"]))
        return results

    def get_written_forms_by_word(self, word_id):
        results = list()
        sql = "SELECT id, value FROM value WHERE word = " + str(word_id)
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            results.append(farsnet.schema.WrittenForm(row["id"], row["value"]))
        return results

    def normal_value(self, value):
        normal_value = value.replace("\u06cc", "\u064a").\
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
        return normal_value

    def _secure_value(self, value):
        if value == None:
            return ""
        value = value.replace("\u0000", "").\
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
        return value

    def _get_verb_tansivity(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"dovajhi":"Causative/Anticausative",
                "inTransitive":"Intransitive",
                "transitive":"Transitive"}\
                .get(value,value)

    def _get_verb_activity(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"active":"Active",
                "passive":"Passive"}\
                .get(value,value)

    def _get_verb_type(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"auxiliaryVerb":"Auxiliary",
                "compoundVerb":"Complex",
                "copulaVerb":"Copula",
                "pishvandiVerb":"Phrasal",
                "simpleVerb":"Simple"}\
                .get(value,value)

    def _get_category(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"category_adad":"Numeral",
                "category_Am":"General",
                "category_khAs":"Specific",
                "category_masdari":"Infinitival",
                "category_esmZamir":"Pronoun"}\
                .get(value,value)

    def _get_goup_or_mokassar(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"am_khas_esmejam":"MassNoun",
                "am_khas_jam":"Regular",
                "am_khas_mokassar":"Irregular"}\
                .get(value,value)

    def _get_esme_zamir(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"moakkad":"Emphatic",
                "gheir_moshakhas":"Indefinite",
                "motaghabel":"Reciprocal",
                "noun_type_morakab":""}\
                .get(value,value)

    def _get_adad(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"asli":"Cardinal",
                "tartibi":"Ordinal"}\
                .get(value,value)

    def get_adverb_type1(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return {"morakkab":"Compound",
                "moshtagh":"Derivative",
                "moshtagh_morakab":"DerivationalCompound",
                "saade":"Simple"}\
                .get(value,value)
        
    def _get_normal_value(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        return value

    def get_adverb_type2(self, value):
        if value == None or value == "" or value == "Nothing":
            return ""
        res = " "
        if value[0] == "1":
            res += "AdjectiveModifying,"
        elif value[0] != "0":
            res += value[0] + ","
        if value[1] == "1":
            res += "AdverbModifying,"
        elif value[1] != "0":
            res += value[1] + ","
        if value[2] == "1":
            res += "VerbModifying,"
        elif value[2] != "0":
            res += value[2] + ","
        if value[3] == "1":
            res += "SentenceModifying,"
        elif value[3] != "0":
            res += value[3] + ","
        return res[:-1]

    def _get_adj_pishin_vijegi(self, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        return {"Yes_mobham":"Indefinite",
                "Yes_taajobi":"Exclamatory",
                "Yes_eshare":"Demonstrative",
                "Yes_Nothing":"Simple"}\
                .get(value,value)

    def _get_adj_type(self, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        return {"bartarin":"Superlative",
                "motlagh":"Absolute",
                "bartar":"Comparative"}\
                .get(value,value)

    def _get_noe_khas(self, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        return {"noe_khas_ensan":"Human",
                "noe_khas_heyvan":"Animal",
                "noe_khas_makan":"Place",
                "noe_khas_zaman":"Time"}\
                .get(value,value)

    def _get_adj_type_sademorakkab(self, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        return {"adj_type_morakab":"Compound",
                "adj_type_moshtagh":"Derivative",
                "adj_type_moshtagh_morakab":"DerivatinalCompound",
                "adj_type_saade":"Simple"}\
                .get(value,value)

    def _get_verb_gozara_type(self, value):
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

    def _get_noun_type(self, value):
        if value == None or value == "" or value == "Nothing" or value == "No":
            return ""
        return {"noun_type_morakab":"Compound",
                "noun_type_moshtagh":"Derivative",
                "noun_type_moshtagh_morakab":"DerivatinalCompound",
                "noun_type_saade":"Simple",
                "noun_type_ebarat":"Phrasal"}\
                .get(value,value)

    def _relation_value(self, type_):
        if type_ == "Derivationally_related_form":
            return "Derivationally related form"
        return type_.replace("_", "-")

    def _reverse_relation_type(self, type_):
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

    def _reverse_str_relation_type(self, type_):
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