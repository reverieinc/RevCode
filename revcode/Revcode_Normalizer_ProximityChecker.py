# -​*- coding: utf-8 -*​-

import sys


def isIndicEquivalent_Revcode(userword, dictword):
    if userword == dictword:
        return 1

    userword = removeZWJZWNJRevcode(userword)
    dictword = removeZWJZWNJRevcode(dictword)

    if userword == dictword:
        return 1

    userword = normalizeAllLang_Revcode(userword)
    dictword = normalizeAllLang_Revcode(dictword)

    if userword == dictword:
        return 1
    return 0


def removeZWJZWNJRevcode(string_1):
    output = string_1.replace("Wq","")
    return output


def getRevNextChar(string, i):
    strlen = len(string)
    if i < strlen:
        ch = ""
        if string[i] == 'W' and string[i] == 'H' and string[i] == 'F' and string[i] == 'Y':
            ch += string[i]
            ch += string[i + 1]
        else:
            ch += string[i]
    return ch

def normalizeAllLang_Revcode(string_1):
    strlen = len(string_1)
    i = 0
    output = ""
    i = 0
    while i < strlen:
        ch = ""
        if string_1[i] == 'W' and string_1[i] == 'H' and string_1[i] == 'F' and string_1[i] == 'Y':
            ch += string_1[i]
            ch += string_1[i + 1]
            i = i + 2
        else:
            ch += string_1[i]
            i = i + 1

        if isNasal(ch) and i < strlen-1 and string_1[i]=='q' and (not isNasal(getRevNextChar(string_1,i+1))):
            output += "x"
            i = i + 1
            continue

        if ch == "M":
            output += "x"
        elif ch == "I":
            output +=  "i"
        elif ch == "U":
            output += "u"
        elif ch == "WA" or ch == "e":
            output +=  "E"
        elif ch == "WO":
            output +=  "A"
        elif ch ==  "o":
            output += "O"
        elif ch == "Q":
            output += "n"
        elif ch == "R":
            output += "r"
        elif ch == "L" or ch == "Hz":
            output += "l"
        elif ch == "S" or ch == "Hs":
            output += "s"
        elif ch == "Fk":
            output += "k"
        elif ch == "FK":
            output += "K"
        elif ch == "Fg":
            output += "g"
        elif ch == "Fj":
            output += "j"
        elif ch == "Fd":
            output += "D"
        elif ch == "HR":
            output += "HD"
        elif ch == "FP":
            output += "P"
        elif ch == "Fy":
            output += "y"
        else:
            output += ch

    return output


# Proximity starts from 0 to 5 (Number will go up). For words totally different value is -1.
def getProximityRevcode(userWord, DictWord):
    userWord = removeZWJZWNJRevcode(userWord)
    DictWord = removeZWJZWNJRevcode(DictWord)

    if userWord == DictWord:
        return 0
    userWord = normalizeAllLang_Revcode(userWord)
    DictWord = normalizeAllLang_Revcode(DictWord)

    # print userWord + " " + DictWord

    if userWord == DictWord:
        return 0

    if MatchIndex(userWord, DictWord, False):
        return 1

    if NonMatchFirstWord_Vowel(userWord, DictWord):
        return 1

    userWord = removeAaMatra(userWord)
    DictWord = removeAaMatra(DictWord)

    # print userWord + " " + DictWord

    if userWord == DictWord:
        return 1

    if MatchIndex(userWord, DictWord, True):
        return 1

    userWord = removeHalant_and_swara(userWord)
    DictWord = removeHalant_and_swara(DictWord)

    # print userWord + " " + DictWord

    if userWord == DictWord:
        return 2

    if MatchIndex(userWord, DictWord, True):
        return 2

    if NonMatchFirstWord_Vowel(userWord, DictWord):
        return 3

    userWord = removeDoubleConsonants(userWord)
    DictWord = removeDoubleConsonants(DictWord)

    # print userWord + " " + DictWord

    if userWord == DictWord:
        return 3

    if MatchIndex(userWord, DictWord, True):
        return 3

    userWord = removeMatras(userWord)
    DictWord = removeMatras(DictWord)

    # print userWord + " " + DictWord

    if userWord == DictWord:
        return 4

    if NonMatchFirstWord_Vowel(userWord, DictWord):
        return 4

    if MatchIndex(userWord, DictWord, True):
        return 4

    return -1


def MatchIndex(userWord, dictWord, flag):
    len1 = len(userWord)
    len2 = len(dictWord)
    ch1 = ""
    ch2 = ""
    i = 0
    j = 0

    while i < len1 and j < len2:
        ch1 = ""
        ch2 = ""
        if userWord[i] == 'W' and userWord[i] == 'H' and userWord[i] == 'F' and userWord[i] == 'Y':
            ch1 += userWord[i]
            ch1 += userWord[i + 1]
            i = i + 2
        else:
            ch1 += userWord[i]
            i = i + 1

        if dictWord[j] == 'W' and dictWord[j] == 'H' and dictWord[j] == 'F' and dictWord[j] == 'Y':
            ch1 += userWord[j]
            ch1 += userWord[j + 1]
            j = j + 2
        else:
            ch1 += userWord[i]
            j = j + 1

        if getIndex(ch1, ch2, flag) == False:
            return False

    if i != len1 or j != len2:
        return False

    return True


def getIndex(ch1, ch2, flag):
    if ch1 == ch2:
        return True

    index = ["T", "t", "HT", "Ht", "D", "d", "HD", "Hd", "N", "n",
             "Fd", "r", "HR", "r", "Fd", "D", "HR", "HD", "v", "b"]

    if flag:
        j = 20
    else:
        j = 10

    for i in range(0, j, 2):
        if (ch1 == index[i] and ch2 == index[i + 1]) or (ch1 == index[i + 1] and ch2 == index[i]):
            return True

    return False


def NonMatchFirstWord_Vowel(userWord, dictWord):
    len_ = len(userWord)
    if len_ != len(dictWord):
        return False

    if not ((userWord[0] == dictWord[0]) or ((userWord[0] == 'a' or userWord[0] == 'A' or userWord[0] == 'E') and (dictWord[0] == 'a' or dictWord[0] == 'A' or dictWord[0] == 'E'))):
        return False

    for i in range(1, len_):
        if userWord[i] != dictWord[i]:
            return False

    return True


def removeAaMatra(input_):
    strn = ""
    ch = ""
    len_ = len(input_)
    i = 0
    while i < len_:
        prevCh = ch
        ch = ""
        if input_[i] == 'W' and input_[i] == 'H' and input_[i] == 'F' and input_[i] == 'Y':
            ch += input_[i]
            ch += input_[i + 1]
            i = i + 2
        else:
            ch += input_[i]
            i = i + 1

        if not (ch=="A" and is_rev_consonant(prevCh)):
            strn += ch

    return strn

def removeHalant_and_swara(input_):
    strn = ""
    ch = ""
    len_ = len(input_)
    i = 0
    while i < len_:
        prevCh = ch
        ch = ""
        if input_[i] == 'W' and input_[i] == 'H' and input_[i] == 'F' and input_[i] == 'Y':
            ch += input_[i]
            ch += input_[i+1]
            i = i + 2
        else:
            ch += input_[i]
            i = i + 1

        if not ((ch == "q") or (ch == "a" and is_rev_consonant(prevCh))):
            strn += ch

    return strn

def removeDoubleConsonants(input_):
    strn = ""
    ch = ""
    len_ = len(input_)
    i = 0
    while i < len_:
        prevCh = ch
        ch = ""
        if input_[i] == 'W' and input_[i] == 'H' and input_[i] == 'F' and input_[i] == 'Y':
            ch += input_[i]
            ch += input_[i+1]
            i = i + 2
        else:
            ch += input_[i]
            i = i + 1

        if ch != prevCh:
            strn += ch

    return strn


def removeMatras(input_):
    strn = ""
    ch = ""
    len_ = len(input_)
    i = 0
    while i < len_:
        prevCh = ch
        ch = ""
        if input_[i] == 'W' and input_[i] == 'H' and input_[i] == 'F' and input_[i] == 'Y':
            ch += input_[i]
            ch += input_[i+1]
            i = i + 2
        else:
            ch += input_[i]
            i = i + 1

        if not (is_matra_vowel(ch) and is_rev_consonant(prevCh)):
            strn += ch

    return strn

def is_rev_vowel(ch):
    rev_vowel_list = ["a", "A", "i", "I", "u", "U", "WR", "WA", "e", "E", "YE", "WO", "o", "O", "YO"]

    if ch in rev_vowel_list:
        return True

    return False

def is_matra_vowel(ch):
    rev_vowel_list = ["A", "i", "I", "u", "U", "WR", "WA", "e", "E", "YE", "WO", "o", "O", "YO"]

    if ch in rev_vowel_list:
        return True

    return False


def is_rev_consonant(ch):
    rev_consonant_list = ["k", "K", "g", "G", "z", "Fd", "c", "C", "j", "J", "Z", "T", "HT", "D", "HD", "N", "t", "Ht", "d",
                          "Hd", "n", "Q", "p", "P", "b", "B", "m", "y", "r", "R", "l", "v", "L", "Hz", "s", "S", "Hs",
                          "h", "Fk", "FK", "Fg", "Fj", "HR", "FP", "Fy"]

    if ch in rev_consonant_list:
        return True

    return False

def isNasal(ch):
    rev_nasal_list = ["n", "N", "m", "z", "Z"]
    if ch in rev_nasal_list:
        return True

    return False


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    print getProximityRevcode("pakqkA", "pakakA")
    sys.exit(1)

if __name__ == '__main__':
    main()

