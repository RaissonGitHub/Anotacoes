<?php

$frutas = [
    'Maçã',
    'Laranja',
    'Banana',
    'Pêra',
    'Mamão',
    'Melancia',
    'Melão'
];
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <ul>
        <?php foreach ($frutas as $fruta) : ?>
            <li><?= $fruta ?></li>
        <?php endforeach; ?>
    </ul>
</body>

</html>