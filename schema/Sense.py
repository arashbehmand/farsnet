import farsnet
import farsnet.schema

class Sense(object):

    def __init__(self,
        id,
        seq_id,
        pos,
        default_value,
        word_id,
        default_phonetic,
        verb_transitivity,
        verb_active_passive,
        verb_type,
        synset,
        verb_past_stem,
        verb_present_stem,
        noun_category,
        noun_plural_type,
        pronoun,
        noun_numeral_type,
        adverb_type1,
        adverb_type2,
        pre_noun_adjective_type,
        adjective_type2,
        noun_specifity_type,
        noun_type,
        adjective_type1,
        is_causative,
        is_idiomatic,
        transitive_type,
        is_abbreviation,
        is_colloquial,
    ):
        self.id = id
        self.is_colloquial = is_colloquial
        self.is_abbreviation = is_abbreviation
        self.transitive_type = transitive_type
        self.is_idiomatic = is_idiomatic
        self.is_causative = is_causative
        self.adjective_type1 = adjective_type1
        self.noun_type = noun_type
        self.noun_specifity_type = noun_specifity_type
        self.adjective_type2 = adjective_type2
        self.pre_noun_adjective_type = pre_noun_adjective_type
        self.adverb_type1 = adverb_type1
        self.adverb_type2 = adverb_type2
        self.noun_numeral_type = noun_numeral_type
        self.pronoun = pronoun
        self.noun_plural_type = noun_plural_type
        self.noun_category = noun_category
        self.verb_past_stem = verb_past_stem
        self.verb_present_stem = verb_present_stem
        self.synset = synset
        self.verb_type = verb_type
        self.verb_active_passive = verb_active_passive
        self.verb_transitivity = verb_transitivity
        self.id = id
        self.seq_id = seq_id
        self.value = default_value
        self.word = farsnet.schema.Word(word_id, pos, default_phonetic, default_value)

    
    def get_synset(self):
        if self.synset != None and not self.synset == "":
            return farsnet.synset_service.get_synset_by_id(int(self.synset))
        return None

    def sense_relations(self, relation_type = None):
        if relation_type is None:
            return farsnet.sense_service.get_sense_relations_by_id(self.id)
        else:
            return farsnet.sense_service.get_sense_relations_by_type(self.id, relation_type)
        
