def draw_colored_trapez(height, base_width, color_code):
    """
    Zeichnet ein farbiges Trapez mit Sternchen.

    :param height: Die Höhe des Trapezes (Anzahl der Zeilen)
    :param base_width: Die Breite der Basis des Trapezes
    :param color_code: Der ANSI Escape-Code für die Farbe
    """
    if height < 3 or base_width < 3:
        print("Ungültige Eingaben. Höhe und Basisbreite müssen mindestens 3 sein.")
        return

    for i in range(height):
        spaces = max(0, height - i - 1)
        stars = min(base_width, 2 * i + 1)
        colored_line = " " * spaces + color_code + "*" * stars + "\033[0m"
        print(colored_line)

# Beispielaufruf mit roter Farbe (ANSI Escape-Code für Rot: \033[91m)
height = int(input("Gib die Höhe des Trapezes an: "))
base_width = int(input("Gib die Breite der Basis des Trapezes an: "))
color_code = "\033[34m"  # Rot

draw_colored_trapez(height, base_width, color_code)

def draw_cat():
    cat = r"""
 /\_/\ 
( o.o )
 > ^ <
    """
    print(cat)

# Aufruf der Funktion, um die Katze zu zeichnen
draw_cat()

def draw_dog():
    dog = r"""
 / \__
(    @\___
 /         O
/   (_____/
/_____/   U
    """
    print(dog)

# Aufruf der Funktion, um den Hund zu zeichnen
draw_dog()

monalisa = [


    
"                                _______\n"
"                           _,,ad8888888888bba,_\n "
"                        ,ad88888I888888888888888ba,\n"
"                      ,88888888I88888888888888888888a,\n"
"                    ,d888888888I8888888888888888888888b,\n"
"                   d88888PP""""     ""YY88888888888888888888b,
                 ,d88"'__,,--------,,,,.;ZZZY8888888888888,
                ,8IIl'"                ;;l"ZZZIII8888888888,
               ,I88l;'                  ;lZZZZZ888III8888888,
             ,II88Zl;.                  ;llZZZZZ888888I888888,
            ,II888Zl;.                .;;;;;lllZZZ888888I8888b
           ,II8888Z;;                 `;;;;;''llZZ8888888I8888,
           II88888Z;'                        .;lZZZ8888888I888b
           II88888Z; _,aaa,      .,aaaaa,__.l;llZZZ88888888I888
           II88888IZZZZZZZZZ,  .ZZZZZZZZZZZZZZ;llZZ88888888I888,
           II88888IZZ<'(@@>Z|  |ZZZ<'(@@>ZZZZ;;llZZ888888888I88I
          ",II88888;   `"" ;|  |ZZ; `""      ;;llZ8888888888I888"
          II888888l            `;;          .;llZZ8888888888I888,
         ,II888888Z;           ;;;        .;;llZZZ8888888888I888I
         III888888Zl;    ..,   `;;       ,;;lllZZZ88888888888I888
         II88888888Z;;...;(_    _)      ,;;;llZZZZ88888888888I888,
         II88888888Zl;;;;;' `--'Z;.   .,;;;;llZZZZ88888888888I888b
         ]I888888888Z;;;;'   ";llllll;..;;;lllZZZZ88888888888I8888,
         II888888888Zl.;;"Y88bd888P";;,..;lllZZZZZ88888888888I8888I
         II8888888888Zl;.; `"PPP";;;,..;lllZZZZZZZ88888888888I88888
         II888888888888Zl;;. `;;;l;;;;lllZZZZZZZZW88888888888I88888
         `II8888888888888Zl;.    ,;;lllZZZZZZZZWMZ88888888888I88888
          II8888888888888888ZbaalllZZZZZZZZZWWMZZZ8888888888I888888,
          `II88888888888888888b"WWZZZZZWWWMMZZZZZZI888888888I888888b
           `II88888888888888888;ZZMMMMMMZZZZZZZZllI888888888I8888888
            `II8888888888888888 `;lZZZZZZZZZZZlllll888888888I8888888,
             II8888888888888888, `;lllZZZZllllll;;.Y88888888I8888888b,
            ,II8888888888888888b   .;;lllllll;;;.;..88888888I88888888b,
            II888888888888888PZI;.  .`;;;.;;;..; ...88888888I8888888888,
            II888888888888PZ;;';;.   ;. .;.  .;. .. Y8888888I88888888888b,
           ,II888888888PZ;;'                        `8888888I8888888888888b,
           II888888888'                              888888I8888888888888888b
          ,II888888888                              ,888888I88888888888888888
         ,d88888888888                              d888888I8888888888ZZZZZZZ
      ,ad888888888888I                              8888888I8888ZZZZZZZZZZZZZ
    ,d888888888888888'                              888888IZZZZZZZZZZZZZZZZZZ
  ,d888888888888P'8P'                               Y888ZZZZZZZZZZZZZZZZZZZZZ
 ,8888888888888,  "                                 ,ZZZZZZZZZZZZZZZZZZZZZZZZ
d888888888888888,                                ,ZZZZZZZZZZZZZZZZZZZZZZZZZZZ
888888888888888888a,      _                    ,ZZZZZZZZZZZZZZZZZZZZ888888888
888888888888888888888ba,_d'                  ,ZZZZZZZZZZZZZZZZZ88888888888888
8888888888888888888888888888bbbaaa,,,______,ZZZZZZZZZZZZZZZ888888888888888888
88888888888888888888888888888888888888888ZZZZZZZZZZZZZZZ888888888888888888888
8888888888888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888888888
888888888888888888888888888888888888888ZZZZZZZZZZZZZZ888888888888888888888888
8888888888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888888888888
88888888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888888888888
8888888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888 Normand  88
88888888888888888888888888888888ZZZZZZZZZZZZZZ8888888888888888888 Veilleux 88
8888888888888888888888888888888ZZZZZZZZZZZZZZ88888888888888888888888888888888
"""
]


for row in monalisa:
    print(row)