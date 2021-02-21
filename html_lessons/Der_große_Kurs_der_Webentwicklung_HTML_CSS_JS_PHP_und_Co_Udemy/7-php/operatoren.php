<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP Operatoren</title>
    </head>
    <body>
        <h1>PHP Operatoren</h1>
        <?php
            $x = 7;
            $y = 3;
        
            # Addition
            $add = $x + $y;
            echo "Summe: ", $add;
        
            # Sub
        
            $sub = $x - $y;
        
            # Mul
        
            $multi = $x * $y;
        
            # Division
        
            $div = $x / $y;
        
            # Power
            echo "<p>", pow(2,$y),"</p>";
        
            # Wurzel
            echo "<p>", sqrt(9),"</p>";
        
        
            $i = 0;
            # Inkrement
            $i++;
            
            # Dekrement
            $i--;
        
            # Kurzschreibweise
            $a = 10;
            $a += 10; // $a = $a + 10;
        
            # Kommazahl (mit . schreiben)
            $b = 2.5;
        
            echo "<p>", $b * 1.7,"</p>";
        ?>
    </body>
</html>