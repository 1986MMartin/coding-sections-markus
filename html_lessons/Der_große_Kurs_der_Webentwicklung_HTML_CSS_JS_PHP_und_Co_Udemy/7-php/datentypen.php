<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP Datentypen</title>
    </head>
    <body>
        <h1>PHP Datentypen</h1>
        <?php
            # String
            $txt = "Hallo Benutzer";
        
            $ciao = "Tschüss!";
        
            echo $txt;
            echo "<br>";
            echo $ciao;
            
            # Integer
        
            $x = 15;
            $y = 7;
        
            $z = $x - $y;
            echo "<br>";
            echo $z;
        
            # Float bzw. Double
            $a = 3.75;
            $b = 27.5;
        
            # Boolean
            $ja = true;
            $nein = false;
        
            # Array
            $arr = array("Eins","Zwei","Drei");
        
        ?>
    </body>
</html>