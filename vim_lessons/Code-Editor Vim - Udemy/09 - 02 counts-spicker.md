# Mehrere Wörter löschen

Lösche alle 3 Wörter: (`3dw`)
Hallo lieber Vim

-------------------------------------------------------------------------------
# Mehrere Zeilen löschen

Lösche diese zwei Zeilen: (`2dd`)
Dies ist Zeile 1.
Dies ist Zeile 2.

-------------------------------------------------------------------------------
# Mehrere Wörter verändern

**Verändere** diese 4 Wörter in _"Hallo Vim"_: (`4cw`)
Wir sind die Wörter

-------------------------------------------------------------------------------
# Annähern

Lösche alle Zeilen des folgenden Absatzes bis zum Pfeil. Damit das schneller
geht, lösche immer 2 Zeilen und wiederhole das mit dem `.`-Befehl. Aber
Vorsicht, immer geht das nicht gut! (`2dd`, `.`, `dd`)

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie
consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan
et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis
adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore
Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie
et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis
dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer
→ magna aliquam erat volutpat.

-------------------------------------------------------------------------------
# Motion mehrfach wiederholen

Starte beim Pfeil und springe direkt über alle 3 Absätze: (`3}`, `5w`)

→
Absatz 1

Absatz 2

Absatz 3

Starte bei _"Wort1"_ und springe über alle 7 Wörter. (`7w`)

Wort1 Wort2 Wort3 Wort4 Wort5 Wort6 Wort7 ✓

-------------------------------------------------------------------------------
# Relative Zeilennummern

Schalte die relativen Zeilennummern erst einmal ein:
  * `:set number`
  * `:set relativenumber`

Dann bewege den Cursor zur Zeile mit dem Rechtspfeil und lösche bis zur Zeile
mit dem Linkspfeil. **Natürlich** darf du nur die Motion `j` mit einem Count
benutzen, z.B. `123j`! (`4j`, `6dj`)

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming
id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet,
→
consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut
laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis
nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea
commodo consequat.
consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut
←
laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis
nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea

-------------------------------------------------------------------------------
# Mehrfach putten

Kopiere diese Zeile und füge sie unten 5x ein. (`yy`, `5p`)

-------------------------------------------------------------------------------
# Mehrfach einfügen

Erstelle eine 20-Zeichen-lange Linie mit Bindestrichen. (`20i-<ESC>`)

Füge unterhalb dieser Zeile 5 Zeilen ein, in denen das gleiche steht. (`5o`)
