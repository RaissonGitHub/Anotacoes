<?php

/* 
    Constrói a lógica condicional que permite apresentar apenas
    o parágrafo correspondente ao valor da varável $nome
*/

$nome = 'João';
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php if ($nome == 'João') : ?>
        <p>O nome é João</p>
    <?php elseif ($nome == 'Ana') : ?>
        <p>O nome é Ana</p>
    <?php elseif ($nome == 'Carlos') : ?>
        <p>O nome é Carlos</p>
    <?php else : ?>
        <p>Nome desconhecido</p>
    <?php endif; ?>
</body>

</html>