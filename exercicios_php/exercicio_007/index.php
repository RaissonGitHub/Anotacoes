<?php

$nomes = [
    'João Oliveira',
    'Maria Teixeira',
    'José Silva',
    'Ana Santos',
    'Pedro Rodrigues',
    'Paulo Castro',
    'Lucas Dinis',
    'Luiz Matias',
    'Luiza Oliveira',
    'Paula Cardoso',
    'Paulina Fernandes'
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
        <?php foreach ($nomes as $nome) : ?>
            <?php if (strlen($nome) <= 12) : ?>
                <li><?= $nome ?></li>
            <?php endif; ?>
        <?php endforeach; ?>
    </ul>
</body>

</html>