class Synset:
    """
    Represents a set of synonymous words (synset).
    """

    def __init__(
        self, id, pos, semantic_category, example, gloss, nofather, no_mapping
    ):
        self.id = id
        self.semantic_category = semantic_category
        self.nofather = nofather
        self.no_mapping = no_mapping
        self.pos = pos

    def examples(self):
        """
        Retrieves examples associated with this synset.

        Returns:
            list: A list of SynsetExample objects.
        """
        from farsnet.service import synset_service  # Import locally

        return synset_service.get_synset_examples(self.id)

    def glosses(self):
        """
        Retrieves glosses (definitions) associated with this synset.

        Returns:
            list: A list of SynsetGloss objects.
        """
        from farsnet.service import synset_service  # Import locally

        return synset_service.get_synset_glosses(self.id)

    def senses(self):
        """
        Retrieves the senses associated with this synset.

        Returns:
            list: A list of Sense objects.
        """
        from farsnet.service import sense_service  # Import locally

        return sense_service.get_senses_by_synset(self.id)

    def wordnet_synsets(self):
        """
        Retrieves the WordNet synsets associated with this synset.

        Returns:
            list: A list of WordNetSynset objects.
        """
        from farsnet.service import synset_service  # Import locally

        return synset_service.get_wordnet_synsets(self.id)

    def synset_relations(self, relation_type=None):
        """
        Retrieves synset relations associated with this synset.

        Args:
            relation_type (SynsetRelationType or list, optional): The type(s) of
                relations to retrieve. If None, retrieves all relations.

        Returns:
            list: A list of SynsetRelation objects.
        """
        from farsnet.service import synset_service  # Import locally

        if relation_type is None:
            return synset_service.get_synset_relations_by_id(self.id)
        if not isinstance(relation_type, list):
            relation_type = [relation_type]
        return synset_service.get_synset_relations_by_type(self.id, relation_type)
