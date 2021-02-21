<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP Switch Anweisungen</title>
    </head>
    <body>
        <h1>PHP Switch Anweisungen</h1>
        <?php
            $a = 15;
            $b = 7;
        
            $c = "15";
        
            // Gleichheit
            if ($a == $b) {
                echo "True! $a == $b <br>";
            } else {
                echo "False! $a == $b <br>";
            }
        
            if ($a === $c) {
                echo "True! $a === $c <br>";
            } else {
                echo "False! $a === $c <br>";
            }
        
            // Ungleichheit
            if ($a != $b) {
                echo "True! $a != $b <br>";
            } else {
                echo "False! $a != $b <br>";
            }
        
            if ($a !== $c) {
                echo "True! $a !== $c <br>";
            } else {
                echo "False! $a !== $c <br>";
            }
        
            // Größe
            if ($a > $b) {
                echo "True! $a > $b <br>";
            } else {
                echo "False! $a > $b <br>";
            }
        
            if ($a < $b) {
                echo "True! $a < $b <br>";
            } else {
                echo "False! $a < $b <br>";
            }
        
            if ($a >= $b) {
                echo "True! $a >= $b <br>";
            } else {
                echo "False! $a >= $b <br>";
            }
        
            if ($a <= $b) {
                echo "True! $a <= $b <br>";
            } else {
                echo "False! $a <= $b <br>";
            }
        ?>
    </body>
</html>