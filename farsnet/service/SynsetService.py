import farsnet.schema
import farsnet.database


class SynsetService(object):
    def __init__(self):
        self.con = farsnet.database.SqlLiteDbUtility.get_connection()

    def get_synsets_by_word(self, search_style, search_keyword):
        results = list()
        sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset WHERE synset.id IN (SELECT synset.id as synset_id FROM word INNER JOIN sense ON sense.word = word.id INNER JOIN synset ON sense.synset = synset.id LEFT OUTER JOIN value ON value.word = word.id WHERE word.search_value @SearchStyle '@SearchValue' OR (value.search_value) @SearchStyle '@SearchValue')  OR synset.id IN (SELECT sense.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') OR synset.id IN (SELECT sense_2.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue')"
        search_keyword = self._secure_value(self.normal_value(search_keyword))
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
                farsnet.schema.Synset(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                )
            )
        return results

    def get_all_synsets(self):
        results = list()
        sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset "
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            results.append(
                farsnet.schema.Synset(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                )
            )
        return results

    def get_synset_by_id(self, synset_id):
        sql = (
            "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset WHERE id="
            + str(synset_id)
        )
        result = None
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            result = farsnet.schema.Synset(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
            )
        return result

    def get_synset_relations_by_id(self, synset_id):
        results = list()
        sql = (
            "SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE synset="
            + str(synset_id)
            + " OR synset2="
            + str(synset_id)
        )
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            results.append(
                farsnet.schema.SynsetRelation(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                )
            )

        reslut_arr = list()
        for res in results:
            if res.synset_id1 != synset_id:
                type_ = res.type_
                reverse_type = res.reverse_type
                synset_id2 = res.synset_id2
                synset_id1 = res.synset_id1
                synset_words2 = res.synset_words1
                synset_words1 = res.synset_words2
                res.reverse_type = type_
                res.type_ = reverse_type
                res.synset_id1 = synset_id2
                res.synset_id2 = synset_id1
                res.synsetWord1 = synset_words2
                res.synsetWord2 = synset_words1
            reslut_arr.append(res)
        return reslut_arr

    def get_synset_relations_by_type(self, synset_id, types):
        results = list()
        _types = ""
        _revTypes = ""
        for type_ in types:
            _types = str(_types) + "'" + self._relation_value(type_) + "',"
            _revTypes = (
                str(_revTypes)
                + "'"
                + self._relation_value(self._reverse_relation_type(type_))
                + "',"
            )
        _types = str(_types) + "'not_type'"
        _revTypes = str(_revTypes) + "'not_type'"
        sql = (
            "SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE (synset = "
            + str(synset_id)
            + " AND type in ("
            + _types
            + ")) OR (synset2 = "
            + str(synset_id)
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
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                )
            )

        reslut_arr = list()
        for res in results:
            if res.synset_id1 != synset_id:
                type_ = res.type_
                reverse_type = res.reverse_type
                synset_id2 = res.synset_id2
                synset_id1 = res.synset_id1
                synset_words2 = res.synset_words1
                synset_words1 = res.synset_words2
                res.reverse_type = type_
                res.type_ = reverse_type
                res.synset_id1 = synset_id2
                res.synset_id2 = synset_id1
                res.synsetWord1 = synset_words2
                res.synsetWord2 = synset_words1
            reslut_arr.append(res)
        return reslut_arr

    def get_wordnet_synsets(self, synset_id):
        results = list()
        sql = (
            "SELECT id, wnPos, wnOffset, example, gloss, synset, type FROM wordnetsynset WHERE synset="
            + str(synset_id)
        )
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            results.append(
                farsnet.schema.WordNetSynset(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                )
            )
        return results

    def get_synset_examples(self, synset_id):
        results = list()
        # sql = (
        #     "SELECT gloss_and_example.id, content, lexicon.title FROM gloss_and_example INNER JOIN lexicon ON gloss_and_example.lexicon=lexicon.id WHERE type='EXAMPLE' and synset="
        #     + str(synset_id)
        # )
        sql = (
            "SELECT id, content FROM gloss_and_example WHERE type='EXAMPLE' and synset="
            + str(synset_id)
        )
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            # results.append(farsnet.schema.SynsetExample(row[0], row[1], row[2]))
            results.append(farsnet.schema.SynsetExample(row[0], row[1], None))
        return results

    def get_synset_glosses(self, synset_id):
        results = list()
        # sql = (
        #     "SELECT gloss_and_example.id, content, lexicon.title FROM gloss_and_example INNER JOIN lexicon ON gloss_and_example.lexicon=lexicon.id WHERE type='GLOSS' and synset="
        #     + str(synset_id)
        # )
        sql = (
            "SELECT id, content FROM gloss_and_example WHERE type='GLOSS' and synset="
            + str(synset_id)
        )
        cur = self.con.cursor()
        cur.execute(sql)
        for row in cur:
            # results.append(farsnet.schema.SynsetGloss(row[0], row[1], row[2]))
            results.append(farsnet.schema.SynsetGloss(row[0], row[1], None))
        return results

    def normal_value(self, value):
        normal_value = (
            value.replace("\u06cc", "\u064a")
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
        return normal_value

    def _secure_value(self, value):
        if value == None:
            return ""
        value = (
            value.replace("\u0000", "")
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
        return value

    def _relation_value(self, type_):
        if type_ == "Related_to" or type_ == "Has-Unit" or type_[:3] == "Is_":
            return type_.replace("_", "-")
        if type_ == "Has_Salient_defining_feature":
            return "Has-Salient defining feature"
        return type_.replace("_", " ")

    def _reverse_relation_type(self, type_):
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
