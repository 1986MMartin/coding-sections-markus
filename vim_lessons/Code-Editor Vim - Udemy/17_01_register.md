# Numerische Register

Zeilen löschen und mit `:registers` kontrollieren. 

Zeile 1
Zeile 2
Zeile 3
Zeile 4
Zeile 5
Zeile 6

-------------------------------------------------------------------------------
# Benannte Register

Yanke diese Zeile ins Register _b_ und putte es danach wieder. 

-------------------------------------------------------------------------------
# Ein Makro verändern

Zeichne zunächst folgendes Makro ins Register _t_ auf: `iHallo Welt<ESC>bbdw`
und spiele es einige Male ab um zu verstehen, was es macht.


Jetzt putte das soeben aufgenommen Makro und lösche einen `b`-Befehl aus dem
Makro. Dann yanke es wieder ins Register _t_. Spiele es dann erneut ab.


-------------------------------------------------------------------------------
# An benanntes Register anhängen

Yanke das Wort HALLO in das Register _a_. Dann yanke das Wort WELT ebenfalls in
das gleiche Register, aber hänge es an, anstatt den Inhalt zu ersetzen. Danach
putte das Register, um den Inhalt zu kontrollieren.


-------------------------------------------------------------------------------
# Inhalte einfach tauschen

Tausche "Stefan" und "Bocholt".


  * Mein Name ist Bocholt.
  * Ich wohne in Stefan.

-------------------------------------------------------------------------------
# Read-Only-Register

Schreibe das Wort "Test" zweimal: Einmal über den Insert-Mode, und das zweite
Mal aus dem _._-Register. →


Füge den Namen der aktuellen Datei ein. →


Führe den Befehl `:echo 'Hallo'` aus. Dann putte diesen Befehl aus dem
Befehlsregister. →


-------------------------------------------------------------------------------
# Selektions-Register

Kopiere auf einer Webseite einen Text und füge ihn hier ein. 
→

Kopiere diese Zeile und füge sie in einem 2. Vim wieder ein. 

**NUR LINUX:** Wähle diese Zeile im Visual-Mode aus und füge sie ein!

→
