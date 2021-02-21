<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>PHP If Anweisungen</title>
    </head>
    <body>
        <h1>PHP If Anweisungen</h1>
        <?php
            $stunde = 22;
        
            if ($stunde < 12) {
                echo "Guten Morgen";
            } elseif ($stunde < 20) {
                echo "Guten Tag";
            } else {
                echo "Guten Abend";
            }
        ?>
    </body>
</html>