#!/usr/bin/env python
""" generated source for module SynsetService """
# 
#  * Decompiled with CFR 0.145.
#  
# package: farsnet.service
import farsnet.database.SqlLiteDbUtility

import farsnet.schema.Synset

import farsnet.schema.SynsetExample

import farsnet.schema.SynsetGloss

import farsnet.schema.SynsetRelation

import farsnet.schema.SynsetRelationType

import farsnet.schema.WordNetSynset

import java.sql.Connection

import java.sql.PreparedStatement

import java.sql.ResultSet

import java.sql.SQLException

import java.util.ArrayList

import java.util.List

class SynsetService(object):
    """ generated source for class SynsetService """
    @classmethod
    def getSynsetsByWord(cls, searchStyle, searchKeyword):
        """ generated source for method getSynsetsByWord """
        results = ArrayList()
        sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset WHERE synset.id IN (SELECT synset.id as synset_id FROM word INNER JOIN sense ON sense.word = word.id INNER JOIN synset ON sense.synset = synset.id LEFT OUTER JOIN value ON value.word = word.id WHERE word.search_value @SearchStyle '@SearchValue' OR (value.search_value) @SearchStyle '@SearchValue')  OR synset.id IN (SELECT sense.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense_2.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue') OR synset.id IN (SELECT sense_2.synset AS synset_id FROM sense INNER JOIN sense_relation ON sense.id = sense_relation.sense INNER JOIN sense AS sense_2 ON sense_2.id = sense_relation.sense2 INNER JOIN word ON sense.word = word.id WHERE sense_relation.type =  'Refer-to' AND word.search_value LIKE  '@SearchValue')"
        searchKeyword = SynsetService.SecureValue(SynsetService.NormalValue(searchKeyword))
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
                results.add(Synset(rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7)))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getAllSynsets(cls):
        """ generated source for method getAllSynsets """
        results = ArrayList()
        sql = "SELECT id, pos, semanticCategory, example, gloss, nofather, noMapping FROM synset "
        try:
            while rs.next():
                results.add(Synset(rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7)))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getSynsetById(cls, synsetId):
        """ generated source for method getSynsetById """
        result = None
        try:
            while rs.next():
                result = Synset(rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7))
        except SQLException as e:
            e.printStackTrace()
        return result

    @classmethod
    def getSynsetRelationsById(cls, synsetId):
        """ generated source for method getSynsetRelationsById """
        results = ArrayList()
        sql = "SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE synset=" + synsetId + " OR synset2=" + synsetId
        try:
            while rs.next():
                results.add(SynsetRelation(rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4), rs.getInt(5), rs.getInt(6), rs.getString(7)))
        except SQLException as e:
            e.printStackTrace()
        resultsArr = ArrayList()
        # 
        #  * Decompiled with CFR 0.145.
        #  
        i = 0
        while i < len(results):
            # 
            #  * Decompiled with CFR 0.145.
            #  
            if temp.getSynsetId1() != synsetId:
                temp.setReverseType(type_)
                temp.setSynsetId1(synsetId2)
                temp.setSynsetId2(synsetId1)
                temp.setSynsetWords1(synsetWords2)
                temp.setSynsetWords2(synsetWords1)
                temp.setType(reverseType)
            resultsArr.add(temp)
            i += 1
        return resultsArr

    @classmethod
    def getSynsetRelationsByType(cls, synsetId, types):
        """ generated source for method getSynsetRelationsByType """
        results = ArrayList()
        _types = ""
        _revTypes = ""
        for type_ in types:
            _types = String.valueOf(_types) + "'" + SynsetService.RelationValue(type_) + "',"
            _revTypes = String.valueOf(_revTypes) + "'" + SynsetService.RelationValue(SynsetService.ReverseRelationType(type_)) + "',"
        _types = String.valueOf(_types) + "'not_type'"
        _revTypes = String.valueOf(_revTypes) + "'not_type'"
        sql = "SELECT id, type, synsetWords1, synsetWords2, synset, synset2, reverse_type FROM synset_relation WHERE (synset = " + synsetId + " AND type in (" + _types + ")) OR (synset2 = " + synsetId + " AND type in (" + _revTypes + "))" + " ORDER BY synset"
        try:
            while rs.next():
                results.add(SynsetRelation(rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4), rs.getInt(5), rs.getInt(6), rs.getString(7)))
        except SQLException as e:
            e.printStackTrace()
        resultsArr = ArrayList()
        # 
        #  * Decompiled with CFR 0.145.
        #  
        i = 0
        while i < len(results):
            # 
            #  * Decompiled with CFR 0.145.
            #  
            if temp.getSynsetId1() != synsetId:
                temp.setReverseType(type_)
                temp.setSynsetId1(synsetId2)
                temp.setSynsetId2(synsetId1)
                temp.setSynsetWords1(synsetWords2)
                temp.setSynsetWords2(synsetWords1)
                temp.setType(reverseType)
            resultsArr.add(temp)
            i += 1
        return results

    @classmethod
    def getWordNetSynsets(cls, synsetId):
        """ generated source for method getWordNetSynsets """
        results = ArrayList()
        sql = "SELECT id, wnPos, wnOffset, example, gloss, synset, type FROM wordnetsynset WHERE synset=" + synsetId
        try:
            while rs.next():
                results.add(WordNetSynset(rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4), rs.getString(5), rs.getInt(6), rs.getString(7)))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getSynsetExamples(cls, synsetId):
        """ generated source for method getSynsetExamples """
        results = ArrayList()
        sql = "SELECT gloss_and_example.id, content, lexicon.title FROM gloss_and_example INNER JOIN lexicon ON gloss_and_example.lexicon=lexicon.id WHERE type='EXAMPLE' and synset=" + synsetId
        try:
            while rs.next():
                results.add(SynsetExample(rs.getInt(1), rs.getString(2), rs.getString(3)))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def getSynsetGlosses(cls, synsetId):
        """ generated source for method getSynsetGlosses """
        results = ArrayList()
        sql = "SELECT gloss_and_example.id, content, lexicon.title FROM gloss_and_example INNER JOIN lexicon ON gloss_and_example.lexicon=lexicon.id WHERE type='GLOSS' and synset=" + synsetId
        try:
            while rs.next():
                results.add(SynsetGloss(rs.getInt(1), rs.getString(2), rs.getString(3)))
        except SQLException as e:
            e.printStackTrace()
        return results

    @classmethod
    def NormalValue(cls, Value):
        """ generated source for method NormalValue """
        NormalValue = Value
        NormalValue = NormalValue.replace("\u06cc", "\u064a")
        NormalValue = NormalValue.replace("\u0649", "\u064a")
        NormalValue = NormalValue.replace("\u0643", "\u06a9")
        NormalValue = NormalValue.replace("'", "")
        NormalValue = NormalValue.replace("\"", "")
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
        """ generated source for method SecureValue """
        if Value == None:
            return ""
        Value = Value.replace("\u0000", "")
        Value = Value.replace("'", "")
        Value = Value.replace("\"", "")
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
    def RelationValue(cls, type_):
        """ generated source for method RelationValue """
        if type_.__str__() == "Related_to" or type_.__str__() == "Has-Unit" or type_.__str__().substring(3) == "Is_":
            return type_.__str__().replace("_", "-")
        if type_.__str__() == "Has_Salient_defining_feature":
            return "Has-Salient defining feature"
        return type_.__str__().replace("_", " ")

    @classmethod
    def ReverseRelationType(cls, type_):
        """ generated source for method ReverseRelationType """
        if SynsetRelationType.Agent == type_:
            return SynsetRelationType.Is_Agent_of
        if SynsetRelationType.Is_Agent_of == type_:
            return SynsetRelationType.Agent
        if SynsetRelationType.Hypernym == type_:
            return SynsetRelationType.Hyponym
        if SynsetRelationType.Hyponym == type_:
            return SynsetRelationType.Hypernym
        if SynsetRelationType.Instance_hyponym == type_:
            return SynsetRelationType.Instance_hypernym
        if SynsetRelationType.Instance_hypernym == type_:
            return SynsetRelationType.Instance_hyponym
        if SynsetRelationType.Part_holonym == type_:
            return SynsetRelationType.Part_meronym
        if SynsetRelationType.Part_meronym == type_:
            return SynsetRelationType.Part_holonym
        if SynsetRelationType.Member_holonym == type_:
            return SynsetRelationType.Member_meronym
        if SynsetRelationType.Member_meronym == type_:
            return SynsetRelationType.Member_holonym
        if SynsetRelationType.Substance_holonym == type_:
            return SynsetRelationType.Substance_meronym
        if SynsetRelationType.Substance_meronym == type_:
            return SynsetRelationType.Substance_holonym
        if SynsetRelationType.Portion_holonym == type_:
            return SynsetRelationType.Portion_meronym
        if SynsetRelationType.Portion_meronym == type_:
            return SynsetRelationType.Portion_holonym
        if SynsetRelationType.Domain == type_:
            return SynsetRelationType.Is_Domain_of
        if SynsetRelationType.Is_Domain_of == type_:
            return SynsetRelationType.Domain
        if SynsetRelationType.Cause == type_:
            return SynsetRelationType.Is_Caused_by
        if SynsetRelationType.Is_Caused_by == type_:
            return SynsetRelationType.Cause
        if SynsetRelationType.Is_Instrument_of == type_:
            return SynsetRelationType.Instrument
        if SynsetRelationType.Instrument == type_:
            return SynsetRelationType.Is_Instrument_of
        if SynsetRelationType.Is_Entailed_by == type_:
            return SynsetRelationType.Entailment
        if SynsetRelationType.Entailment == type_:
            return SynsetRelationType.Is_Entailed_by
        if SynsetRelationType.Location == type_:
            return SynsetRelationType.Is_Location_of
        if SynsetRelationType.Is_Location_of == type_:
            return SynsetRelationType.Location
        if SynsetRelationType.Has_Salient_defining_feature == type_:
            return SynsetRelationType.Salient_defining_feature
        if SynsetRelationType.Salient_defining_feature == type_:
            return SynsetRelationType.Has_Salient_defining_feature
        if SynsetRelationType.Is_Attribute_of == type_:
            return SynsetRelationType.Attribute
        if SynsetRelationType.Attribute == type_:
            return SynsetRelationType.Is_Attribute_of
        if SynsetRelationType.Unit == type_:
            return SynsetRelationType.Has_Unit
        if SynsetRelationType.Has_Unit == type_:
            return SynsetRelationType.Unit
        if SynsetRelationType.Is_Patient_of == type_:
            return SynsetRelationType.Patient
        if SynsetRelationType.Patient == type_:
            return SynsetRelationType.Is_Patient_of
        return type_

