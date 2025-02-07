<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Treasure Hunt</title>
</head>
<body>
    <h2>Welcome to the Interactive Treasure Hunt!  
Enter your details to solve the puzzle and find the treasure.</h2>
    
    <form method="post">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required><br><br>

        <label for="text">Enter a text message:</label>
        <input type="text" id="text" name="text" required><br><br>

        <button type="submit">Submit</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = escapeshellarg($_POST["number"]);
        $text = escapeshellarg($_POST["text"]);

        // Ejecutar el script Python
        $output = shell_exec("python3 process.py $number $text 2>&1");

        // Mostrar resultados
        echo "<h2>Results:</h2>";
        echo "<pre>$output</pre>";
    }
    ?>
</body>
</html>
