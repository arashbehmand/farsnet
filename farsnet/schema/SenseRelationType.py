from enum import Enum


class SenseRelationType(Enum):
    Antonym = "Antonym"
    Refer_to = "Refer_to"
    Is_Referred_by = "Is_Referred_by"
    Is_Non_Verbal_Part_of = "Is_Non_Verbal_Part_of"
    Non_Verbal_Part = "Non_Verbal_Part"
    Verbal_Part = "Verbal_Part"
    Is_Verbal_Part_of = "Is_Verbal_Part_of"
    Co_Occurrence = "Co_Occurrence"
    Derivationally_related_form = "Derivationally_related_form"
