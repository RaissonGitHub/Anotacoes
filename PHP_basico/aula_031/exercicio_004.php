<?php

/* 
    Dada a coleção de nomes, devem ser todos apresentados, 
    mas a partir de maria (inclusive) devem ser com texto vermelho
*/

$nomes = ['joao', 'ana', 'carlos', 'marco', 'maria', 'silva', 'helena', 'ricardo'];
$css = '';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .red {
            color: red;
        }
    </style>
</head>

<body>
    <?php foreach ($nomes as $key => $value) : ?>
        <?php if ($key >= 4) $css = 'red' ?>
        <h3 class="<?= $css ?>"><?= $value ?> </h3>
    <?php endforeach ?>
</body>

</html>