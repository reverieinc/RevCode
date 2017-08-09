# -*- coding: utf-8 -*-
offset = 0x0C00

rev_code = {
    "M": 0xC01,  # ఁ
    "x": 0xC02,  # ం
    "X": 0xC03,  # ః
    "a": 0xC05,  # అ
    "A": 0xC06,  # ఆ
    "i": 0xC07,  # ఇ
    "I": 0xC08,  # ఈ
    "u": 0xC09,  # ఉ
    "U": 0xC0A,  # ఊ
    "WR": 0xC0B,  # ఋ
    "": 0xC0C,  # -
    "WA": 0xC0D,  # -
    "e": 0xC0E,  # ఎ
    "E": 0xC0F,  # ఏ
    "YE": 0xC10,  # ఐ
    "WO": 0xC11,  # -
    "o": 0xC12,  # ఒ
    "O": 0xC13,  # ఓ
    "YO": 0xC14,  # ఔ
    "k": 0xC15,  # క
    "K": 0xC16,  # ఖ
    "g": 0xC17,  # గ
    "G": 0xC18,  # ఘ
    "z": 0xC19,  # ఙ
    "c": 0xC1A,  # చ
    "C": 0xC1B,  # ఛ
    "j": 0xC1C,  # జ
    "J": 0xC1D,  # ఝ
    "Z": 0xC1E,  # ఞ
    "T": 0xC1F,  # ట
    "HT": 0xC20,  # ఠ
    "D": 0xC21,  # డ
    "HD": 0xC22,  # ఢ
    "N": 0xC23,  # ణ
    "t": 0xC24,  # త
    "Ht": 0xC25,  # థ
    "d": 0xC26,  # ద
    "Hd": 0xC27,  # ధ
    "n": 0xC28,  # న
    "Q": 0xC29,  # -
    "p": 0xC2A,  # ప
    "P": 0xC2B,  # ఫ
    "b": 0xC2C,  # బ
    "B": 0xC2D,  # భ
    "m": 0xC2E,  # మ
    "y": 0xC2F,  # య
    "r": 0xC30,  # ర
    "R": 0xC31,  # ఱ
    "l": 0xC32,  # ల
    "L": 0xC33,  # ళ
    "Hz": 0xC34,  # ఴ
    "v": 0xC35,  # వ
    "S": 0xC36,  # శ
    "Hs": 0xC37,  # ష
    "s": 0xC38,  # స
    "h": 0xC39,  # హ
    # "" : 0xC3C,  #
    # "" : 0xC3D,  # ఽ
    # "A" : 0xC3E,  # ా
    # "i" : 0xC3F,  # ి
    # "I" : 0xC40,  # ీ
    # "u" : 0xC41,  # ు
    # "U" : 0xC42,  # ూ
    # "WR" : 0xC43,  # ృ
    # "WA" : 0xC45,  # -
    # "e" : 0xC46,  # ె
    # "E" : 0xC47,  # ే
    # "YE" : 0xC48,  # ై
    # "WO" : 0xC49,  # -
    # "o" : 0xC4A,  # ొ
    # "O" : 0xC4B,  # ో
    # "YO" : 0xC4C,  # ౌ
    "q": 0xC4D,  # ్
    "Fk": 0xC58,  # ౘ
    "FK": 0xC59,  # ౙ
    "Fg": 0xC5A,  # ౚ
    "Fj": 0xC5B,  # -
    "Fd": 0xC5C,  # -
    "HR": 0xC5D,  # -
    "FP": 0xC5E,  # -
    "Fy": 0xC5F,  # -
    "Wq": 0x200c,  # NJ
}
