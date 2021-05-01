# Buffer öffnen

Bevor du loslegst: 2. Vim öffnen!

Öffne eine Datei und schreibe dort etwas hinein (`:e buffer1.txt`). Dann öffne
eine andere Datei und schreibe dort ebenfalls etwas hinein (`:e buffer2.txt`).

-------------------------------------------------------------------------------
# Bufferliste ansehen

Schaue dir die Buffer-Liste an. (`:buffers`)

-------------------------------------------------------------------------------
# Zu Buffern wechseln

Wechsle zwischen den Buffern hin und her (`:buffer buffer1.txt`, `:b
buffer2.txt`). Natürlich kannst du mit Tab vervollständigen/suchen, probiere
mal `:b ff` und drücke dann Tab.

-------------------------------------------------------------------------------
# Buffer entladen

Entlade einen Buffer mit `:bd`.

-------------------------------------------------------------------------------
# Fenster teilen

Teile dieses Fenster horizontal und noch einmal vertikal. (`^ws`, `^wv`)

-------------------------------------------------------------------------------
# Zwischen Fenster bewegen

Bewege dich zu allen geteilten Fenstern. (`^wh`, `^wj`, `^wk`, `^wl`)

-------------------------------------------------------------------------------
# Fenstergröße verändern

Vergrößere das Fenster horizontal (`^w+`, `5^w+`, `^w-`) und vertikal (`^w<`,
`^w>`).

Verteile den Platz wieder gleichmäßig zwischen den Fenstern. (`^w=`)

Maximiere dieses Fenster. (`^w_`)

-------------------------------------------------------------------------------
# Fenster schließen

Schließe dieses Fenster. (`:hide`, `:q:`)

-------------------------------------------------------------------------------
# Tabs erstellen

Öffne einen Tab. (`:tabnew`)

-------------------------------------------------------------------------------
# Zwischen Tabs navigieren.

Öffne noch einen Tab (`:tabnew`). Jetzt navigiere zwischen den Tabs, sowohl
vorwärts (`gt`) als auch rückwärts (`gT`).

-------------------------------------------------------------------------------
# Tab schließen

Schließe alle Tabs außer einem. (`:tabclose`)
