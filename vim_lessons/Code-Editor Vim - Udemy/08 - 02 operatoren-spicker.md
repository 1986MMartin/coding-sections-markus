# Insert-Mode

Platziere den Cursor jeweils auf die Pfeile. Beim Linkspfeil fügst du etwas
davor ein, beim Rechtspfeil dahinter:

  ← Davor (`i`)
  Dahinter → (`a`)

Bewege den Cursor an Anfang, und füge direkt etwas am Ende ein: →
(`A`)

← Bewege den Cursor ans Ende und für am Anfang etwas ein. (`I`)

↓↑ Cursor in diese Zeile und unter oder über ihr etwas einfügen. (`o`, `O`)

Mache deine Änderungen rückgängig. (`u`) Wiederhole die Änderungen dann doch
wieder, deine Arbeit soll ja nicht umsonst gewesen sein. (`^r`)

-------------------------------------------------------------------------------
# Ändern

Dieser ganze Satz soll verändert werden. (`cc`)

Jetzt soll nur dieses →WORT← verändert werden. (`cw`)

Ab →hier wird alles geändert. (`C`)

Bis zum →x wird alles verändert. (`cfx`, `cFx`)

-------------------------------------------------------------------------------
# Ersetzen

In dieser Zeile steckt ein Fejlet. Korrigiere das Wort in "Fehler", indem du
einzelne Zeichen ersetzt. (`r`)

-------------------------------------------------------------------------------
# Löschen

Dieser ganze Satz soll gelöscht werden. (`dd`)

Jetzt soll nur dieses →WORT← gelöscht werden. (`dw`)

Ab →HIER wird alles gelöscht. (`D`)

Zum Schluss werden nur einzelne →x Zeichen →X gelöscht. (`x`, `X`)

-------------------------------------------------------------------------------
# Groß-/Kleinschreibung verändern

hier steht alles in klein, ich möchte aber groß sein. (`~`, `g~~`)

-------------------------------------------------------------------------------
# Einrückungstiefe verändern

Rücke mich doch mal ein paar Ebenen ein! (`>>`)
    Und mich rückst du lieber etwas zurück! (`<<`)

-------------------------------------------------------------------------------
# Kopieren und einfügen

↓ Dieser Satz ist nicht gern allein. Kopiere und füge ihn oben und unten ein! ↑
(`yy`, `p`, `P`).

Kopiere dieses →Wort← und füge es genau hier ein: →
(`yw`, `p`)

-------------------------------------------------------------------------------
# Zur letzten Einfüge-Stelle gehen

Schreibe hier einige Wörter auf: →

Dann navigierst du einige Zeilen weg, bis die einfällt, dass du noch etwas
ergänzen möchtest. Benutze einen einzigen Befehl, um wieder zur alten Stelle
zurückzukehren und direkt im Insert-Mode zu landen.
(`gi`)
