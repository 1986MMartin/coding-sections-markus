<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">

        <title>PHP Arrays</title>
    </head>
    <body>
        <div class="container">
            <h1>PHP Arrays</h1>
      
            <?php
            
                // Index Array
                $autos = array("Mercedes","BMW","VW");
            
                echo $autos[1];
            
                echo "<br>";
            
                $arr_lange = count($autos);
            
                for($i = 0; $i < $arr_lange; $i++) {
                    echo "Hersteller: ", $autos[$i];
                    echo "<br>";
                }
            
                echo "<br>";
            
                // Assoziative Array
                $alter = array("Peter"=>35,"Susanne"=>24,"Marie"=>48);
            
                echo $alter["Marie"];
            
                echo "<br>";
            
                foreach($alter as $j => $j_wert) {
                    echo "Key: ", $j, ", Wert: ", $j_wert;
                    echo "<br>";
                }
      
                // Sortieren
                sort($autos); // aufsteigende Sortierung
                
                echo $autos[1];
            
                echo "<br>";
            
                // rsort absteigende Sortierung
                // asort -> assoziative Arrays aufsteigend, Werte
                // arsort -> assoziative Arrays absteigende, Werte
                // ksort -> assoziative Arrays aufsteigend Keys
                // krsort -> assoziative Arrays absteigende Keys
            
                $farben = array("success","info","warning");
                
                $farbe_laenge = count($farben);
            
                for($k = 0; $k < $farbe_laenge; $k++) {
                    echo "<div class='alert alert-$farben[$k]'>Farbe $farben[$k]</div>";
                }
            ?>    
        </div>
        
        <!-- Optionalen JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="js/jquery-3.3.1.slim.min.js"></script>
        <script src="js/popper.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>