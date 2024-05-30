<?php

$nomes = ['João',
'Maria',
'José'];

$apelidos = ['Silva',
'Teixeira',
'Oliveira'];

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
        <?php for($i = 0; $i < count($nomes); $i++): ?>
            <li><?=$nomes[$i] . ' ' . $apelidos[$i] ?></li>
        <?php endfor; ?>
    </ul>
</body>
</html>