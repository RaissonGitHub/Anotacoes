<?php

// alterar o nome da sessão
session_name('minha_sessao');

// definir o periodo de duração dos cookies
session_set_cookie_params(60*15);

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