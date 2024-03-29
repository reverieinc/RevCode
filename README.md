RevCode
=======
A Roman encoding and mapping module for Indian languages.


*Languages Supported*
---------------------
| Language  | ISO Code |
|-----------|----------|
| Hindi     | hi       |
| Punjabi   | pa       |
| Gujarati  | gu       |
| Marathi   | mr       |
| Kannada   | kn       |
| Telugu    | te       |
| Tamil     | ta       |
| Malayalam | ml       |
| Oriya     | or       |
| Assamese  | as       |
| Bengali   | bn       |

Installation
============

From PyPI:  
```pip install revcode```

From source `tar.gz` bundle:  
```pip install revcode-2.0.tar.gz```


Example Usage
=============

*1. Convert text to RevCode*
--------------------------------------------
```python
from revcode import revcode_conversion as rc

text = 'नमस्ते'
print(rc.to_revcode(text, 'hi'))  # language as ISO-2 code

text = 'ನಮಸ್ಕಾರ'
print(rc.to_revcode(text, 'kannada'))  # langauge as full name

text = 'నమస్కారం'
print(rc.to_revcode(text, 'te'))

```
*Output*
-------
```
namastE
namaskAra
namaskArx
```

*2. Convert text from RevCode*
-----------------------------------------------------
**Note: Converting from non-RevCode text will give inappropriate results**
```python
from revcode import revcode_conversion as rc

text = 'namastE'
print(rc.from_revcode(text, 'hindi'))

text = 'namaskAra'
print(rc.from_revcode(text, 'kn'))

text = 'namaskArx'
print(rc.from_revcode(text, 'telugu'))
```
*Output*
------------
```
नमस्ते
ನಮಸ್ಕಾರ
నమస్కారం
```

RevCode Reference Table
=======================

| RevCode | Unicode-Hindi | Hindi | Unicode-Punjabi | Punjabi | Unicode-Gujarati | Gujarati | Unicode-Marathi | Marathi | Unicode-Kannada | Kannada | Unicode-Telugu | Telugu | Unicode-Tamil | Tamil | Unicode-Malayalam | Malayalam | Unicode-Oriya | Oriya | Unicode-Assamese | Assamese | Unicode-Bengali | Bengali |
|---------|---------------|-------|-----------------|---------|------------------|----------|-----------------|---------|-----------------|---------|----------------|--------|---------------|-------|-------------------|-----------|---------------|-------|------------------|----------|-----------------|---------|
| M       | 0x901         | ँ      | 0xA01           | ਁ        | 0xA81            | ઁ         | 0x901           | ँ        | 0xC81           | -       | 0xC01          | ఁ      | 0xB81         | -     | 0x0D01            | -         | 0x0B01        | ଁ      | 0x981            | ঁ         | 0x981           | ঁ        |
| x       | 0x902         | ं      | 0xA02           | ਂ        | 0xA82            | ં         | 0x902           | ं        | 0xC82           | ಂ       | 0xC02          | ం      | 0xB82         | ஂ      | 0x0D02            | ം         | 0x0B02        | ଂ     | 0x982            | ং        | 0x982           | ং       |
| X       | 0x903         | ः     | 0xA03           | ਃ       | 0xA83            | ઃ        | 0x903           | ः       | 0xC83           | ಃ       | 0xC03          | ః      | 0xB83         | ஃ     | 0x0D03            | ഃ         | 0x0B03        | ଃ     | 0x983            | ঃ        | 0x983           | ঃ       |
| a       | 0x905         | अ     | 0xA05           | ਅ       | 0xA85            | અ        | 0x905           | अ       | 0xC85           | ಅ       | 0xC05          | అ      | 0xB85         | அ     | 0x0D05            | അ         | 0x0B05        | ଅ     | 0x985            | অ        | 0x985           | অ       |
| A       | 0x906         | आ     | 0xA06           | ਆ       | 0xA86            | આ        | 0x906           | आ       | 0xC86           | ಆ       | 0xC06          | ఆ      | 0xB86         | ஆ     | 0x0D06            | ആ         | 0x0B06        | ଆ     | 0x986            | আ        | 0x986           | আ       |
| i       | 0x907         | इ     | 0xA07           | ਇ       | 0xA87            | ઇ        | 0x907           | इ       | 0xC87           | ಇ       | 0xC07          | ఇ      | 0xB87         | இ     | 0x0D07            | ഇ         | 0x0B07        | ଇ     | 0x987            | ই        | 0x987           | ই       |
| I       | 0x908         | ई     | 0xA08           | ਈ       | 0xA88            | ઈ        | 0x908           | ई       | 0xC88           | ಈ       | 0xC08          | ఈ      | 0xB88         | ஈ     | 0x0D08            | ഈ         | 0x0B08        | ଈ     | 0x988            | ঈ        | 0x988           | ঈ       |
| u       | 0x909         | उ     | 0xA09           | ਉ       | 0xA89            | ઉ        | 0x909           | उ       | 0xC89           | ಉ       | 0xC09          | ఉ      | 0xB89         | உ     | 0x0D09            | ഉ         | 0x0B09        | ଉ     | 0x989            | উ        | 0x989           | উ       |
| U       | 0x90A         | ऊ     | 0xA0A           | ਊ       | 0xA8A            | ઊ        | 0x90A           | ऊ       | 0xC8A           | ಊ       | 0xC0A          | ఊ      | 0xB8A         | ஊ     | 0x0D0A            | ഊ         | 0x0B0A        | ଊ     | 0x98A            | ঊ        | 0x98A           | ঊ       |
| WR      | 0x90B         | ऋ     | 0xA0B           | -       | 0xA8B            | ઋ        | 0x90B           | ऋ       | 0xC8B           | ಋ       | 0xC0B          | ఋ      | 0xB8B         | -     | 0x0D0B            | ഋ         | 0x0B0B        | ଋ     | 0x98B            | ঋ        | 0x98B           | ঋ       |
| WD      | 0x90C         |       | 0xA0C           | -       | 0xA8C            | ઌ        | 0x90C           |         | 0xC8C           | -       | 0xC0C          | -      | 0xB8C         |       |                   | -         | 0x0B0C        | -     | 0x98C            | -        | 0x98C           | -       |
| WA      | 0x90D         | ऍ     | 0xA0D           | -       | 0xA8D            | ઍ        | 0x90D           | ऍ       | 0xC8D           | -       | 0xC0D          | -      | 0xB8D         | -     |                   | -         | 0x0B0D        | -     | 0x98D            | -        | 0x98D           | -       |
| e       | 0x90E         | -     | 0xA0E           | -       | 0xA8E            |          | 0x90E           |         | 0xC8E           | ಎ       | 0xC0E          | ఎ      | 0xB8E         | எ     | 0x0D0E            | എ         | 0x0B0E        | -     | 0x98E            | -        | 0x98E           | -       |
| E       | 0x90F         | ए     | 0xA0F           | ਏ       | 0xA8F            | એ        | 0x90F           | ए       | 0xC8F           | ಏ       | 0xC0F          | ఏ      | 0xB8F         | ஏ     | 0x0D0F            | ഏ         | 0x0B0F        | ଏ     | 0x98F            | এ        | 0x98F           | এ       |
| YE      | 0x910         | ऐ     | 0xA10           | ਐ       | 0xA90            | ઐ        | 0x910           | ऐ       | 0xC90           | ಐ       | 0xC10          | ఐ      | 0xB90         | ஐ     | 0x0D10            | ഐ         | 0x0B10        | ଐ     | 0x990            | ঐ        | 0x990           | ঐ       |
| WO      | 0x911         | ऑ     | 0xA11           |         | 0xA91            | ઑ        | 0x911           | ऑ       | 0xC91           | -       | 0xC11          | -      | 0xB91         | -     |                   | -         | 0x0B11        | -     | 0x991            | -        | 0x991           | -       |
| o       | 0x912         | -     | 0xA12           |         | 0xA92            |          | 0x912           |         | 0xC92           | ಒ       | 0xC12          | ఒ      | 0xB92         | ஒ     | 0x0D12            | ഒ         | 0x0B12        | -     | 0x992            | -        | 0x992           | -       |
| O       | 0x913         | ओ     | 0xA13           | ਓ       | 0xA93            | ઓ        | 0x913           | ओ       | 0xC93           | ಓ       | 0xC13          | ఓ      | 0xB93         | ஓ     | 0x0D13            | ഓ         | 0x0B13        | ଓ     | 0x993            | ও        | 0x993           | ও       |
| YO      | 0x914         | औ     | 0xA14           | ਔ       | 0xA94            | ઔ        | 0x914           | औ       | 0xC94           | ಔ       | 0xC14          | ఔ      | 0xB94         | ஒள    | 0x0D14            | ഔ         | 0x0B14        | ଔ     | 0x994            | ঔ        | 0x994           | ঔ       |
| k       | 0x915         | क     | 0xA15           | ਕ       | 0xA95            | ક        | 0x915           | क       | 0xC95           | ಕ       | 0xC15          | క      | 0xB95         | க     | 0x0D15            | ക         | 0x0B15        | କ     | 0x995            | ক        | 0x995           | ক       |
| K       | 0x916         | ख     | 0xA16           | ਖ       | 0xA96            | ખ        | 0x916           | ख       | 0xC96           | ಖ       | 0xC16          | ఖ      | 0xB96         | -     | 0x0D16            | ഖ         | 0x0B16        | ଖ     | 0x996            | খ        | 0x996           | খ       |
| g       | 0x917         | ग     | 0xA17           | ਗ       | 0xA97            | ગ        | 0x917           | ग       | 0xC97           | ಗ       | 0xC17          | గ      | 0xB97         | -     | 0x0D17            | ഗ         | 0x0B17        | ଗ     | 0x997            | গ        | 0x997           | গ       |
| G       | 0x918         | घ     | 0xA18           | ਘ       | 0xA98            | ઘ        | 0x918           | घ       | 0xC98           | ಘ       | 0xC18          | ఘ      | 0xB98         | -     | 0x0D18            | ഘ         | 0x0B18        | ଘ     | 0x998            | ঘ        | 0x998           | ঘ       |
| z       | 0x919         | ङ     | 0xA19           | ਙ       | 0xA99            | ઙ        | 0x919           | ङ       | 0xC99           | ಙ       | 0xC19          | ఙ      | 0xB99         | ங     | 0x0D19            | ങ         | 0x0B19        | ଙ     | 0x999            | ঙ        | 0x999           | ঙ       |
| c       | 0x91A         | च     | 0xA1A           | ਚ       | 0xA9A            | ચ        | 0x91A           | च       | 0xC9A           | ಚ       | 0xC1A          | చ      | 0xB9A         | ச     | 0x0D1A            | ച         | 0x0B1A        | ଚ     | 0x99A            | চ        | 0x99A           | চ       |
| C       | 0x91B         | छ     | 0xA1B           | ਛ       | 0xA9B            | છ        | 0x91B           | छ       | 0xC9B           | ಛ       | 0xC1B          | ఛ      | 0xB9B         | -     | 0x0D1B            | ഛ         | 0x0B1B        | ଛ     | 0x99B            | ছ        | 0x99B           | ছ       |
| j       | 0x91C         | ज     | 0xA1C           | ਜ       | 0xA9C            | જ        | 0x91C           | ज       | 0xC9C           | ಜ       | 0xC1C          | జ      | 0xB9C         | ஜ     | 0x0D1C            | ജ         | 0x0B1C        | ଜ     | 0x99C            | জ        | 0x99C           | জ       |
| J       | 0x91D         | झ     | 0xA1D           | ਝ       | 0xA9D            | ઝ        | 0x91D           | झ       | 0xC9D           | ಝ       | 0xC1D          | ఝ      | 0xB9D         | -     | 0x0D1D            | ഝ         | 0x0B1D        | ଝ     | 0x99D            | ঝ        | 0x99D           | ঝ       |
| Z       | 0x91E         | ञ     | 0xA1E           | ਞ       | 0xA9E            | ઞ        | 0x91E           | ञ       | 0xC9E           | ಞ       | 0xC1E          | ఞ      | 0xB9E         | ஞ     | 0x0D1E            | ഞ         | 0x0B1E        | ଞ     | 0x99E            | ঞ        | 0x99E           | ঞ       |
| T       | 0x91F         | ट     | 0xA1F           | ਟ       | 0xA9F            | ટ        | 0x91F           | ट       | 0xC9F           | ಟ       | 0xC1F          | ట      | 0xB9F         | ட     | 0x0D1F            | ട         | 0x0B1F        | ଟ     | 0x99F            | ট        | 0x99F           | ট       |
| HT      | 0x920         | ठ     | 0xA20           | ਠ       | 0xAA0            | ઠ        | 0x920           | ठ       | 0xCA0           | ಠ       | 0xC20          | ఠ      | 0xBA0         | -     | 0x0D20            | ഠ         | 0x0B20        | ଠ     | 0x9A0            | ঠ        | 0x9A0           | ঠ       |
| D       | 0x921         | ड     | 0xA21           | ਡ       | 0xAA1            | ડ        | 0x921           | ड       | 0xCA1           | ಡ       | 0xC21          | డ      | 0xBA1         | -     | 0x0D21            | ഡ         | 0x0B21        | ଡ     | 0x9A1            | ড        | 0x9A1           | ড       |
| HD      | 0x922         | ढ     | 0xA22           | ਢ       | 0xAA2            | ઢ        | 0x922           | ढ       | 0xCA2           | ಢ       | 0xC22          | ఢ      | 0xBA2         | -     | 0x0D22            | ഢ         | 0x0B22        | ଢ     | 0x9A2            | ঢ        | 0x9A2           | ঢ       |
| N       | 0x923         | ण     | 0xA23           | ਣ       | 0xAA3            | ણ        | 0x923           | ण       | 0xCA3           | ಣ       | 0xC23          | ణ      | 0xBA3         | ண     | 0x0D23            | ണ         | 0x0B23        | ଣ     | 0x9A3            | ণ        | 0x9A3           | ণ       |
| t       | 0x924         | त     | 0xA24           | ਤ       | 0xAA4            | ત        | 0x924           | त       | 0xCA4           | ತ       | 0xC24          | త      | 0xBA4         | த     | 0x0D24            | ത         | 0x0B24        | ତ     | 0x9A4            | ত        | 0x9A4           | ত       |
| Ht      | 0x925         | थ     | 0xA25           | ਥ       | 0xAA5            | થ        | 0x925           | थ       | 0xCA5           | ಥ       | 0xC25          | థ      | 0xBA5         | -     | 0x0D25            | ഥ         | 0x0B25        | ଥ     | 0x9A5            | থ        | 0x9A5           | থ       |
| d       | 0x926         | द     | 0xA26           | ਦ       | 0xAA6            | દ        | 0x926           | द       | 0xCA6           | ದ       | 0xC26          | ద      | 0xBA6         | -     | 0x0D26            | ദ         | 0x0B26        | ଦ     | 0x9A6            | দ        | 0x9A6           | দ       |
| Hd      | 0x927         | ध     | 0xA27           | ਧ       | 0xAA7            | ધ        | 0x927           | ध       | 0xCA7           | ಧ       | 0xC27          | ధ      | 0xBA7         | -     | 0x0D27            | ധ         | 0x0B27        | ଧ     | 0x9A7            | ধ        | 0x9A7           | ধ       |
| n       | 0x928         | न     | 0xA28           | ਨ       | 0xAA8            | ન        | 0x928           | न       | 0xCA8           | ನ       | 0xC28          | న      | 0xBA8         | ந     | 0x0D28            | ന         | 0x0B28        | ନ     | 0x9A8            | ন        | 0x9A8           | ন       |
| Q       | 0x929         | ऩ     | 0xA29           | -       |                  |          | 0x929           | ऩ       | 0xCA9           | -       | 0xC29          | -      | 0xBA9         | ன     |                   | -         | 0x0B29        | -     | 0x9A9            | -        | 0x9A9           | -       |
| p       | 0x92A         | प     | 0xA2A           | ਪ       | 0xAAA            | પ        | 0x92A           | प       | 0xCAA           | ಪ       | 0xC2A          | ప      | 0xBAA         | ப     | 0x0D2A            | പ         | 0x0B2A        | ପ     | 0x9AA            | প        | 0x9AA           | প       |
| P       | 0x92B         | फ     | 0xA2B           | ਫ       | 0xAAB            | ફ        | 0x92B           | फ       | 0xCAB           | ಫ       | 0xC2B          | ఫ      | 0xBAB         | -     | 0x0D2B            | ഫ         | 0x0B2B        | ଫ     | 0x9AB            | ফ        | 0x9AB           | ফ       |
| b       | 0x92C         | ब     | 0xA2C           | ਬ       | 0xAAC            | બ        | 0x92C           | ब       | 0xCAC           | ಬ       | 0xC2C          | బ      | 0xBAC         | -     | 0x0D2C            | ബ         | 0x0B2C        | ବ     | 0x9AC            | ব        | 0x9AC           | ব       |
| B       | 0x92D         | भ     | 0xA2D           | ਭ       | 0xAAD            | ભ        | 0x92D           | भ       | 0xCAD           | ಭ       | 0xC2D          | భ      | 0xBAD         | -     | 0x0D2D            | ഭ         | 0x0B2D        | ଭ     | 0x9AD            | ভ        | 0x9AD           | ভ       |
| m       | 0x92E         | म     | 0xA2E           | ਮ       | 0xAAE            | મ        | 0x92E           | म       | 0xCAE           | ಮ       | 0xC2E          | మ      | 0xBAE         | ம     | 0x0D2E            | മ         | 0x0B2E        | ମ     | 0x9AE            | ম        | 0x9AE           | ম       |
| y       | 0x92F         | य     | 0xA2F           | ਯ       | 0xAAF            | ય        | 0x92F           | य       | 0xCAF           | ಯ       | 0xC2F          | య      | 0xBAF         | ய     | 0x0D2F            | യ         | 0x0B5F        | ୟ     | 0x9AF            | য        | 0x9AF           | য       |
| r       | 0x930         | र     | 0xA30           | ਰ       | 0xAB0            | ર        | 0x930           | र       | 0xCB0           | ರ       | 0xC30          | ర      | 0xBB0         | ர     | 0x0D30            | ര         | 0x0B30        | ର     | 0x9F0            | ৰ        | 0x9B0           | র       |
| R       | 0x931         | ऱ     | 0xA31           |         |                  |          | 0x931           |         | 0xCB1           | ಱ       | 0xC31          | ఱ      | 0xBB1         | -     | 0x0D31            | റ         | 0x0B31        | -     | 0x9B1            | -        | 0x9B1           | -       |
| l       | 0x932         | ल     | 0xA32           | ਲ       | 0xAB2            | લ        | 0x932           | ल       | 0xCB2           | ಲ       | 0xC32          | ల      | 0xBB2         | ல     | 0x0D32            | ല         | 0x0B32        | ଲ     | 0x9B2            | ল        | 0x9B2           | ল       |
| L       | 0x933         | ळ     | 0xA33           | ਲ਼       | 0xAB3            | ળ        | 0x933           | ळ       | 0xCB3           | ಳ       | 0xC33          | ళ      | 0xBB3         | ள     | 0x0D33            | ള         | 0x0B33        | ଳ     | 0x9B3            | -        | 0x9B3           | -       |
| Hz      | 0x934         | ऴ     | 0xA34           |         |                  |          | 0x934           |         | 0xCB4           | -       | 0xC34          | ఴ      | 0xBB4         | ழ     | 0x0D34            | ഴ         | 0x0B34        | -     | 0x9B4            | -        | 0x9B4           | -       |
| v       | 0x935         | व     | 0xA35           | ਵ       | 0xAB5            | વ        | 0x935           | व       | 0xCB5           | ವ       | 0xC35          | వ      | 0xBB5         | வ     | 0x0D35            | വ         | 0x0B71        | ୱ     | 0x9F1            | ৱ        | 0x9F1           | ৱ       |
| S       | 0x936         | श     | 0xA36           | ਸ਼       | 0xAB6            | શ        | 0x936           | श       | 0xCB6           | ಶ       | 0xC36          | శ      | 0xBB6         | ஶ     | 0x0D36            | ശ         | 0x0B36        | ଶ     | 0x9B6            | শ        | 0x9B6           | শ       |
| Hs      | 0x937         | ष     | 0xA37           | -       | 0xAB7            | ષ        | 0x937           | ष       | 0xCB7           | ಷ       | 0xC37          | ష      | 0xBB7         | ஷ     | 0x0D37            | ഷ         | 0x0B37        | ଷ     | 0x9B7            | ষ        | 0x9B7           | ষ       |
| s       | 0x938         | स     | 0xA38           | ਸ       | 0xAB8            | સ        | 0x938           | स       | 0xCB8           | ಸ       | 0xC38          | స      | 0xBB8         | ஸ     | 0x0D38            | സ         | 0x0B38        | ସ     | 0x9B8            | স        | 0x9B8           | স       |
| h       | 0x939         | ह     | 0xA39           | ਹ       | 0xAB9            | હ        | 0x939           | ह       | 0xCB9           | ಹ       | 0xC39          | హ      | 0xBB9         | ஹ     | 0x0D39            | ഹ         | 0x0B39        | ହ     | 0x9B9            | হ        | 0x9B9           | হ       |
|         | 0x93C         | ़      | 0xA3C           |         | 0xABC            | ઼         | 0x93C           | ़        | 0xCBC           | -       | 0xC3C          |        | 0xBBC         |       |                   |           | 0x0B3C        | ଼      | 0x9BC            | ়         | 0x9BC           | ়        |
|         | 0x93D         |       | 0xA3D           |         | 0xABD            | ઽ        | 0x93D           |         | 0xCBD           | ಽ       | 0xC3D          | ఽ      | 0xBBD         |       |                   |           | 0x0B3D        | -     | 0x9BD            | -        | 0x9BD           | -       |
| A       | 0x93E         | ा     | 0xA3E           | ਾ       | 0xABE            | ા        | 0x93E           | ा       | 0xCBE           | ಾ       | 0xC3E          | ా       | 0xBBE         | ா     | 0x0D3E            | ാ         | 0x0B3E        | ା     | 0x9BE            | া        | 0x9BE           | া       |
| i       | 0x93F         | ि     | 0xA3F           | ਿ       | 0xABF            | િ        | 0x93F           | ि       | 0xCBF           | ಿ        | 0xC3F          | ి       | 0xBBF         | ி     | 0x0D3F            | ി         | 0x0B3F        | ି      | 0x9BF            | ি        | 0x9BF           | ি       |
| I       | 0x940         | ी     | 0xA40           | ੀ       | 0xAC0            | ી        | 0x940           | ी       | 0xCC0           | ೀ       | 0xC40          | ీ       | 0xBC0         | ீ      | 0x0D40            | ീ         | 0x0B40        | ୀ     | 0x9C0            | ী        | 0x9C0           | ী       |
| u       | 0x941         | ु      | 0xA41           | ੁ        | 0xAC1            | ુ         | 0x941           | ु        | 0xCC1           | ು       | 0xC41          | ు      | 0xBC1         | ு     | 0x0D41            | ു          | 0x0B41        | ୁ      | 0x9C1            | ু         | 0x9C1           | ু        |
| U       | 0x942         | ू      | 0xA42           | ੂ        | 0xAC2            | ૂ         | 0x942           | ू        | 0xCC2           | ೂ       | 0xC42          | ూ      | 0xBC2         | ூ     | 0x0D42            | ൂ          | 0x0B42        | ୂ      | 0x9C2            | ু         | 0x9C2           | ু        |
| WR      | 0x943         | ृ      | 0xA43           |         | 0xAC3            | ૃ         | 0x943           | ृ        | 0xCC3           | ೃ       | 0xC43          | ృ      | 0xBC3         | -     | 0x0D7C            | ര്‍         | 0x0B43        | ୃ      | 0x9C3            | ৃ         | 0x9C3           | ৃ        |
| WA      | 0x945         | ॅ      | 0xA45           |         | 0xAC4            | ૄ         | 0x945           | ॅ        | 0xCC5           | -       | 0xC45          | -      | 0xBC5         | -     |                   |           | 0x0B45        | -     | 0x9C5            | -        | 0x9C5           | -       |
| e       | 0x946         | ॆ      | 0xA46           |         | 0xAC5            | ૅ         | 0x946           |         | 0xCC6           | ೆ        | 0xC46          | ె       | 0xBC6         | ெ     | OD46              | െ         | 0x0B46        | -     | 0x9C6            | -        | 0x9C6           | -       |
| E       | 0x947         | े      | 0xA47           | ੇ        | 0xAC7            | ે         | 0x947           | े        | 0xCC7           | ೇ       | 0xC47          | ే       | 0xBC7         | ே     | OD47              | േ         | 0x0B47        | େ     | 0x9C7            | ে        | 0x9C7           | ে       |
| YE      | 0x948         | ै      | 0xA48           | ੈ        | 0xAC8            | ૈ         | 0x948           | ै        | 0xCC8           | ೈ       | 0xC48          | ై       | 0xBC8         | ை     |                   | ൈ         | 0x0B48        | ୈ     | 0x9C8            | ৈ        | 0x9C8           | ৈ       |
| WO      | 0x949         | ॉ     | 0xA49           |         |                  |          | 0x949           | ॉ       | 0xCC9           | -       | 0xC49          | -      | 0xBC9         | -     |                   |           | 0x0B49        | -     | 0x9C9            | -        | 0x9C9           | -       |
| o       | 0x94A         | ॊ     | 0xA4A           |         | 0xAC9            | ૉ        | 0x94A           |         | 0xCCA           | ೊ       | 0xC4A          | ొ       | 0xBCA         | ொ     | 0x0D4A            | ൊ         | 0x0B4A        | -     | 0x2019           | ’        | 0x2019          | ’       |
| O       | 0x94B         | ो     | 0xA4B           | ੋ        | 0xACB            | ો        | 0x94B           | ो       | 0xCCB           | ೋ       | 0xC4B          | ో       | 0xBCB         | ோ     | 0x0D4B            | ോ         | 0x0B4B        | ୋ     | 0x9CB            | ো        | 0x9CB           | ো       |
| YO      | 0x94C         | ौ     | 0xA4C           | ੌ        | 0xACC            | ૌ        | 0x94C           | ौ       | 0xCCC           | ೌ        | 0xC4C          | ౌ       | 0xBCC         | ௌ     |                   |           | 0x0B4C        | ୌ     | 0x9CC            | ৌ        | 0x9CC           | ৌ       |
| q       | 0x94D         | ्      | 0xA4D           |         | 0xACD            | ્         | 0x94D           | ्        | 0xCCD           | ್        | 0xC4D          | ్       | 0xBCD         | ்      |                   | ്          | 0x0B4D        | ୍      | 0x9CD            | ্         | 0x9CD           | ্        |
| Fk      | 0x958         | क़     | 0xA58           | -       |                  |          | 0x958           |         | 0xCD8           | -       | 0xC58          | ౘ      | 0xBD8         |       | 0x0D7F            | ൿ         | 0x0B58        | -     | 0x9D8            | -        | 0x9D8           | -       |
| FK      | 0x959         | ख़     | 0xA59           | ਖ਼       |                  |          | 0x959           |         | 0xCD9           | -       | 0xC59          | ౙ      | 0xBD9         |       |                   |           | 0x0B59        | -     | 0x9D9            | -        | 0x9D9           | -       |
| Fg      | 0x95A         | ग़     | 0xA5A           | ਗ਼       |                  |          | 0x95A           |         | 0xCDA           | -       | 0xC5A          | ౚ      | 0xBDA         |       |                   |           | 0x0B5A        | -     | 0x9DA            | -        | 0x9DA           | -       |
| Fj      | 0x95B         | ज़     | 0xA5B           | ਜ਼       |                  |          | 0x95B           | ज़       | 0xCDB           | -       | 0xC5B          | -      | 0xBDB         |       |                   |           | 0x0B5B        | -     | 0x9DB            | -        | 0x9DB           | -       |
| Fd      | 0x95C         | ड़     | 0xA5C           | ੜ       |                  |          | 0x95C           | ड़       | 0xCDC           | -       | 0xC5C          | -      | 0xBDC         |       |                   |           | 0x0B5C        | ଡ଼     | 0x9DC            | ড়        | 0x9DC           | ড়       |
| HR      | 0x95D         | ढ़     | 0xA5D           |         |                  |          | 0x95D           | ढ़       | 0xCDD           | -       | 0xC5D          | -      | 0xBDD         |       | 0x0D43            | ൃ          | 0x0B5D        | ଢ଼     | 0x9DD            | ঢ়        | 0x9DD           | ঢ়       |
| FP      | 0x95E         | फ़     | 0xA5E           | ਫ਼       |                  |          | 0x95E           | फ़       | 0xCDE           | ೞ       | 0xC5E          | -      | 0xBDE         |       |                   |           | 0x0B5E        | -     | 0x9DE            | -        | 0x9DE           | -       |
| Fy      | 0x95F         | य़     | 0xA5F           | -       |                  |          | 0x95F           |         | 0xCDF           | -       | 0xC5F          | -      | 0xBDF         |       |                   |           | 0x0B2F        | ଯ     | 0x9DF            | য়        | 0x9DF           | য়       |
| YN      | 0x970         |       | 0xA70           | ੰ        |                  |          |                 |         |                 |         |                |        |               |       |             |         |               |       |                  | -        |                 | -       |
| HH      | 0x971         |       | 0xA71           | ੱ        |                  |          |                 |         |                 |         |                |        |               |       |                   |           |               |       |                  | -        |                 | -       |
| Yt      |               |       |                 |         |                  |          |                 |         |                 |         |                |        |               |       | 0x0D7A                 | ണ്‍           |               |       | 0x9CE            | ৎ        |                 | ৎ       |
| Yn      |               |       |                 |         |                  |          |                 |         |                 |         |                |        |               |       | 0x0D7B            | ന്‍         |               |       |                  |          |                 |         |
| Yl      |               |       |                 |         |                  |          | 0x093D          |       |                 |         |                |        |               |       | 0x0D7D            | ല്‍         |               |       |                  |          |                 |         |
| YL      |               |       |                 |         |                  |          | 0x0952          |       |                 |         |                |        |               |       | 0x0D7E            | ള്‍         |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |           |       |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
| Yr      |               |       |                 |         |                  |          | 0x0960          | ॠ       |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |           |       |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |                 |         |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |                 |      |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |                 |      |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |                 |      |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |
|         |               |       |                 |         |                  |          |                 |     |                 |         |                |        |               |       |                   |           |               |       |                  |          |                 |         |



