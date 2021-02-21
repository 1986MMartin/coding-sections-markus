<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP Logische Operatoren</title>
    </head>
    <body>
        <h1>PHP Logische Operatoren</h1>
        <?php
            $user = "Peter";
            $pw = "Test123";
        
            if ($user == "David" && $pw == "Test123") {
                echo "Du wirst eingeloggt.<br>";
            } else {
                echo "Etwas stimmt hier nicht.<br>";
            }
        
            $mann = "Nein";
            $frau = "Nein";
            $alien = "Ja";
        
            if ($mann == "Ja" || $frau == "Ja") {
                echo "Du bist ein Mensch.<br>";
            } else {
                echo "Du bist ein Alien.<br>";
            }
        
            // Kombination von logischen Operatoren
            // ((a AND b) OR (c AND d))
        
            $tag = "Dienstag";
        
            if (! ($tag == "Samstag" || $tag == "Sonntag")) {
                echo "Leider noch kein Wochenende.<br>";
            } else {
                echo "Es ist Wochenende.<br>";
            }
        ?>
    </body>
</html>