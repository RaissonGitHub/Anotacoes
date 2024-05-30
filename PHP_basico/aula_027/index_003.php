<?php

$valor1 = 1;
$valor2 = 1;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- While -->
    <?php while ($valor1<=10) : ?>
        <h3>Valor = <?= $valor1++?></h3>
    <?php endwhile; ?>

    <!-- Do while -->
    <?php do {?>
        <h3><?= $valor2++ ?></h3>
    <?php } while ($valor2<+11);?>
    <!-- Não há endwhile -->
</body>
</html>