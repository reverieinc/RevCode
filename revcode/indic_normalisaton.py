# -*- coding: utf-8 -*-

SHORT_A = unichr(0x904)
A = unichr(0x905)
AA = unichr(0x906)
AI = unichr(0x910)
LETTER_CANDRA_O = unichr(0x911)
SHORT_O = unichr(0x912)
O = unichr(0x913)
AU = unichr(0x914)
CANDRA_E = unichr(0x90d)
SHORT_E = unichr(0x90e)
E = unichr(0x90f)
KA = unichr(0x915)
KHA = unichr(0x916)
GA = unichr(0x917)
JA = unichr(0x91c)
DDA = unichr(0x921)
DDHA = unichr(0x922)
NA = unichr(0x928)
NNAA = unichr(0x929)
PHA = unichr(0x92b)
YA = unichr(0x92f)
RA = unichr(0x930)
RRA = unichr(0x931)
LLLA = unichr(0x934)
LLA = unichr(0x933)
SIGN_NUKTA = unichr(0x93c)
SIGN_AA = unichr(0x93e)
SIGN_CANDRA_E = unichr(0x945)
SIGN_SHORT_E = unichr(0x946)
SIGN_E = unichr(0x947)
SIGN_AI = unichr(0x948)
SIGN_CANDRA_O = unichr(0x949)
SIGN_SHORT_O = unichr(0x94a)
SIGN_O = unichr(0x94b)
SIGN_AU = unichr(0x94c)
QA = unichr(0x958)
KHHA = unichr(0x959)
GHHA = unichr(0x95a)
ZA = unichr(0x95b)
DDDHA = unichr(0x95c)
RHA = unichr(0x95d)
FA = unichr(0x95e)
YYA = unichr(0x95f)
CANDRA_A = unichr(0x972)


def get_indic_normalized(input_):
    str_ = u""
    i = 0
    len_ = len(input_)

    while i < len_:

        if i < len_ - 2 and input_[i] == A and input_[i + 1] == SIGN_AA and input_[i + 2] == SIGN_CANDRA_E:
            str_ = ''.join([str_, LETTER_CANDRA_O])
            i += 3

        elif i < len_ - 2 and input_[i] == A and input_[i + 1] == SIGN_AA and input_[i + 2] == SIGN_SHORT_E:
            str_ = ''.join([str_, SHORT_O])
            i += 3

        elif i < len_ - 2 and input_[i] == A and input_[i + 1] == SIGN_AA and input_[i + 2] == SIGN_E:
            str_ = ''.join([str_, O])
            i += 3

        elif i < len_ - 2 and input_[i] == A and input_[i + 1] == SIGN_AA and input_[i + 2] == SIGN_AI:
            str_ = ''.join([str_, AU])
            i += 3

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_AA:
            str_ = ''.join([str_, AA])
            i += 2

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_CANDRA_E:
            str_ = ''.join([str_, CANDRA_A])
            i += 2

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_SHORT_E:
            str_ = ''.join([str_, SHORT_A])
            i += 2

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_CANDRA_O:
            str_ = ''.join([str_, LETTER_CANDRA_O])
            i += 2

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_SHORT_O:
            str_ = ''.join([str_, SHORT_O])
            i += 2

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_O:
            str_ = ''.join([str_, O])
            i += 2

        elif i < len_ - 1 and input_[i] == A and input_[i + 1] == SIGN_AU:
            str_ = ''.join([str_, AU])
            i += 2

        elif i < len_ - 1 and input_[i] == AA and input_[i + 1] == SIGN_CANDRA_E:
            str_ = ''.join([str_, LETTER_CANDRA_O])
            i += 2

        elif i < len_ - 1 and input_[i] == AA and input_[i + 1] == SIGN_SHORT_E:
            str_ = ''.join([str_, SHORT_O])
            i += 2

        elif i < len_ - 1 and input_[i] == AA and input_[i + 1] == SIGN_E:
            str_ = ''.join([str_, O])
            i += 2

        elif i < len_ - 1 and input_[i] == AA and input_[i + 1] == SIGN_AI:
            str_ = ''.join([str_, AU])
            i += 2

        elif i < len_ - 1 and input_[i] == E and input_[i + 1] == SIGN_CANDRA_E:
            str_ = ''.join([str_, CANDRA_E])
            i += 2

        elif i < len_ - 1 and input_[i] == E and input_[i + 1] == SIGN_SHORT_E:
            str_ = ''.join([str_, SHORT_E])
            i += 2

        elif i < len_ - 1 and input_[i] == E and input_[i + 1] == SIGN_E:
            str_ = ''.join([str_, AI])
            i += 2

        elif i < len_ - 1 and input_[i] == KA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, QA])
            i += 2

        elif i < len_ - 1 and input_[i] == KHA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, KHHA])
            i += 2

        elif i < len_ - 1 and input_[i] == GA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, GHHA])
            i += 2

        elif i < len_ - 1 and input_[i] == JA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, ZA])
            i += 2

        elif i < len_ - 1 and input_[i] == DDA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, DDDHA])
            i += 2

        elif i < len_ - 1 and input_[i] == DDHA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, RHA])
            i += 2

        elif i < len_ - 1 and input_[i] == NA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, NNAA])
            i += 2

        elif i < len_ - 1 and input_[i] == PHA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, FA])
            i += 2

        elif i < len_ - 1 and input_[i] == YA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, YYA])
            i += 2

        elif i < len_ - 1 and input_[i] == RA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, RRA])
            i += 2

        elif i < len_ - 1 and input_[i] == LLA and input_[i + 1] == SIGN_NUKTA:
            str_ = ''.join([str_, LLLA])
            i += 2

        elif i < len_ - 1 and input_[i] == SIGN_AA and input_[i + 1] == SIGN_CANDRA_E:
            str_ = ''.join([str_, SIGN_CANDRA_O])
            i += 2

        elif i < len_ - 1 and input_[i] == SIGN_AA and input_[i + 1] == SIGN_SHORT_E:
            str_ = ''.join([str_, SIGN_SHORT_O])
            i += 2

        elif i < len_ - 1 and input_[i] == SIGN_AA and input_[i + 1] == SIGN_E:
            str_ = ''.join([str_, SIGN_O])
            i += 2

        elif i < len_ - 1 and input_[i] == SIGN_AA and input_[i + 1] == SIGN_AI:
            str_ = ''.join([str_, SIGN_AU])
            i += 2
        else:
            str_ = ''.join([str_, input_[i]])
            i = i + 1

    return str_
