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
            # Ausprägungen überprüfen und Anweisungen durchführen
            
            $tag = "Samstag";
        
            switch ($tag) {
                case "Montag":
                    echo "Es ist Montag.";
                    break;
                case "Dienstag":
                    echo "Es ist Dienstag.";
                    break;
                case "Mittwoch":
                    echo "Es ist Mittwoch.";
                    break;
                case "Donnerstag":
                    echo "Es ist Donnerstag.";
                    break;
                case "Freitag":
                    echo "Es ist Freitag.";
                    break;
                default:
                    echo "Es ist Wochenende!";
            }
        ?>
    </body>
</html>