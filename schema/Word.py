import farsnet.schema

import farsnet


class Word(object):

    def __init__(self, id, pos, default_phonetic, default_value):
        self.id = id
        self.default_phonetic = default_phonetic
        self.default_value = default_value
        self.pos = pos

    def written_forms(self):
        return farsnet.sense_service.get_written_forms_by_word(self.id)

    def phonetic_forms(self):
        return farsnet.sense_service.get_phonetic_forms_by_word(self.id)
