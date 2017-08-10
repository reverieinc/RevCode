from meta import enums
from meta.enums import Tense, Person, Case, Plurality, Gender, Fallback

# POS

VERBS = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
VERBS_MODALS = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "MD"]

ALL_NOUNS = ["NN", "NNS", "NNP", "NNPS", "PRP", "PRP$", "WP", "WP$", "CD"]
PROPER_NOUNS = ["NNP", "NNPS"]
GENERAL_NOUNS = ["NN", "NNS"]
NOUNS = ["NN", "NNS", "NNP", "NNPS"]
NOUN_PLURALS = ["NNS", "NNPS"]

INTERROGATIVE_PRONOUNS = ["WP", "WP$"]
PRONOUNS = ["PRP", "PRP$", "WP", "WP$"]
ASSERT_PRONOUNS = ["PRP", "PRP$"]

ADJECTIVES = ["JJ", "JJR", "JJS"]

DETERMINERS = ["DT", "WDT", "PDT"]

ADVERBS = ["RB", "RBR", "RBS", "WRB", "RP"]
ASSERT_ADVERBS = ["RB", "RBR", "RBS"]

MODALS = ["MD"]

TO = ["TO"]

MODALS = ["MD"]

PREPOSITIONS = ["IN", "TO"]

DETERMINER = ["DT"]

CONJUNCTIONS = ["CC"]

POS = ["POS"]
EXISTENTIAL = ["EX"]

INTERROGATIVES = ["WDT", "WP", "WP$", "WRB"]
INTERROGATIVES_EXCEPT_DT = [ "WP", "WP$", "WRB"]
NUMERAL = ["CD"]
INTERJECTIONS = ["UH"]

FILE_VOCABS = ["PRP", "PRP$", "WDT", "WP", "WP$", "WRB", "IN", "TO", "MD"]
# Pronoun verb_mappings
# Review : ergative case

# Noun classification :
# Rosetta classification :
LOCALITY_TAGS = ["QQQTAGCOUNTRYTAGQQQ", "QQQTAGTOWNTAGQQQ", "QQQTAGCITYTAGQQQ", "QQQTAGLOCALITYTAGQQQ", "QQQTAGLOCATIONQQQ", "PLACE"]

PLACE = ["PLACE", "EVENT"]

PRONOUNS_MAPPINGS = {
    Fallback.Default: [Person.Third, Case.Subjective, Plurality.Singular, Gender.Neutral],
    # Assigned default as Subjective
    "i": [Person.First, Case.Subjective, Plurality.Singular, Gender.Masculine],
    "we": [Person.First, Case.Subjective, Plurality.Plural, Gender.Masculine],
    "me": [Person.First, Case.Objective, Plurality.Singular, Gender.Masculine],
    "us": [Person.First, Case.Objective, Plurality.Plural, Gender.Masculine],
    "my": [Person.First, Case.Possessive, Plurality.Singular, Gender.Masculine],
    "mine": [Person.First, Case.Possessive, Plurality.Singular, Gender.Masculine],
    "our": [Person.First, Case.Possessive, Plurality.Plural, Gender.Masculine],
    "ours": [Person.First, Case.Possessive, Plurality.Plural, Gender.Masculine],
    "you": [Person.Second, Case.Subjective, Plurality.Plural, Gender.Masculine],
    "your": [Person.Second, Case.Possessive, Plurality.Singular, Gender.Masculine],
    "yours": [Person.Second, Case.Possessive, Plurality.Plural, Gender.Masculine],
    "he": [Person.Third, Case.Subjective, Plurality.Singular, Gender.Masculine],
    "she": [Person.Third, Case.Subjective, Plurality.Singular, Gender.Feminine],
    "they": [Person.Third, Case.Subjective, Plurality.Plural, Gender.Masculine],
    "him": [Person.Third, Case.Objective, Plurality.Singular, Gender.Masculine],
    "her": [Person.Third, Case.Objective, Plurality.Singular, Gender.Feminine],
    "them": [Person.Third, Case.Objective, Plurality.Plural, Gender.Masculine],
    "his": [Person.Third, Case.Possessive, Plurality.Singular, Gender.Masculine],
    "hers": [Person.Third, Case.Possessive, Plurality.Singular, Gender.Feminine],
    "their": [Person.Third, Case.Possessive, Plurality.Plural, Gender.Masculine],
    "theirs": [Person.Third, Case.Possessive, Plurality.Plural, Gender.Masculine],
    "it": [Person.Third, Case.Subjective, Plurality.Singular, Gender.Neutral],
    "its": [Person.Third, Case.Possessive, Plurality.Singular, Gender.Masculine],
    "himself": [Person.First, Case.Subjective, Plurality.Singular, Gender.Masculine],
    "herself": [Person.First, Case.Subjective, Plurality.Singular, Gender.Feminine],
    "yourself": [Person.Second, Case.Subjective, Plurality.Plural, Gender.Masculine],
    "yourselves": [Person.Second, Case.Subjective, Plurality.Plural, Gender.Masculine],
    "itself": [Person.Third, Case.Subjective, Plurality.Singular, Gender.Neutral],
    "myself": [Person.First, Case.Subjective, Plurality.Singular, Gender.Masculine],
    "ourselves": [Person.First, Case.Possessive, Plurality.Plural, Gender.Masculine],
    "themselves": [Person.Third, Case.Objective, Plurality.Plural, Gender.Masculine]
}

FIRST_PERSON_PRP = ["i", "we", "me", "us", "my", "mine", "our", "ours", "himself", "herself", "ourselves"]

# Tense verb_mappings

TENSE_MAPPINGS_PASSIVE = {

    # ----------- Present ------------
    "VBZ:VBN": Tense.PresentIndefiniteTense,  # is eaten
    "VBN:VBZ": Tense.PresentIndefiniteTense,  # is eaten
    "VBP:VBN": Tense.PresentIndefiniteTense,  # are eaten
    # "VB:VBN": Tense.PresentIndefiniteTense, instructional sentence

    "VBZ:VBG:VBN": Tense.PresentContinuousTense,  # is being eaten
    "VB:VBG:VBN": Tense.PresentContinuousTense,  # check
    "VBP:VBG:VBN": Tense.PresentContinuousTense,  # are being eaten

    "VB:VBN": Tense.PresentPerfectTense,  # check
    "VBN:VB": Tense.PresentPerfectTense,  # check
    # "VB:VBN:VBN": Tense.PresentPerfectTense, considered for instructional be eaten
    "VBZ:VBN:VBN": Tense.PresentPerfectTense,  # has been eaten
    "VBP:VBN:VBN": Tense.PresentPerfectTense,  # have been eaten

    "VBP:VBN:VBG": Tense.PresentPerfectContinuousTense,  # check occurrence
    "VBZ:VBN:VBG": Tense.PresentPerfectContinuousTense,  # active
    "VB:VBN:VBG": Tense.PresentPerfectContinuousTense,  # active

    # --------- Past Tense -------------

    "VBD:VBN": Tense.PastIndefiniteTense,  # was eaten
    "VBN:VBD": Tense.PastIndefiniteTense,  # was eaten

    "VBD:VBG:VBN": Tense.PastContinuousTense,  # was being eaten

    "VBD:VBN:VBN": Tense.PastPerfectTense,  # had been  eaten

    "VBD:VBN:VBG": Tense.PastPerfectContinuousTense,  # active has been doing

    # -------- Modals -------------------

    "CAN:VB:VBN": Tense.PresentIndefiniteTense,  # can be eaten
    "COULD:VB:VBN": Tense.PresentIndefiniteTense,  # could be eaten
    "WILL:VB:VBN": Tense.FutureIndefiniteTense,  # will be eaten
    "WOULD:VB:VBN": Tense.FutureIndefiniteTense,  # would be eaten
    "SHALL:VB:VBN": Tense.FutureIndefiniteTense,  # shall be eaten
    "SHOULD:VB:VBN": Tense.FutureIndefiniteTense,  # should be eaten
    "MAY:VB:VBN": Tense.FutureIndefiniteTense,
    "MIGHT:VB:VBN": Tense.FutureIndefiniteTense,
    "MUST:VB:VBN": Tense.FutureIndefiniteTense,

    "CAN:VB:VBN:VBN": Tense.PresentIndefiniteTense,  # can have been eaten
    "COULD:VB:VBN:VBN": Tense.PresentIndefiniteTense,  # could have been eaten
    "WILL:VB:VBN:VBN": Tense.FuturePerfectTense,  # will have been eaten
    "WOULD:VB:VBN:VBN": Tense.FuturePerfectTense,
    "SHALL:VB:VBN:VBN": Tense.FuturePerfectTense,
    "SHOULD:VB:VBN:VBN": Tense.FuturePerfectTense,
    "MAY:VB:VBN:VBN": Tense.FuturePerfectTense,
    "MIGHT:VB:VBN:VBN": Tense.FuturePerfectTense,
    "MUST:VB:VBN:VBN": Tense.FuturePerfectTense,

    "VBZ:VB:VBG:VBN": Tense.PresentPerfectContinuousTense,  # does enjoy being bathed
    "CAN:VB:VBG:VBN": Tense.FutureContinuousTense,  # can be eaten
    "COULD:VB:VBG:VBN": Tense.FutureContinuousTense,  # could be eaten
    "WILL:VB:VBG:VBN": Tense.FutureContinuousTense,  # will be eaten
    "WOULD:VB:VBG:VBN": Tense.FutureContinuousTense,  # would be eaten
    "SHALL:VB:VBG:VBN": Tense.FutureContinuousTense,  # shall be eaten
    "SHOULD:VB:VBG:VBN": Tense.FutureContinuousTense,  # should be eaten
    "MAY:VB:VBG:VBN": Tense.FutureContinuousTense,
    "MIGHT:VB:VBG:VBN": Tense.FutureContinuousTense,
    "MUST:VB:VBG:VBN": Tense.FutureContinuousTense,

    "CAN:VB:VBN:VBG:VBN": Tense.PresentPerfectContinuousTense,  # can have been being eaten
    "COULD:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,  # could have been being eaten
    "WILL:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,  # will have been being  eaten
    "WOULD:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,
    "SHALL:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,
    "SHOULD:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,
    "MAY:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,
    "MIGHT:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,
    "MUST:VB:VBN:VBG:VBN": Tense.FuturePerfectContinuousTense,

    # -----------------------------------------------

}

TENSE_MAPPINGS_ACTIVE = {

    # ---------------- Default ----------------------
    "VB": Tense.Default,  # Book now
    "VB:VB": Tense.Default,  # check
    # ---------------- PRESENT -----------------------

    "VBP": Tense.PresentIndefiniteTense,  # We do
    "VBZ": Tense.PresentIndefiniteTense,  # He does
    "VBZ:VB": Tense.PresentIndefiniteTense,  # He does play
    "VBP:VB": Tense.PresentIndefiniteTense,  # We do play

    "VB:VBG": Tense.PresentContinuousTense,  # be doing
    "VBP:VBG": Tense.PresentContinuousTense,  # are doing
    "VBZ:VBG": Tense.PresentContinuousTense,  # were doing
    "VB:VBG:VBN": Tense.PresentContinuousTense,  # check

    "VB:VBN": Tense.PresentPerfectTense,  # check
    "VBP:VBN": Tense.PresentPerfectTense,  # have eaten
    "VBZ:VBN": Tense.PresentPerfectTense,  # has eaten
    # "VB:VBN:VBN": Tense.PresentPerfectTense,     have been eaten  PASSIVE

    "VB:VBN:VBG": Tense.PresentPerfectContinuousTense,  # be been eating check
    "VBP:VBN:VBG": Tense.PresentPerfectContinuousTense,  # have been eating
    "VBZ:VBN:VBG": Tense.PresentPerfectContinuousTense,  # has been eating

    # ----------------- PAST -----------------------

    "VBD": Tense.PastIndefiniteTense,  # played
    "VBN": Tense.PastIndefiniteTense,  # check
    "VBD:VB": Tense.PastIndefiniteTense,  # no chance check

    "VBD:VBG": Tense.PastContinuousTense,  # was doing

    "VBD:VBN": Tense.PastPerfectTense,  # had done

    "VBD:VBN:VBG": Tense.PastPerfectContinuousTense,  # had been doing

    # --------------- WITH MODALS -------------------

    "CAN:VB": Tense.PresentIndefiniteTense,  # can do
    "COULD:VB": Tense.PastIndefiniteTense,  # could do

    "WILL:VB": Tense.FutureIndefiniteTense,
    "WOULD:VB": Tense.FutureIndefiniteTense,
    "SHALL:VB": Tense.FutureIndefiniteTense,
    "SHOULD:VB": Tense.FutureIndefiniteTense,

    "MAY:VB": Tense.FutureIndefiniteTense,
    "MIGHT:VB": Tense.FutureIndefiniteTense,
    "MUST:VB": Tense.FutureIndefiniteTense,

    # -----------------------------------------------

    "CAN:VB:VBG": Tense.FutureContinuousTense,  # Ambig with past  # be doing
    "COULD:VB:VBG": Tense.FutureContinuousTense,  # Ambig with past

    "WILL:VB:VBG": Tense.FutureContinuousTense,
    "WOULD:VB:VBG": Tense.FutureContinuousTense,
    "SHALL:VB:VBG": Tense.FutureContinuousTense,
    "SHOULD:VB:VBG": Tense.FutureContinuousTense,

    "MAY:VB:VBG": Tense.FutureContinuousTense,
    "MIGHT:VB:VBG": Tense.FutureContinuousTense,
    "MUST:VB:VBG": Tense.FutureContinuousTense,

    # ------------------------------------------------

    "COULD:VB:VBN": Tense.PastPerfectTense,  # could be done  check passive

    "WILL:VB:VBN": Tense.FuturePerfectTense,
    "WOULD:VB:VBN": Tense.PastPerfectTense,
    "SHALL:VB:VBN": Tense.FuturePerfectTense,
    "SHOULD:VB:VBN": Tense.PastPerfectTense,

    "MAY:VB:VBN": Tense.PastPerfectTense,
    "MIGHT:VB:VBN": Tense.PastPerfectTense,
    "MUST:VB:VBN": Tense.PastPerfectTense,

    # -------------------------------------------------



    "COULD:VB:VBN:VBG": Tense.PastPerfectContinuousTense,  # could have being doing

    "WILL:VB:VBN:VBG": Tense.FuturePerfectContinuousTense,
    "WOULD:VB:VBN:VBG": Tense.PastPerfectContinuousTense,
    "SHALL:VB:VBN:VBG": Tense.FuturePerfectContinuousTense,
    "SHOULD:VB:VBN:VBG": Tense.PastPerfectContinuousTense,

    "MAY:VB:VBN:VBG": Tense.PastPerfectContinuousTense,
    "MIGHT:VB:VBN:VBG": Tense.PastPerfectContinuousTense,
    "MUST:VB:VBN:VBG": Tense.PastPerfectContinuousTense

}

"""
mapping all tags under one category to a single key
"""

tags_dict = {}
for __tag in VERBS:
    tags_dict[__tag] = 'vw'
for __tag in ALL_NOUNS:
    tags_dict[__tag] = 'nn'
for __tag in ADJECTIVES:
    tags_dict[__tag] = 'adj'
for __tag in ADVERBS:
    tags_dict[__tag] = 'adv'
for __tag in PREPOSITIONS:
    tags_dict[__tag] = 'prep'
for __tag in DETERMINERS:
    tags_dict[__tag] = 'adj'
for __tag in CONJUNCTIONS:
    tags_dict[__tag] = 'cc'
for __tag in INTERROGATIVES:
    tags_dict[__tag] = 'wh'

LOCMAN_TAGS = {

    "QQQTAGCOPMANYNAMETAGQQQ": ("NNP","T13N"),
    "QQQTAGBRANDTAGQQQ": ("NNP","T13N"),
    "QQQTAGEMPLOYERTAGQQQ": ("NNP","T13N"),
    "QQQTAGCOMPANYTAGQQQ": ("NNP","T13N"),
    "QQQTAGPRODUCTTYPETAGQQQ": ("NNP","T13N"),
    "QQQTAGLOCALITYTAGQQQ": ("NNP","T13N"),
    "QQQTAGLOCATIONTAGQQQ": ("NNP","T13N"),
    "QQQTAGSUBCATEGORYTAGQQQ": ("NNP","T13N"),
    "QQQTAGCATEGORYTAGQQQ": ("NNP","T13N"),
    "QQQTAGCITYTAGQQQ": ("NNP","T13N"),
    "QQQTAGTOWNTAGQQQ": ("NNP","T13N"),
    "QQQTAGSALARYTAGQQQ": ("CD","UN"),
    "QQQTAGCOUNTRYTAGQQQ": ("NNP","UN"),
    "QQQTAGRETAILSTORETAGQQQ": ("NNP","UN"),
    "QQQTAGBANKTAGQQQ": ("NNP","T13N"),
    "QQQTAGBANKINGTERMTAGQQQ": ("NNP","T13N"),
    "QQQTAGCOMMONTECHNICALTERMTAGQQQ": ("NNP","T13N"),
    "QQQTAGSERVICEPROVIDERTAGQQQ": ("NNP","T13N"),
    "QQQTAGAIRPORTTAGQQQ": ("NNP","UN"),
    "QQQTAGRESTAURANTTAGQQQ": ("NNP","T13N"),
    "QQQTAGAIRLINETAGQQQ": ("NNP","T13N"),
    "QQQTAGINDUSTRYTAGQQQ": ("NNP","T13N"),
    "QQQTAGALNUMTAGQQQ": ("NNP","UN"),
    "QQQTAGQUANTITYTAGQQQ": ("NNP","UN"),
    "QQQTAGAMOUNTTAGQQQ": ("CD","UN"),
    "QQQTAGTIMETAGQQQ": ("NNP","UN"),
    "QQQTAGTIMEZONETAGQQQ": ("NNP","UN"),
    "QQQTAGDATETAGQQQ": ("NNP","UN"),
    "QQQTAGDATETIMETAGQQQ": ("NNP","UN"),
    "QQQTAGPHONENUMBERTAGQQQ": ("NNP","UN"),
    "QQQTAGURLTAGQQQ": ("NNP","UN"),
    "QQQTAGEMAILIDTAGQQQ": ("NNP","UN"),
    "QQQTAGHASHTAGTAGQQQ": ("NNP","UN"),
    "QQQTAGACCOUNTNUMBERTAGQQQ": ("NNP","UN"),
    "QQQTAGCODETAGQQQ": ("NNP","UN"),
    "QQQTAGPERCENTTAGQQQ": ("CD","UN"),
    "QQQTAGNUMBERTAGQQQ": ("CD","UN"),
    "QQQTAGSPLHYPHENATEDTERMTAGQQQ": ("NNP","T13N"),
    "QQQTAGCOMPANYNAMETAGQQQ": ("NNP","T13N"),
    "QQQTAGNAMEDENTITYTAGQQQ": ("NNP","T13N"),
    "QQQTAGNDWTAGQQQ": ("NNP","T13N"),
    "QQQTAGGENRETAGQQQ": ("NNP","T13N"),
    "QQQTAGACTORTAGQQQ": ("NNP","T13N"),
    "QQQTAGDIRECTORTAGQQQ": ("NNP","T13N"),
    "QQQTAGWRITERTAGQQQ": ("NNP","T13N"),
    "QQQTAGTITLETAGQQQ": ("NNP","T13N"),
    "QQQTAGSOURCETAGQQQ": ("NNP","T13N"),
}

TRANSLITERATED_TAGS = {
    "QQQTAGBRANDTAGQQQ": "NNP",
    "QQQTAGEMPLOYERTAGQQQ": "NNP",
    "QQQTAGCOMPANYTAGQQQ": "NNP",
    "QQQTAGLOCALITYTAGQQQ": "NNP",
    "QQQTAGLOCATIONTAGQQQ": "NNP",
    "QQQTAGSUBCATEGORYTAGQQQ": "NNP",
    "QQQTAGCITYTAGQQQ": "NNP",
    "QQQTAGTOWNTAGQQQ": "NNP",
    "QQQTAGCOUNTRYTAGQQQ": "NNP",
    "QQQTAGRETAILSTORETAGQQQ": "NNP",
    "QQQTAGBANKINGTERMTAGQQQ": "NNP",
    "QQQTAGSERVICEPROVIDERTAGQQQ": "NNP",
    "QQQTAGRESTAURANTTAGQQQ": "NNP",
    "QQQTAGAIRLINETAGQQQ": "NNP",
    "QQQTAGINDUSTRYTAGQQQ": "NNP",
    "QQQTAGSPLHYPHENATEDTERMTAGQQQ": "NNP",
    "QQQTAGCOMPANYNAMETAGQQQ": "NNP",
    "QQQTAGNAMEDENTITYTAGQQQ": "NNP",
    "QQQTAGNDWTAGQQQ": "NNP",
    "QQQTAGGENRETAGQQQ": "NNP",
    "QQQTAGACTORTAGQQQ": "NNP",
    "QQQTAGDIRECTORTAGQQQ": "NNP",
    "QQQTAGWRITERTAGQQQ": "NNP",
    "QQQTAGTITLETAGQQQ": "NNP",
    "QQQTAGSOURCETAGQQQ": "NNP",

}

UNCHANGED_TAGS = {
    "QQQTAGSALARYTAGQQQ": "CD",
    "QQQTAGAIRPORTTAGQQQ": "NNP",
    "QQQTAGALNUMTAGQQQ": "NNP",
    "QQQTAGQUANTITYTAGQQQ": "NNP",
    "QQQTAGAMOUNTTAGQQQ": "CD",
    "QQQTAGTIMETAGQQQ": "NNP",
    "QQQTAGTIMEZONETAGQQQ": "NNP",
    "QQQTAGDATETAGQQQ": "NNP",
    "QQQTAGDATETIMETAGQQQ": "NNP",
    "QQQTAGPHONENUMBERTAGQQQ": "NNP",
    "QQQTAGURLTAGQQQ": "NNP",
    "QQQTAGEMAILIDTAGQQQ": "NNP",
    "QQQTAGHASHTAGTAGQQQ": "NNP",
    "QQQTAGACCOUNTNUMBERTAGQQQ": "NNP",
    "QQQTAGCODETAGQQQ": "NNP",
    "QQQTAGPERCENTTAGQQQ": "CD",
    "QQQTAGNUMBERTAGQQQ": "CD",
}
TRANSLATED_TAG = {
    "QQQTAGPRODUCTTYPETAGQQQ": "NNP",
    "QQQTAGCATEGORYTAGQQQ": "NNP",
    "QQQTAGCOMMONTECHNICALTERMTAGQQQ": "NNP",
    "QQQTAGBANKTAGQQQ": "NNP",
}

STRATEGY_MAP = {

}

DEFALUT_ROSETTA_TAG = "QQQTAGNAMEDENTITYTAGQQQ"

RESPECT_LIST = ["father", "mother", "grandfather", "grand father", "grandmother", "grand mother", "father of nation",
                "everybody", "everyone", "prime minister", "team"]

INDEFINITE_TENSES = [enums.Tense.PastIndefiniteTense,
                     enums.Tense.PresentIndefiniteTense,
                     enums.Tense.FutureIndefiniteTense]

CONTINUOUS_TENSES = [enums.Tense.PresentContinuousTense,
                     enums.Tense.PastContinuousTense,
                     enums.Tense.FutureContinuousTense]

PERFECT_TENSES = [enums.Tense.PresentPerfectTense,
                  enums.Tense.PastPerfectTense,
                  enums.Tense.FuturePerfectTense]

PERFECT_CONTINUOUS_TENSES = [enums.Tense.PastPerfectContinuousTense,
                             enums.Tense.PresentPerfectContinuousTense,
                             enums.Tense.FuturePerfectContinuousTense]

PRESENT_TENSES = [enums.Tense.PresentIndefiniteTense,
                  enums.Tense.PresentContinuousTense,
                  enums.Tense.PresentPerfectTense,
                  enums.Tense.PresentPerfectContinuousTense]

PAST_TENSES = [enums.Tense.PastIndefiniteTense,
               enums.Tense.PastContinuousTense,
               enums.Tense.PastPerfectTense,
               enums.Tense.PastPerfectContinuousTense]

FUTURE_TENSES = [enums.Tense.FutureIndefiniteTense,
                 enums.Tense.FutureContinuousTense,
                 enums.Tense.FuturePerfectTense,
                 enums.Tense.FuturePerfectContinuousTense]

MODAL_TYPE_MAPPINGS = {
    "can": enums.ModalType.Ability,
    "could": enums.ModalType.Ability,
    "may": enums.ModalType.Possibility,
    "might": enums.ModalType.Possibility,
    "should": enums.ModalType.Obligatory,
    "must": enums.ModalType.Obligatory
}

Language_offset = {
    enums.Language.Hindi: 0x0900,
    enums.Language.Punjabi: 0x0A00,
    enums.Language.Telugu: 0x0C00,
    enums.Language.Kannada: 0x0C80
}

NEUTRAL_MAPPINGS = {
    enums.Language.Hindi: Gender.Masculine,
    enums.Language.Telugu: Gender.Feminine,
    enums.Language.Punjabi: Gender.Masculine,
    enums.Language.Kannada: Gender.Neutral
}

DOMAIN_TO_T13N = {
    enums.Domains.MAPS: 9,
    enums.Domains.TRAVEL: 9,
    enums.Domains.GENERIC: 4
}
