class PhoneticForm:
    """
    Represents a phonetic form of a word.
    """

    def __init__(self, id, value):
        """
        Initializes a new instance of the PhoneticForm class.

        Args:
            id (int): The ID of the phonetic form.
            value (str): The phonetic representation of the word.
        """
        self.id = id
        self.value = value
