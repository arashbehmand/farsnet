class SenseRelation:
    """
    Represents a relation between two senses.
    """

    def __init__(self, id, sense_id1, sense_id2, sense_word1, sense_word2, type_):
        self.id = id
        self.sense_id1 = sense_id1
        self.sense_id2 = sense_id2
        self.sense_word1 = sense_word1
        self.sense_word2 = sense_word2
        self.type_ = type_

    def sense1(self):
        """
        Retrieves the first sense in the relation.

        Returns:
            Sense: The first Sense object.
        """
        from farsnet.service import sense_service

        return sense_service.get_sense_by_id(self.sense_id1)

    def sense2(self):
        """
        Retrieves the second sense in the relation.

        Returns:
            Sense: The second Sense object.
        """
        from farsnet.service import sense_service  # Import locally

        return sense_service.get_sense_by_id(self.sense_id2)
