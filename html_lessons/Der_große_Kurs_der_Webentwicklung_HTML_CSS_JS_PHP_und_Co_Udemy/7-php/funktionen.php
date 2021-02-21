<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">

        <title>PHP Funktionen</title>
    </head>
    <body>
        <div class="container">
            <h1>PHP Funktionen</h1>
      
            <?php
            
                $name = "Susanne";
        
                function sagHallo($fname = "David") {
                    return "<div class='alert alert-info'>Hallo $fname</div>";
                }
            
                echo sagHallo("Peter");
                echo sagHallo();
                echo sagHallo("Susanne");
            
                echo "<br>", $name;
      
            ?>    
        </div>
        
        <!-- Optionalen JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="js/jquery-3.3.1.slim.min.js"></script>
        <script src="js/popper.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>