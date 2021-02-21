<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP For-Schleife</title>
    </head>
    <body>
        <h1>PHP For-Schleife</h1>
        <?php
        
            // Syntax
            
            for ($i = 0; $i < 5; $i++) {
                echo "$i, ";
            }
        
            echo "<br>";
        
            // Break
        
            for ($j = 0;$j < 15; $j++) {
                if ($j == 10) {
                    echo "Ende";
                    break;
                }
                echo "$j, ";
            }
        
            echo "<br>";
        
            // Continue
        
            for ($k = 0; $k < 15; $k++) {
                if ($k == 10) {
                    echo "Zehn, ";
                    continue;
                }
                echo "$k, ";
            }
        ?>
    </body>
</html>