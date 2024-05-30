<?php
// alterar o nome da sessão
session_name('minha_sessao');

// definir o periodo de duração dos cookies
session_set_cookie_params(60*15);
session_start();
unset($_SESSION['apelido']); // destruir uma chave da sessão
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
    <h2>Valor de 'apelido' removido da sessão.</h2>
</body>

</html>