# -*- coding: utf-8 -*-


def get_indic_normalized(in_str):
    out_str = ""
    i = 0
    length = len(in_str)

    while i < length:
        # DEVANAGARI STARTS
        if (
            i < length - 2
            and ord(in_str[i]) == 0x905
            and ord(in_str[i + 1]) == 0x93E
            and ord(in_str[i + 2]) == 0x945
        ):
            out_str += chr(0x911)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0x905
            and ord(in_str[i + 1]) == 0x93E
            and ord(in_str[i + 2]) == 0x946
        ):
            out_str += chr(0x912)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0x905
            and ord(in_str[i + 1]) == 0x93E
            and ord(in_str[i + 2]) == 0x947
        ):
            out_str += chr(0x913)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0x905
            and ord(in_str[i + 1]) == 0x93E
            and ord(in_str[i + 2]) == 0x948
        ):
            out_str += chr(0x914)
            i += 3

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x93E:
            out_str += chr(0x906)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x945:
            out_str += chr(0x972)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x946:
            out_str += chr(0x904)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x949:
            out_str += chr(0x911)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x94A:
            out_str += chr(0x912)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x94B:
            out_str += chr(0x913)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x905 and ord(in_str[i + 1]) == 0x94C:
            out_str += chr(0x914)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x906 and ord(in_str[i + 1]) == 0x945:
            out_str += chr(0x911)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x906 and ord(in_str[i + 1]) == 0x946:
            out_str += chr(0x912)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x906 and ord(in_str[i + 1]) == 0x947:
            out_str += chr(0x913)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x906 and ord(in_str[i + 1]) == 0x948:
            out_str += chr(0x914)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x90F and ord(in_str[i + 1]) == 0x945:
            out_str += chr(0x90D)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x90F and ord(in_str[i + 1]) == 0x946:
            out_str += chr(0x90E)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x90F and ord(in_str[i + 1]) == 0x947:
            out_str += chr(0x910)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x915 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x958)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x916 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x959)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x917 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x95A)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x91C and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x95B)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x921 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x95C)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x922 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x95D)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x928 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x929)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x92B and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x95E)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x92F and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x95F)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x930 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x931)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x933 and ord(in_str[i + 1]) == 0x93C:
            out_str += chr(0x934)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x93E and ord(in_str[i + 1]) == 0x945:
            out_str += chr(0x949)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x93E and ord(in_str[i + 1]) == 0x946:
            out_str += chr(0x94A)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x93E and ord(in_str[i + 1]) == 0x947:
            out_str += chr(0x94B)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x93E and ord(in_str[i + 1]) == 0x948:
            out_str += chr(0x94C)
            i += 2

        # DEVANAGARI ENDS

        # BENGALI STARTS
        elif i < length - 1 and ord(in_str[i]) == 0x985 and ord(in_str[i + 1]) == 0x9BE:
            out_str += chr(0x986)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x9A1 and ord(in_str[i + 1]) == 0x9BC:
            out_str += chr(0x9DC)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x9A2 and ord(in_str[i + 1]) == 0x9BC:
            out_str += chr(0x9DD)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x9AF and ord(in_str[i + 1]) == 0x9BC:
            out_str += chr(0x9DF)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x9C7 and ord(in_str[i + 1]) == 0x9BE:
            out_str += chr(0x9CB)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0x9C7 and ord(in_str[i + 1]) == 0x9D7:
            out_str += chr(0x9CC)
            i += 2

        elif (
            i < length - 2
            and ord(in_str[i]) == 0x9A4
            and ord(in_str[i + 1]) == 0x9CD
            and ord(in_str[i + 2]) == 0x200D
        ):
            out_str += chr(0x9CE)
            i += 3

        # BENGALI ENDS

        # GURMUKHI STARTS
        elif i < length - 1 and ord(in_str[i]) == 0xA05 and ord(in_str[i + 1]) == 0xA3E:
            out_str += chr(0xA06)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA05 and ord(in_str[i + 1]) == 0xA48:
            out_str += chr(0xA10)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA05 and ord(in_str[i + 1]) == 0xA4C:
            out_str += chr(0xA14)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA72 and ord(in_str[i + 1]) == 0xA3F:
            out_str += chr(0xA07)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA72 and ord(in_str[i + 1]) == 0xA40:
            out_str += chr(0xA08)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA72 and ord(in_str[i + 1]) == 0xA47:
            out_str += chr(0xA0F)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA73 and ord(in_str[i + 1]) == 0xA41:
            out_str += chr(0xA09)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA73 and ord(in_str[i + 1]) == 0xA42:
            out_str += chr(0xA0A)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA16 and ord(in_str[i + 1]) == 0xA3C:
            out_str += chr(0xA59)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA17 and ord(in_str[i + 1]) == 0xA3C:
            out_str += chr(0xA5A)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA1C and ord(in_str[i + 1]) == 0xA3C:
            out_str += chr(0xA5B)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA2B and ord(in_str[i + 1]) == 0xA3C:
            out_str += chr(0xA5E)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA32 and ord(in_str[i + 1]) == 0xA3C:
            out_str += chr(0xA33)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA38 and ord(in_str[i + 1]) == 0xA3C:
            out_str += chr(0xA36)
            i += 2

        # GURMUKHI ENDS

        # GUJARATI STARTS
        elif (
            i < length - 2
            and ord(in_str[i]) == 0xA85
            and ord(in_str[i + 1]) == 0xABE
            and ord(in_str[i + 2]) == 0xAC5
        ):
            out_str += chr(0xA91)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xA85
            and ord(in_str[i + 1]) == 0xABE
            and ord(in_str[i + 2]) == 0xAC7
        ):
            out_str += chr(0xA93)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xA85
            and ord(in_str[i + 1]) == 0xABE
            and ord(in_str[i + 2]) == 0xAC8
        ):
            out_str += chr(0xA94)
            i += 3

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xABE:
            out_str += chr(0xA86)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xAC5:
            out_str += chr(0xA8D)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xAC7:
            out_str += chr(0xA8F)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xAC8:
            out_str += chr(0xA90)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xAC9:
            out_str += chr(0xA91)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xACB:
            out_str += chr(0xA93)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA85 and ord(in_str[i + 1]) == 0xACC:
            out_str += chr(0xA94)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA86 and ord(in_str[i + 1]) == 0xAC5:
            out_str += chr(0xA91)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA86 and ord(in_str[i + 1]) == 0xAC7:
            out_str += chr(0xA93)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xA86 and ord(in_str[i + 1]) == 0xAC8:
            out_str += chr(0xA94)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xABE and ord(in_str[i + 1]) == 0xAC5:
            out_str += chr(0xAC9)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xABE and ord(in_str[i + 1]) == 0xAC7:
            out_str += chr(0xACB)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xABE and ord(in_str[i + 1]) == 0xAC8:
            out_str += chr(0xACC)
            i += 2

        # GUJARATI ENDS

        # ODIA STARTS

        elif i < length - 1 and ord(in_str[i]) == 0xB05 and ord(in_str[i + 1]) == 0xB3E:
            out_str += chr(0xB06)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB0F and ord(in_str[i + 1]) == 0xB57:
            out_str += chr(0xB10)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB13 and ord(in_str[i + 1]) == 0xB57:
            out_str += chr(0xB14)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB47 and ord(in_str[i + 1]) == 0xB56:
            out_str += chr(0xB48)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB47 and ord(in_str[i + 1]) == 0xB3E:
            out_str += chr(0xB4B)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB47 and ord(in_str[i + 1]) == 0xB57:
            out_str += chr(0xB4C)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB21 and ord(in_str[i + 1]) == 0xB3C:
            out_str += chr(0xB5C)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xB22 and ord(in_str[i + 1]) == 0xB3C:
            out_str += chr(0xB5D)
            i += 2

        # ODIA ENDS

        # TAMIL STARTS
        elif i < length - 1 and ord(in_str[i]) == 0xB92 and ord(in_str[i + 1]) == 0xBD7:
            out_str += chr(0xB94)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xBC6 and ord(in_str[i + 1]) == 0xBBE:
            out_str += chr(0xBCA)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xBC7 and ord(in_str[i + 1]) == 0xBBE:
            out_str += chr(0xBCB)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xBC6 and ord(in_str[i + 1]) == 0xBD7:
            out_str += chr(0xBCC)
            i += 2

        # TAMIL ENDS

        # TELUGU STARTS
        elif (
            i < length - 2
            and ord(in_str[i]) == 0xC2C
            and ord(in_str[i + 1]) == 0xC41
            and ord(in_str[i + 2]) == 0xC41
        ):
            out_str += chr(0xC0B)
            i += 3

        elif i < length - 1 and ord(in_str[i]) == 0xC12 and ord(in_str[i + 1]) == 0xC55:
            out_str += chr(0xC13)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xC12 and ord(in_str[i + 1]) == 0xC4C:
            out_str += chr(0xC14)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xC46 and ord(in_str[i + 1]) == 0xC55:
            out_str += chr(0xC47)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xC46 and ord(in_str[i + 1]) == 0xC56:
            out_str += chr(0xC48)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xC4A and ord(in_str[i + 1]) == 0xC55:
            out_str += chr(0xC4B)
            i += 2

        # TELUGU ENDS

        # KANNADA STARTS
        elif (
            i < length - 2
            and ord(in_str[i]) == 0xCC6
            and ord(in_str[i + 1]) == 0xCC2
            and ord(in_str[i + 2]) == 0xCD5
        ):
            out_str += chr(0xCCB)
            i += 3

        elif i < length - 1 and ord(in_str[i]) == 0xC92 and ord(in_str[i + 1]) == 0xCCC:
            out_str += chr(0xC94)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xCBF and ord(in_str[i + 1]) == 0xCD5:
            out_str += chr(0xCC0)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xCC6 and ord(in_str[i + 1]) == 0xCD5:
            out_str += chr(0xCC7)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xCC6 and ord(in_str[i + 1]) == 0xCD6:
            out_str += chr(0xCC8)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xCC6 and ord(in_str[i + 1]) == 0xCC2:
            out_str += chr(0xCCA)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xCCA and ord(in_str[i + 1]) == 0xCD5:
            out_str += chr(0xCCB)
            i += 2

        # KANNADA ENDS

        # MALAYALAM STARTS
        elif i < length - 1 and ord(in_str[i]) == 0xD07 and ord(in_str[i + 1]) == 0xD57:
            out_str += chr(0xD08)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD09 and ord(in_str[i + 1]) == 0xD57:
            out_str += chr(0xD0A)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD12 and ord(in_str[i + 1]) == 0xD57:
            out_str += chr(0xD14)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD12 and ord(in_str[i + 1]) == 0xD3E:
            out_str += chr(0xD13)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD0E and ord(in_str[i + 1]) == 0xD46:
            out_str += chr(0xD10)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD46 and ord(in_str[i + 1]) == 0xD46:
            out_str += chr(0xD48)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD46 and ord(in_str[i + 1]) == 0xD3E:
            out_str += chr(0xD4A)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD47 and ord(in_str[i + 1]) == 0xD3E:
            out_str += chr(0xD4B)
            i += 2

        elif i < length - 1 and ord(in_str[i]) == 0xD46 and ord(in_str[i + 1]) == 0xD57:
            out_str += chr(0xD4C)
            i += 2

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xD23
            and ord(in_str[i + 1]) == 0xD4D
            and ord(in_str[i + 2]) == 0x200D
        ):
            out_str += chr(0xD7A)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xD28
            and ord(in_str[i + 1]) == 0xD4D
            and ord(in_str[i + 2]) == 0x200D
        ):
            out_str += chr(0xD7B)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xD30
            and ord(in_str[i + 1]) == 0xD4D
            and ord(in_str[i + 2]) == 0x200D
        ):
            out_str += chr(0xD7C)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xD32
            and ord(in_str[i + 1]) == 0xD4D
            and ord(in_str[i + 2]) == 0x200D
        ):
            out_str += chr(0xD7D)
            i += 3

        elif (
            i < length - 2
            and ord(in_str[i]) == 0xD33
            and ord(in_str[i + 1]) == 0xD4D
            and ord(in_str[i + 2]) == 0x200D
        ):
            out_str += chr(0xD7E)
            i += 3

        # MALAYALAM ENDS

        else:
            out_str += in_str[i]
            i += 1

    return out_str
