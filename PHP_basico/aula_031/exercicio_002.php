<?php
/* 

1. Construa um array com todos os resultados da tabuada dos 327.
2. Apresetna os dados do arry com um ciclo foreach (apenas os valores)

*/

$tabuada = [];

for ($i = 0; $i <= 10; $i++) {
    $tabuada[] = $i * 327;
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php foreach ($tabuada as $n) : ?>
        <h3><?= $n ?></h3>
    <?php endforeach; ?>
</body>

</html>