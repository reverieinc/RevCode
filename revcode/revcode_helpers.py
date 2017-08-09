def is_local_vowel(ch):
    ch = ch & 0x7f

    if ch >= 0x5 and ch <= 0x14:
        return True
    return False


def is_local_consonant(ch, consonant_flag=False):
    # if ch in u"XYZ~`!@#$%^&*()_-+={}[]:>;',</?*-+":
    #     return 0
    #
    # if ch in u"\"":
    #     return -1

    if(ch==0x9f0 or ch==0x9f1):
        return 1

    if ch == 0x200c:
       return -1
    
    ch = ch & 0x7f

    
    if ((ch >= 0x15 and ch <= 0x39) or (ch >= 0x58 and ch <= 0x5f)):
        return 1
    return 0


def is_local_matra(ch):
    ch = ord(ch) & 0x7f

    if (ch >= 0x3e and ch <= 0x4c):
        return True
    return False


def is_rev_vowel(ch):
    rev_vowel_list = ["a", "A", "i", "I", "u", "U", "WR", "WA", "e", "E", "YE", "WO", "o", "O", "YO"]  # "x","M","X"

    if ch in rev_vowel_list:
        return True

    return False


def is_rev_consonant(ch):
    rev_consonant_list = ["k", "K", "g", "G", "Fd", "c", "C", "j", "J", "Z", "T", "HT", "D", "HD", "N", "t", "Ht", "d",
                          "Hd", "n", "Q", "p", "P", "b", "B", "m", "y", "r", "R", "l", "v", "L", "Hz", "s", "S", "Hs",
                          "h", "Fk", "FK", "Fg", "Fj", "HR", "FP", "Fy", "z"]

    if ch in rev_consonant_list:
        return True

    return False


def in_indic(ch):
    return ch >= 0x900 and ch <= 0xD7F


def get_single_chars(rev_str) :
    """

    :param rev_str:
    :return: list of rev chars
    """

    double_letter_code = ["H", "F", "W", "Y"]

    i = 0
    rev_str_list =[]
    while i < len(rev_str):

        ch = rev_str[i]
        dict_key = ch
        if ch in double_letter_code:
            ch_next = rev_str[i + 1]
            dict_key = ch + ch_next
            i = i + 1
        i = i+1
        rev_str_list.append(dict_key)

    return rev_str_list

if __name__ == '__main__':
    get_single_chars("WarajaHztaFy")