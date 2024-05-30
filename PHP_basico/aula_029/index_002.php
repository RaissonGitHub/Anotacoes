<?php

// LOOP FOREACH

// PHP com HTML
$nomes = ['joao', 'ana', 'carlos', 'andre', 'ricardo'];

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div>
        <?php foreach ($nomes as $nome) : ?>
            <h3><?= $nome ?></h3>
        <?php endforeach; ?>
    </div>
</body>

</html>