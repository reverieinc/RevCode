from enum import Enum


class Language(Enum):
    English = 0
    Hindi = 1
    Punjabi = 2
    Gujarati = 3
    Marathi = 4
    Kannada = 5
    Telugu = 6
    Tamil = 7
    Malayalam = 8
    Oriya = 9
    Bengali = 10
    Assamese = 11


class Fallback(Enum):
    Default = 1


class Animacy(Enum):
    Animate = 1
    Inanimate = 2


class Tense(Enum):
    Default = 0
    PresentIndefiniteTense = 1
    PresentContinuousTense = 2
    PresentPerfectTense = 3
    PresentPerfectContinuousTense = 4

    PastIndefiniteTense = 5
    PastContinuousTense = 6
    PastPerfectTense = 7
    PastPerfectContinuousTense = 8

    FutureIndefiniteTense = 9
    FutureContinuousTense = 10
    FuturePerfectTense = 11
    FuturePerfectContinuousTense = 12


class Voice(Enum):
    Active = 0
    Passive = 1


class Negation(Enum):
    Yes = 0
    No = 1

class Noun_Negate(Enum):
    Yes = 0
    No = 1

class Negate_Never(Enum):
    Yes = 0
    No = 1


class Interrogative(Enum):
    Yes = 0
    No = 1


class InterrogativeToken(Enum):
    Yes = 0
    No = 0


class ClauseMarker(Enum):
    Yes = 0
    No = 1


class ClauseDelimiter(Enum):
    Yes = 0
    No = 1


class NFClauseDelimiter(Enum):
    Yes = 0
    No = 1


class Gender(Enum):
    Masculine = 0
    Feminine = 1
    Neutral = 2


class Person(Enum):
    First = 0
    Second = 1
    Third = 2


class Case(Enum):
    Subjective = 0
    Objective = 1
    Possessive = 2


class Plurality(Enum):
    Singular = 0
    Plural = 1


class Participle(Enum):
    Present = 0
    Past = 1


class AuxVbForm(Enum):
    Yes = 0
    No = 1


class LastChar(Enum):
    default = 0
    AA = 1
    I = 2
    II = 3
    U = 4
    UU = 5
    vocalic_R = 6
    vocalic_RR = 7
    candra_E = 8
    short_E = 9
    E = 10
    AI = 11
    candra_O = 12
    short_O = 13
    O = 14
    AU = 15
    bindu = 16


class SentenceProperties(Enum):
    clause_Tense = 0
    clause_Voice = 1
    clause_aux_vb_form = 2
    clause_negate_form = 3
    clause_interrogative = 4
    clause_wh_word = 5


class VerbForm(Enum):
    Causative = 0
    Inchoative = 1


class WhWord(Enum):
    Yes = 0
    No = 1


class Rosetta_mask(Enum):
    Yes = 0
    No = 1


class Strategy(Enum): # This is to be used to know what to do with value in base_revcode
    RosettaMask = 0
    Unchanged = 1
    Transliterated = 2
    Dictionary = 3
    Removed = 4

class Status(Enum):
    MISSING_KEY = -5
    MALFORMED_JSON = -4
    TAG_NOT_MASKED = -3
    ROSETTA_ERROR = -2
    MT_ERROR = -1
    EMPTY_STRING = 0
    MT_SUCCESS = 1


class SentenceType(Enum):
    Regular = 0
    NounPhrase = 1
    VerbPhrase = 2
    Cta=3
    Address=4


class Domains(Enum):
    TEST = 0
    GENERIC = 1
    ECOMM = 3
    JOBS = 7
    ENTERTAINMENT = 4
    BANKING = 5
    TRAVEL = 9
    MAPS = 14


class ModalType(Enum):
    Ability = 1  # can, could
    Possibility = 2  # may, might
    Obligatory = 3  # should, must


class Transliterated(Enum):
    Yes = 0
    No = 1

class Tamil_verb_classes(Enum) :
    default = -1
    # Weak verbs
    class_1a = 0
    class_1b = 1
    class_1c = 2
    class_2 = 3
    class_3 = 4
    class_4 = 5
    # Strong Verbs
    class_6 = 6
    class_7 = 7
    # irregular verbs
    class_5 = 8
# verb_mappings from locMan DB
'''
1	General
2	Travel
3	Ecom
4	Music/Entertainment
5	Banking
6	Grocery
7	Education/Jobs
8	Medical
9	A2P
10	Test
11	Mobile Agent
12	Random Test
'''
