# Lokale Marken

**WICHTIGER SPICKER-HINWEIS:** Durch eine Markdown-Limitierung und damit es
schöner aussieht, wurden alle Befehle, die mit einem Backtick beginnen, so
notiert: `` `a ``. In diesen Fällen also einfach Backtip und a drücken. Die
doppelten Backticks zu Beginn und zum Ende können ignoriert werden.

Setze hier → ← die Marke _a_. Bewege den Cursor einige Zeilen nach unten und
springe die Marke _a_ wieder an. Schaue dir auch mal die Marken an.
(`ma`, `` `a ``, `'a`, `:marks`)

-------------------------------------------------------------------------------
# Globale Marken

Öffne einen weiteren Buffer, schreibe etwas und setze dort die Marke _A_. Dann
öffne noch einen Buffer, schreibe etwas und setze die Marke _B_. Jetzt springe
zu den Marken _A_ und _B_.
(`:e buffer1.txt`, `mA`, `:e buffer2.txt`, `mB`, `` `A ``, `` `B ``)

-------------------------------------------------------------------------------
# Numerische Marken

Springe zur Marke _0_, um herauszufinden, wo du Vim zuletzt verlassen hast.
Bei den Marken _1-9_ kannst du weiter in die Vergangenheit reisen.
(`` `0 ``, `` `1 ``, ...)

-------------------------------------------------------------------------------
# An letzte Insert-Stelle springen

Gehe in den Insert-Mode und schreibe etwas: →
Bewege den Cursor in eine andere Zeile und springe dann zur Marke _^_.
Vergleiche das mit `gi`.
(`` `^ ``)

-------------------------------------------------------------------------------
# An Stelle der letzten Änderung springen

Ersetze das X durch ein Y: →X
Bewege dann den Cursor in eine andere Zeile und springe zur Marke _._
(`` `. ``)

-------------------------------------------------------------------------------
# Selektions-Marken

Selektiere in diesem Absatz etwas und drücke wieder `<ESC>`. Dann stelle die
Selektion wieder her. Springe zum Anfang und Ende der Selektion.
(`gv`, `` `< ``, `` `> ``)

Yanke diesen Absatz Visual-Line-Mode. Dann springe zum Ende der Selektion und
putte. So ist es besonders einfach, hinter einer Selektion etwas einzufügen.
