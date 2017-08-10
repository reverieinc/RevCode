# -*- coding: utf-8 -*-

import codecs
import os

import  indic_normalizer
from revcode_helpers import is_local_consonant, is_local_vowel, is_rev_consonant, is_rev_vowel, in_indic

# global dictionaries
from mappings import hindi_to_rev, punjabi_to_rev, telugu_to_rev, tamil_to_rev, kannada_to_rev, gujarati_to_rev, oriya_to_rev, malayalam_to_rev, marathi_to_rev, bengali_to_rev, assamese_to_rev
from mappings import rev_to_hindi, rev_to_punjabi, rev_to_telugu, rev_to_tamil, rev_to_kannada,rev_to_gujarati,rev_to_assamese, rev_to_bengali, rev_to_malayalam, rev_to_oriya, rev_to_marathi
from meta.enums import Language
from mappings import language_mappings
from meta.language_mappings import TARGET_LANGUAGES

normalised_local_rev = {
    Language.Hindi: hindi_to_rev,
    Language.Punjabi: punjabi_to_rev,
    Language.Telugu: telugu_to_rev,
    Language.Tamil: tamil_to_rev,
    Language.Kannada: kannada_to_rev,
    Language.Gujarati: gujarati_to_rev,
    Language.Assamese : assamese_to_rev,
    Language.Bengali : bengali_to_rev,
    Language.Malayalam : malayalam_to_rev,
    Language.Marathi : marathi_to_rev,
    Language.Oriya : oriya_to_rev

}
normalised_rev_local = {
    Language.Hindi: rev_to_hindi,
    Language.Punjabi: rev_to_punjabi,
    Language.Telugu: rev_to_telugu,
    Language.Tamil: rev_to_tamil,
    Language.Kannada: rev_to_kannada,
    Language.Gujarati : rev_to_gujarati,
    Language.Assamese : rev_to_assamese,
    Language.Bengali : rev_to_bengali,
    Language.Malayalam : rev_to_malayalam,
    Language.Marathi : rev_to_marathi,
    Language.Oriya : rev_to_oriya
}

IGNORE_LIST = "~`!@#$%^&*()_-+={}[]:>;',</?*-+.\""


# Given local string and target language, returns revcoded string for that language
def to_revcode(local_str, language):
   global normalised_local_rev
   if language in normalised_local_rev:
       to_revcode_dict = normalised_local_rev[language]
       return convert_to_revcode(local_str, to_revcode_dict)
   else:
       raise KeyError("Local to RevCode map not found for specified language")


# Given revcoded string and target language, returns local string for that language
def from_revcode(rev_str, language):
    global normalised_rev_local
    if language in normalised_rev_local:
        from_revcode_dict = normalised_rev_local[language]
        return convert_rev_to_local(rev_str, from_revcode_dict)
    else:
        raise KeyError("RevCode to Local map not found for specified language")


def load_normalised_dict():
    global normalised_local_rev
    global normalised_rev_local
    normalised_local_rev = hindi_to_rev
    normalised_rev_local = rev_to_hindi


def convert_to_revcode(local_str, normalised_local_rev=hindi_to_rev):
    local_str = indic_normalizer.get_indic_normalized(local_str)

    final_rev_local_str = ""
    rev_local_str = ""
    consonant_flag = 0
    halant = (0x094D & 0x00FF) + normalised_local_rev.offset
    nukta = (0x093c & 0x00FF) + normalised_local_rev.offset

    local_str = local_str.strip()

    for i, ch in enumerate(list(local_str)):

        if not in_indic(ord(ch)):
            if i != 0 and is_const:
                rev_local_str = rev_local_str + "a"
            final_rev_local_str += rev_local_str + ch
            consonant_flag = 0
            is_const = 0
            rev_local_str = ""
            continue

        if ch == " ":
            rev_local_str = rev_local_str + " "
            consonant_flag = 0
            is_const = 0
            continue
        ch = ord(ch)

        if is_local_consonant(ch) == -1:
            is_const = 0
        else:
            is_const = is_local_consonant(ch)

        if consonant_flag == 1 and (is_const == 1 or is_local_vowel(ch)) and local_str[i - 1] != " ":
            if ch != " ":
                rev_local_str = rev_local_str + "a"
                rev_local_str = rev_local_str + normalised_local_rev.rev_code.get(ch, "")

                if is_local_consonant(ch) == -1:
                    consonant_flag = consonant_flag
                else:
                    consonant_flag = is_local_consonant(ch)

        elif ch == nukta:
            consonant_flag = 1
        elif ch == halant:
            consonant_flag = 0
        else:
            rev_local_str = rev_local_str + normalised_local_rev.rev_code.get(ch, unichr(ch))

            if is_local_consonant(ch) == -1:
                consonant_flag = consonant_flag
            else:
                consonant_flag = is_local_consonant(ch)

        if consonant_flag == 1 and ((i < len(local_str) - 1 and local_str[i + 1] in [' '] and ch != ' ') \
                                            or (i == len(local_str) - 1)):
            rev_local_str = rev_local_str + "a"
            is_const = 0

    final_rev_local_str += rev_local_str
    return final_rev_local_str


def convert_rev_to_local(rev_str, normalised_rev_local=rev_to_hindi):
    rev_str = rev_str.strip()

    double_letter_code = ["H", "F", "W", "Y"]
    local_str = u""
    halant = unichr((0x094D & 0x00FF) + normalised_rev_local.offset)
    consonant_flag = False

    i = 0
    while i < len(rev_str):

        ch = rev_str[i]
        dict_key = ch
        if ch in double_letter_code:
            ch_next = rev_str[i + 1]
            dict_key = ch + ch_next
            i = i + 1

        if dict_key in IGNORE_LIST or dict_key == ' ':
            if consonant_flag:
                local_str = local_str + halant
            consonant_flag = False
        if normalised_rev_local.rev_code.get(dict_key) is not None:
            val = normalised_rev_local.rev_code.get(dict_key)
            val = unichr(val)

            if (dict_key == "a" and i != 0 and rev_str[i - 1] != " "):
                consonant_flag = False

            elif (consonant_flag and (is_rev_consonant(dict_key) or is_rev_vowel(dict_key)) and rev_str[i - 1] != "  "):
                if is_rev_consonant(dict_key):
                    local_str = local_str + halant
                    local_str = local_str + val
                    consonant_flag = is_rev_consonant(dict_key)

                elif is_rev_vowel(dict_key):
                    tmp_ch = val
                    tmp_ch = ord(tmp_ch) + 0x038
                    local_str = local_str + unichr(tmp_ch)
                    consonant_flag = False
            else:
                local_str = local_str + val
                consonant_flag = is_rev_consonant(dict_key)
        else:
            consonant_flag = False
            val = normalised_rev_local.rev_code.get(dict_key, dict_key)
            local_str = local_str + val

        if (dict_key == "a" and i != 0 and not is_rev_consonant(rev_str[i - 1]) and rev_str[i - 1] != " "):
            local_str = local_str + val
            consonant_flag = False
        i = i + 1

    if consonant_flag:
        local_str = local_str + halant

    return local_str

# read a target language file
# ending with "_language.py" convert it to
# "_language_rev_code.py" in another rev_code folder at same level to src file .
def convert_py_file_to_rev(fnames):
    '''

    :param fnames: a list with file names 
    '''


    for fname in fnames:
        source_path = fname[0:fname.rfind("/")]
        target_path = source_path[:-15]+"rev_code/"
        source_file = fname[fname.rfind("/")+1:fname.rfind("_")]
        source_lang = fname[fname.rfind("_")+1:fname.rfind(".")]
        target_file = target_path + source_file +"_"+source_lang+ "_rev_code.py"

        with codecs.open(fname, "r", "utf-8") as fin, codecs.open(target_file,"w", "utf-8") as fout:
            for line in fin:
                line = line.strip()
                normalised_line = indic_normalizer.get_indic_normalized(line)
                src_lang = TARGET_LANGUAGES.get(source_lang)
                line = to_revcode(normalised_line,src_lang)
                fout.write(line + "\n")

    print "VOCAB REV_CODED"


# reads tsv file
# each tab corresponding to a language
def convert_vocab_tsv_file(fpath):
    '''
    :param file_path: path of tsv file
    :return: 
    '''
    if fpath.strip() == "":
        return
    target_file = fpath+"_rev"
    print target_file
    with codecs.open(fpath, "r", "utf-8") as fin, codecs.open(target_file, "w", "utf-8") as fout:
        for line in fin:
                line_t = line.split("\t")
                line_out = []

                for i in range(len(line_t)):

                    # for POS need to to append in file
                    if i < 1 :
                        line_out.append(line_t[i])
                    elif i>12 :
                        continue
                    # for SYNSET id and ENGLISH word
                    else :
                        src_lang = language_mappings.Language_TSV[i]
                        normalised_word = indic_normalizer.get_indic_normalized(line_t[i])
                        revcoded_word = to_revcode(normalised_word, src_lang)
                        line_out.append(revcoded_word)
                fout.write("\t".join(line_out)+"\n")
                print line_out

    print "VOCAB REV_CODED"


def convert_vocab_list(data_list):
    '''
    :param file_path: path of tsv file
    :return: 
    '''
    line_out = []
    for i in range(len(data_list)):

        # for POS need to to append in file
        if i < 1:
            line_out.append(data_list[i])
        elif i > 12:
            continue
        # for SYNSET id and ENGLISH word
        else:
            src_lang = language_mappings.Language_TSV_LIST[i]
            normalised_word = indic_normalizer.get_indic_normalized(data_list[i])
            revcoded_word = to_revcode(normalised_word, src_lang)
            line_out.append(revcoded_word)

    return line_out

# read a file , convert it to revcode
def convert_file_to_Rev():

    fnames_maps = [
        # "/Users/ankita/git/reflection-py/main/data/language_related_mappings/verb_suffix_mappings/verb_suffix_mappings_target_language/verb_suffix_structure_marathi.py"
         "/Users/ankita/git/reflection-py/main/data/language_related_mappings/preposition_mappings/preposition_mappings_target_language/preposition_mappings_marathi.py"
    ]

    for fname in fnames_maps:
        source_path = fname[0:fname.rfind("/")]
        target_path = source_path[:-15]+"rev_code/"
        source_file = fname[fname.rfind("/")+1:fname.rfind("_")]
        source_lang = fname[fname.rfind("_")+1:fname.rfind(".")]
        target_file = target_path + source_file +"_"+source_lang+ "_rev_code.py"

        with codecs.open(fname, "r", "utf-8") as fin, codecs.open(target_file, "w", "utf-8") as fout:
            for line in fin:
                line = line.strip()
                normalised_line = indic_normalizer.get_indic_normalized(line)
                src_lang = TARGET_LANGUAGES.get(source_lang)
                line = to_revcode(normalised_line,src_lang)
                fout.write(line + "\n")

    print "File REV_CODED",target_file
# read a target language file
# ending with "_language.py" convert it to
# "_language_rev_code.py"
def convert_language_file_to_rev(fname):
    '''
    :param fnames: a list with file names
    '''
    print fname
    if fname.strip() == "":
        return
    source_lang = fname[fname.rfind("_") + 1:fname.rfind(".")]
    # target_file = fname[0:fname.rfind(".")] + "_rev_code.py"

    grand_parent_dir = os.path.dirname(os.path.dirname(fname))
    rev_code_file_dir = "pronoun_mappings_rev_code"
    final_file_name = fname[fname.rfind("/")+1:fname.rfind(".")] + "_rev_code.py"
    target_file = "/".join([grand_parent_dir, rev_code_file_dir, final_file_name])


    with codecs.open(fname, "r", "utf-8") as fin, codecs.open(target_file, "w", "utf-8") as fout:
        for line in fin:
            line = line.strip()
            normalised_line = indic_normalizer.get_indic_normalized(line)
            src_lang = TARGET_LANGUAGES.get(source_lang)
            line = to_revcode(normalised_line, src_lang)
            fout.write(line + "\n")

    print "VOCAB REV_CODED",target_file


if __name__ == '__main__':


    local_str = u"तारीक  फ्लाइट  टिकट"

    print local_str

    rev_str = convert_to_revcode(indic_normalizer.get_indic_normalized(local_str), hindi_to_rev)

    print  rev_str

    local_returned = convert_rev_to_local(rev_str, rev_to_hindi)

    print local_returned

    if indic_normalizer.get_indic_normalized(local_str) == local_returned:
        print "True"
    else:
        print "False"

    # file conversions :

    # "_language.py" files : mapping files
    fnames = [


    ]
    # convert_py_file_to_rev(fnames)

    # SYNSET file , TSV files

    fapth = ""
    # convert_vocab_tsv_file(fapth)
    # convert_file_to_Rev()
    # language file
    # language file
