<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST["number"];
    $text = $_POST["text"];

    // Call Python script with user input
    $output = shell_exec("python3 process.py " . escapeshellarg($number) . " " . escapeshellarg($text));

    // Display results
    echo "<h2>Results:</h2>";
    echo nl2br(htmlspecialchars($output));
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Treasure Hunt</title>
</head>
<body>
    <h2>Enter Your Details</h2>
    <form method="post">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required><br><br>

        <label for="text">Enter a text message:</label>
        <input type="text" id="text" name="text" required><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
