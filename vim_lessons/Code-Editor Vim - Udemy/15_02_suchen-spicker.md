# Suchen

Suchen den Text "Vim" vorwärts. Platziere den Cursor vorher beim Pfeil.
(`/Vim`)
→ ←

Vim. Gut, aber es gibt den Treffer noch einmal, also suche weiter — aber ohne
den Suchbefehl noch einmal einzugeben!
(`n`)

Vim. Führe die Suche jetzt noch einmal rückwärts durch. Sowohl als Suchbefehl,
als auch ohne.
(`?Vim`, `N`)

-------------------------------------------------------------------------------
# Groß-/Kleinschreibung ignorieren

Suche noch einmal nach "Vim", aber ignoriere die Groß- und Kleinschreibung
dabei.
(`/Vim\c`)

vim Vim VIm VIM vIm vIM viM VIM

-------------------------------------------------------------------------------
# Mit regulärem Ausdruck suchen

Suche alle Wörter, die mit _B_ beginnen, gefolgt von 2 beliebigen Zeichen, und
mit einem _d_ enden. Achte auf die Groß- und Kleinschreibung!
(`/B..d`)

Bild
Bald
Bund
Band

Suche jetzt nach allen Wörtern, die mit _Ha_ beginnen und mit einem _s_ enden.
(`/Ha.*s`)

Haus
Haarspliss
Hamsterglas
Hautverschliss

-------------------------------------------------------------------------------
# Nach Dingen unter dem Cursor suchen

Suche nach dem Wort "Kuh", indem du den Cursor auf ihm platziert und dann
danach suchen lässt — vorwärts und rückwärts. (`*`, `#`)

Eine Kuh macht gerne Muh. Mit einer blöden Kuh hat das aber nichts zu tun. Ein
Kuhfladen riecht nicht gut. Kuh-Dung auch nicht.

-------------------------------------------------------------------------------
# Ersetzen

Ersetze in diesem Satz das Wort "soll" zu "muss".
(`:s/soll/muss/`, `:s/soll/muss/g`)

Man kann den Befehl auch so verändern, dass alle "Kuh"-Wörter in der ganzen
Datei in "Ameise" verändert werden. Probier's mal! (`:%s/Kuh/Ameise/g`)

Benutze den Visual-Mode, um nur in diesem Absatz alle A-Buchstaben durch ein
Gleichheitszeichen (=) zu ersetzen.
(`V`, `:'<,'>s/a/=/g`)

-------------------------------------------------------------------------------
# Mit regulären Ausdrücken ersetzen

Ersetze "Der Preis" mit "Unser Preis", und "Äpfel" mit "Birnen". Benutze dazu
aber nur einen Ersetzenbefehl mit einem regulären Ausdruck.

Der Preis für 12 Äpfel ist: 5 €

(`:s/Der Preis für \(\d\+\) Äpfel/Unser Preis für \1 Birnen/`)

-------------------------------------------------------------------------------
# Befehle auf Treffer anwenden

Lösche alle folgenden Zeilen, die das Wort "DeleteMe" enthalten. Nutze dafür
den Global-Befehl.
(`V`, `:'<,'>g/DeleteMe/d`)

Mich sollst du verändern. DeleteMe
Mich sollst du in Frieden lassen.
Mich sollst du verändern. DeleteMe
Mich sollst du verändern. DeleteMe
Mich sollst du in Frieden lassen.
Mich sollst du in Frieden lassen.
Mich sollst du verändern. DeleteMe
Mich sollst du in Frieden lassen.
