<?php

/* 
    Dada a coleção de nomes, apresente toda a coleção exceto o nome cujo 
    índice = 4 (maria)
*/

$nomes = ['joao', 'ana', 'carlos', 'marco', 'maria', 'silva', 'helena', 'ricardo'];

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php foreach($nomes as $key => $value) : ?>
        <?php if ($key == 4) continue; ?>
        <h3><?= $value ?></h3>
    <?php endforeach; ?>
</body>

</html>