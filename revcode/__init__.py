from revcode.meta.enums import Language
from revcode.mappings import assamese_to_rev, rev_to_assamese
from revcode.mappings import bengali_to_rev, rev_to_bengali
from revcode.mappings import gujarati_to_rev, rev_to_gujarati
from revcode.mappings import hindi_to_rev, rev_to_hindi
from revcode.mappings import kannada_to_rev, rev_to_kannada
from revcode.mappings import malayalam_to_rev, rev_to_malayalam
from revcode.mappings import marathi_to_rev, rev_to_marathi
from revcode.mappings import oriya_to_rev, rev_to_oriya
from revcode.mappings import punjabi_to_rev, rev_to_punjabi
from revcode.mappings import tamil_to_rev, rev_to_tamil
from revcode.mappings import telugu_to_rev, rev_to_telugu

normalised_local_rev = {
    Language.Hindi: hindi_to_rev,
    "hindi": hindi_to_rev,
    "hin": hindi_to_rev,
    "hi": hindi_to_rev,
    Language.Punjabi: punjabi_to_rev,
    "punjabi": punjabi_to_rev,
    "pun": punjabi_to_rev,
    "pa": punjabi_to_rev,
    Language.Telugu: telugu_to_rev,
    "telugu": telugu_to_rev,
    "tel": telugu_to_rev,
    "te": telugu_to_rev,
    Language.Tamil: tamil_to_rev,
    "tamil": tamil_to_rev,
    "tam": tamil_to_rev,
    "ta": tamil_to_rev,
    Language.Kannada: kannada_to_rev,
    "kannada": kannada_to_rev,
    "kan": kannada_to_rev,
    "kn": kannada_to_rev,
    Language.Gujarati: gujarati_to_rev,
    "gujarati": gujarati_to_rev,
    "guj": gujarati_to_rev,
    "gu": gujarati_to_rev,
    Language.Assamese: assamese_to_rev,
    "assamese": assamese_to_rev,
    "asa": assamese_to_rev,
    "as": assamese_to_rev,
    Language.Bengali: bengali_to_rev,
    "bengali": bengali_to_rev,
    "ben": bengali_to_rev,
    "bn": bengali_to_rev,
    Language.Malayalam: malayalam_to_rev,
    "malayalam": malayalam_to_rev,
    "mal": malayalam_to_rev,
    "ml": malayalam_to_rev,
    Language.Marathi: marathi_to_rev,
    "marathi": marathi_to_rev,
    "mar": marathi_to_rev,
    "mr": marathi_to_rev,
    Language.Oriya: oriya_to_rev,
    "oriya": oriya_to_rev,
    "odia": oriya_to_rev,
    "odi": oriya_to_rev,
    "or": oriya_to_rev,
}


normalised_rev_local = {
    Language.Hindi: rev_to_hindi,
    "hindi": rev_to_hindi,
    "hin": rev_to_hindi,
    "hi": rev_to_hindi,
    Language.Punjabi: rev_to_punjabi,
    "punjabi": rev_to_punjabi,
    "pun": rev_to_punjabi,
    "pa": rev_to_punjabi,
    Language.Telugu: rev_to_telugu,
    "telugu": rev_to_telugu,
    "tel": rev_to_telugu,
    "te": rev_to_telugu,
    Language.Tamil: rev_to_tamil,
    "tamil": rev_to_tamil,
    "tam": rev_to_tamil,
    "ta": rev_to_tamil,
    Language.Kannada: rev_to_kannada,
    "kannada": rev_to_kannada,
    "kan": rev_to_kannada,
    "kn": rev_to_kannada,
    Language.Gujarati: rev_to_gujarati,
    "gujarati": rev_to_gujarati,
    "guj": rev_to_gujarati,
    "gu": rev_to_gujarati,
    Language.Assamese: rev_to_assamese,
    "assamese": rev_to_assamese,
    "asa": rev_to_assamese,
    "as": rev_to_assamese,
    Language.Bengali: rev_to_bengali,
    "bengali": rev_to_bengali,
    "ben": rev_to_bengali,
    "bn": rev_to_bengali,
    Language.Malayalam: rev_to_malayalam,
    "malayalam": rev_to_malayalam,
    "mal": rev_to_malayalam,
    "ml": rev_to_malayalam,
    Language.Marathi: rev_to_marathi,
    "marathi": rev_to_marathi,
    "mar": rev_to_marathi,
    "mr": rev_to_marathi,
    Language.Oriya: rev_to_oriya,
    "oriya": rev_to_oriya,
    "odia": rev_to_oriya,
    "odi": rev_to_oriya,
    "or": rev_to_oriya,
}
