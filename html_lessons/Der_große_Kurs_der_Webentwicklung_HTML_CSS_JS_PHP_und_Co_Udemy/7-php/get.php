<!doctype html>
<html lang="de">
    <head>
        <!-- Meta Tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">

        <title>PHP $_GET</title>
    </head>
    <body>
        <div class="container">
            <h1>PHP $_GET</h1>
      
            <?php
                
                $user = $_GET["user"];
                $password = $_GET["password"];
            
                echo "Der Nutzer ", $user, " verwendet das Passwort: ", $password;
                
            ?>  
            
            <form action="post.php" method="post">
                Vorname: <input type="text" name="vorname"><br>
                Nachname: <input type="text" name="nachname">
                <input type="submit" value="Senden">
            </form>
        </div>
        
        <!-- Optionalen JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="js/jquery-3.3.1.slim.min.js"></script>
        <script src="js/popper.js"></script>
        <script src="js/bootstrap.min.js"></script>
    </body>
</html>