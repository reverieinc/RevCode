# -*- coding: utf-8 -*-

import revcode.indic_normalizer as indic_normalizer
from revcode import normalised_local_rev, normalised_rev_local

from revcode.revcode_helpers import (
    is_local_consonant,
    is_local_vowel,
    is_rev_consonant,
    is_rev_vowel,
    in_indic,
)

from revcode.mappings import (
    hindi_to_rev,
    rev_to_hindi,
)  # since default language, it needs import

IGNORE_LIST = "1234567890~`!@#$%^&*()_-+={}[]:>;',</?*-+.\""


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
    nukta = (0x093C & 0x00FF) + normalised_local_rev.offset

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

        if (
            consonant_flag == 1
            and (is_const == 1 or is_local_vowel(ch))
            and local_str[i - 1] != " "
        ):
            if ch != " ":
                rev_local_str = rev_local_str + "a"
                rev_local_str = rev_local_str + normalised_local_rev.rev_code.get(
                    ch, ""
                )

                if is_local_consonant(ch) == -1:
                    consonant_flag = consonant_flag
                else:
                    consonant_flag = is_local_consonant(ch)

        elif ch == nukta:
            consonant_flag = 1

        elif ch == halant:
            # if next char is a vowel add chr(0xA6) to local string
            if not consonant_flag or (
                consonant_flag
                and i < len(local_str) - 1
                and not is_local_consonant(ord(local_str[i + 1]))
            ):
                rev_local_str = rev_local_str + chr(0xA6)

            consonant_flag = 0

        else:
            rev_local_str = rev_local_str + normalised_local_rev.rev_code.get(
                ch, chr(ch)
            )

            if is_local_consonant(ch) == -1:
                consonant_flag = consonant_flag
            else:
                consonant_flag = is_local_consonant(ch)

        if consonant_flag == 1 and (
            (i < len(local_str) - 1 and local_str[i + 1] in [" "] and ch != " ")
            or (i == len(local_str) - 1)
        ):
            rev_local_str = rev_local_str + "a"
            is_const = 0

    final_rev_local_str += rev_local_str
    return final_rev_local_str


def convert_rev_to_local(rev_str, normalised_rev_local=rev_to_hindi):
    rev_str = rev_str.strip()
    double_letter_code = ["H", "F", "W", "Y"]
    local_str = ""
    halant = chr((0x094D & 0x00FF) + normalised_rev_local.offset)
    consonant_flag = False

    i = 0
    while i < len(rev_str):
        ch = rev_str[i]
        dict_key = ch
        if ch in double_letter_code:
            ch_next = rev_str[i + 1]
            dict_key = ch + ch_next
            i = i + 1

        if dict_key in IGNORE_LIST or dict_key == " " or dict_key == "\u200c":
            if consonant_flag:
                local_str = local_str + halant
            consonant_flag = False
        if normalised_rev_local.rev_code.get(dict_key) is not None:
            val = normalised_rev_local.rev_code.get(dict_key)
            val = chr(val)

            if dict_key == "a" and i != 0 and rev_str[i - 1] != " ":
                consonant_flag = False

            elif (
                consonant_flag
                and (is_rev_consonant(dict_key) or is_rev_vowel(dict_key))
                and rev_str[i - 1] != "  "
            ):
                if is_rev_consonant(dict_key):
                    local_str = local_str + halant
                    local_str = local_str + val
                    consonant_flag = is_rev_consonant(dict_key)

                elif is_rev_vowel(dict_key):
                    tmp_ch = val
                    tmp_ch = ord(tmp_ch) + 0x038
                    local_str = local_str + chr(tmp_ch)
                    consonant_flag = False
            else:
                local_str = local_str + val
                consonant_flag = is_rev_consonant(dict_key)
        else:
            consonant_flag = False
            val = normalised_rev_local.rev_code.get(dict_key, dict_key)
            # if val == 0xA then add halant else next line
            if val == chr(0xA6):
                local_str = local_str + halant
            else:
                local_str = local_str + val

        if (
            dict_key == "a"
            and i != 0
            and not is_rev_consonant(rev_str[i - 1])
            and rev_str[i - 1] != " "
        ):
            local_str = local_str + val
            consonant_flag = False
        i = i + 1

    if consonant_flag:
        local_str = local_str + halant

    return local_str
