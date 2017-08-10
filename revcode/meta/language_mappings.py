from meta.enums import Language

# Keep verb_mappings only for languages which MT can produce output for

TARGET_LANGUAGES = {
    "hindi": Language.Hindi,
    "punjabi": Language.Punjabi,
    "kannada": Language.Kannada,
    "telugu": Language.Telugu,
    "tamil": Language.Tamil,
    "assamese" : Language.Assamese,
    "bengali" : Language.Bengali,
    "gujarati" : Language.Gujarati,
    "malayalam" : Language.Malayalam,
    "marathi" : Language.Marathi,
    "oriya" : Language.Oriya
}

DEFAULT_TARGET_LANGUAGES = [val for key, val in TARGET_LANGUAGES.iteritems()]

TARGET_LANGUAGES_STR = {
    Language.Hindi :"hindi",
    Language.Punjabi :  "punjabi",
    Language.Kannada : "kannada",
    Language.Telugu: "telugu" ,
    Language.Tamil:"tamil",
    Language.Malayalam : "malayalam",
    Language.Gujarati : "gujarati",
    Language.Marathi : "marathi",
    Language.Assamese : "assamese",
    Language.Oriya : "oriya",
    Language.Bengali : "bengali"
}

