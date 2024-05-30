<?php
$valores = [
    'nome' => 'João',
    'idade' => 20,
    'altura' => 1.80,
    'peso' => 80,
    'profissão' => 'Programador'
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
    <?php foreach($valores as $key => $valor) : ?>
        <p><?=ucfirst($key) . " = " . $valor?></p>
    <?php endforeach; ?>
</body>
</html>