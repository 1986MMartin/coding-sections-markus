<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP Textausgabe</title>
    </head>
    <body>
        <h1>PHP Textausgabe</h1>
        <p>Ausgabe von Text im Beispiel</p>
        <?php
            # Testausgabe mit Echo
            echo "<p>Text den wir <b>ausgeben</b> wollen</p>";
            echo("<p>Weiterer String</p>");
            echo "<p>","Erster String, ", "zweiter String ", "und dritter String.","</p>";
            
            # Textausgabe mit Print
            print "<p>String mit print.</p>";
            print("<p>Nur ein Argument für print.</p>")
        
            # Welche Variante nutzen wir?
            # Echo
        ?>
    </body>
</html>