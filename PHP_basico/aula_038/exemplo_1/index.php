<?php

// todos os scripts devem ter o inicio de sessão,
// antes de qualquer output do PHP
session_start();

// variáveis que vão ser apresentadas nesta página
// o valor de $nome e $apelido vai ser definido tendo
// em atenção à exesitencia ou não das variáveis na super global $_SESSION
$nome = !empty($_SESSION['nome']) ? $_SESSION['nome'] : '-';
$apelido = !empty($_SESSION['apelido']) ? $_SESSION['apelido'] : '-';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php require_once 'nav.php'?>
    <hr>
    <h2>Exercício com sessões de PHP</h2>
    <h3>Valor da variável 'nome':</h3>
    <h1><?= $nome?></strong></h1>
    <h3>Valor da variável 'apelido':</h3>
    <h1><?= $apelido?></h1>

</body>
</html>