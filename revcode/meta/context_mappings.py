from meta import enums

CONTEXT_SENTENCE_TYPE_OLD = {

    "generic_address": enums.SentenceType.NounPhrase,
    "generic_city": enums.SentenceType.NounPhrase,
    "generic_industry": enums.SentenceType.NounPhrase,
    "generic_name": enums.SentenceType.NounPhrase,
    "jobs_category": enums.SentenceType.NounPhrase,
    "jobs_description": enums.SentenceType.Regular,
    "jobs_employer": enums.SentenceType.NounPhrase,
    "jobs_skills": enums.SentenceType.NounPhrase,
    "jobs_title": enums.SentenceType.NounPhrase,
    "jobs_name": enums.SentenceType.NounPhrase,
    "cta": enums.SentenceType.VerbPhrase,
    "movies_title": enums.SentenceType.NounPhrase,
    "movies_genre": enums.SentenceType.NounPhrase,
    "movies_plot": enums.SentenceType.Regular,
    "name_indian_": enums.SentenceType.NounPhrase,
    "name_indian_female": enums.SentenceType.NounPhrase,
    "name_indian_male": enums.SentenceType.NounPhrase,
    "retail_product_brand": enums.SentenceType.NounPhrase,
    "retail_product_breadcrumb": enums.SentenceType.NounPhrase,
    "retail_product_description": enums.SentenceType.Regular,
    "retail_product_name": enums.SentenceType.NounPhrase,
    "retail_product_producttype": enums.SentenceType.NounPhrase,
    "retail_product_subcategory": enums.SentenceType.NounPhrase,
    "retail_product_category": enums.SentenceType.NounPhrase,
    "generic_english_proper": enums.SentenceType.Regular,
    "generic_location": enums.SentenceType.NounPhrase,
    "generic_shortform": enums.SentenceType.NounPhrase,
    "generic_organization": enums.SentenceType.NounPhrase,
}

'''
generic_english_proper -- A (generic) well-formed Proper English sentence
generic_location -- A location, can be a city, town, country, locality
generic_shortform -- A term that is a short form for a longer term (abbreviation, SMS lingo, acronym)
generic_english_common -- A common English word (this is not really useful for you, but serves as a "negative class" during training)
generic_english_rare -- A rare English word (this is not really useful for you, but serves as a "negative class" during training)
generic_organization -- An organization name (company, bank, employer, service provider, etc)
'''

CONTEXT_SENTENCE_TYPE = {
    "address": enums.SentenceType.NounPhrase,
    "title": enums.SentenceType.NounPhrase,
    "description": enums.SentenceType.VerbPhrase,
}
