def join_rev_matra(rev_word, rev_vowel):
    #   rev_vowel_list = ["a","A","i","I","u","U","WR","WA","e","E","YE","WO","o","O","YO","x","M","X"]
    #   rev_consonant_list = ["k","K","g","G","Fd","c","C","j","J","Z","T","HT","D","HD","N","t","Ht","d","Hd","n","Q","p","P","b","B","m","y","r","R","l","v","L","Hz","s","S","Hs","h","Fk","FK","Fg","Fj","HR","FP","Fy","z"]

    if len(rev_word) == 0 :
        return rev_vowel
    if rev_word[len(rev_word) - 1].lower() not in "abcdefghijklmnopqrstuvwxyz ":
        return rev_word

    if is_last_char_consonant(rev_word) and is_first_char_vowel(rev_vowel):
        if last_char_to_be_removed(rev_word):
            rev_word = rev_word[:-1]

    joined_rev_code = rev_word + rev_vowel

    return joined_rev_code


rev_vowel_list = ["a", "A", "i", "I", "u", "U", "WR", "WA", "e", "E", "YE", "WO", "o", "O", "YO", "x", "M", "X"]
rev_consonant_list = ["k", "K", "g", "G", "Fd", "c", "C", "j", "J", "Z", "T", "HT", "D", "HD", "N", "t", "Ht", "d",
                      "Hd", "n", "Q", "p", "P", "b", "B", "m", "y", "r", "R", "l", "v", "L", "Hz", "s", "S", "Hs", "h",
                      "Fk", "FK", "Fg", "Fj", "HR", "FP", "Fy", "z"]


def is_last_char_consonant(rev_str):
    if len(rev_str) > 1:

        last_ch = rev_str[len(rev_str) - 1]
        second_last_ch = rev_str[len(rev_str) - 2]
        last_two_chars = rev_str[-2:]

        if last_two_chars in rev_consonant_list:
            return True

        if last_ch == "a" and (second_last_ch in rev_consonant_list or last_two_chars in rev_consonant_list):
            return True

    last_ch = rev_str[-1:]
    if last_ch in rev_consonant_list:
        return True

    return False

def is_first_char_vowel(rev_str):
    first_char = rev_str[:1]
    if first_char in rev_vowel_list:
        return True

    if len(rev_str) > 1:
        first_two_char = rev_str[:2]
        if first_two_char in rev_vowel_list:
            return True

    return False


def is_last_char_matra(rev_str):

    if len(rev_str)<=1 :
        return False
    if len(rev_str) >= 2 :
        last_char = rev_str[-1:]

        if last_char == "a" :
            return False
        if last_char in rev_vowel_list and is_last_char_consonant(rev_str[:-1]) :
            return True

    return False


def last_char_to_be_removed(rev_str):
    if len(rev_str) > 1:
        last_ch = rev_str[-1:]
        if last_ch == "a":
            return True

    return False


# if __name__ == '__main__':
#     print join_rev_matra("kara", "tE")
