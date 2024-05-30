<?php
session_start();
$_SESSION['nome'] = 'João';
// se o indice 'nome' já existe ele será reatribuido a João
// se não existe ele é criado
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php require_once 'nav.php' ?>
    <hr>
    <h2>Valor de 'nome' adicionado à sessão.</h2>
</body>

</html>