# -*- coding: utf-8 -*-
offset = 0x0D00

rev_code = {
    0x0D01: "M",  #  -
    0x0D02: "x",  #  ം
    0x0D03: "X",  #  ഃ
    0x0D05: "a",  #  അ
    0x0D06: "A",  #  ആ
    0x0D07: "i",  #  ഇ
    0x0D08: "I",  #  ഈ
    0x0D09: "u",  #  ഉ
    0x0D0A: "U",  #  ഊ
    0x0D0B: "WR",  #  ഋ
    # : "WD", #  -
    # : "WA", #  -
    0x0D0E: "e",  #  എ
    0x0D0F: "E",  #  ഏ
    0x0D10: "YE",  #  ഐ
    # : "WO", #  -
    0x0D12: "o",  #  ഒ
    0x0D13: "O",  #  ഓ
    0x0D14: "YO",  #  ഔ
    0x0D15: "k",  #  ക
    0x0D16: "K",  #  ഖ
    0x0D17: "g",  #  ഗ
    0x0D18: "G",  #  ഘ
    0x0D19: "z",  #  ങ
    0x0D1A: "c",  #  ച
    0x0D1B: "C",  #  ഛ
    0x0D1C: "j",  #  ജ
    0x0D1D: "J",  #  ഝ
    0x0D1E: "Z",  #  ഞ
    0x0D1F: "T",  #  ട
    0x0D20: "HT",  #  ഠ
    0x0D21: "D",  #  ഡ
    0x0D22: "HD",  #  ഢ
    0x0D23: "N",  #  ണ
    0x0D24: "t",  #  ത
    0x0D25: "Ht",  #  ഥ
    0x0D26: "d",  #  ദ
    0x0D27: "Hd",  #  ധ
    0x0D28: "n",  #  ന
    # : "Q", #  -
    0x0D2A: "p",  #  പ
    0x0D2B: "P",  #  ഫ
    0x0D2C: "b",  #  ബ
    0x0D2D: "B",  #  ഭ
    0x0D2E: "m",  #  മ
    0x0D2F: "y",  #  യ
    0x0D30: "r",  #  ര
    0x0D31: "R",  #  റ
    0x0D32: "l",  #  ല
    0x0D33: "L",  #  ള
    0x0D34: "Hz",  #  ഴ
    0x0D35: "v",  #  വ
    0x0D36: "S",  #  ശ
    0x0D37: "Hs",  #  ഷ
    0x0D38: "s",  #  സ
    0x0D39: "h",  #  ഹ
    # : "", #
    # : "", #
    0x0D3E: "A",  #  ാ
    0x0D3F: "i",  #  ി
    0x0D40: "I",  #  ീ
    0x0D41: "u",  #  ു
    0x0D42: "U",  #  ൂ
    # : "WR", #
    # : "WA", #
    0x0D46: "e",  #  െ
    0x0D47: "E",  #  േ
    # : "YE", #  ൈ
    # : "WO", #
    0x0D4A: "o",  #  ൊ
    0x0D4B: "O",  #  ോ
    # : "YO", #
    # : "q", #  ്
    # : "Fk", #
    # : "FK", #
    # : "Fg", #
    # : "Fj", #
    # : "Fd", #
    0x0D43: "WR",  #  ൃ
    # : "FP", #
    # : "Fy", #
    # : "YN", #
    # : "HH", #
    # : "Yt", #
    0x0D7A: "HN",  #  ണ്‍
    0x0D7B: "Hn",  #  ന്‍
    0x0D7C: "Hr",  #  ര്‍
    0x0D7D: "HL",  #  ല്‍
    # : "", #
    0x0D7E: "Hl",  #  ള്‍
    0x0D7F: "Hk",  #  ക്‍
    0x0D48: "Ye",  #
    # : "", #
    # : "", #
    # : "", #
    0x200C: "WQ",  #
}
