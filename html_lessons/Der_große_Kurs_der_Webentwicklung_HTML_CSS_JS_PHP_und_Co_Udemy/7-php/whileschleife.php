<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP While-Schleife</title>
    </head>
    <body>
        <h1>PHP While-Schleife</h1>
        <?php
        
            // Syntax
            $i = 0;
        
            while ($i < 5) {
                echo "$i, ";
                $i++;
            }
        
            echo "<br>";
        
            // Break
            $j = 0;
        
            while ($j < 15) {
                if ($j == 10) {
                    echo "Ende";
                    break;
                }
                echo "$j, ";
                $j++;
            }
        
            echo "<br>";
        
            // Continue
            $k = 0;
        
            while ($k < 15) {
                if ($k == 10) {
                    echo "Zehn, ";
                    $k++;
                    continue;
                }
                echo "$k, ";
                $k++;
            }
        ?>
    </body>
</html>