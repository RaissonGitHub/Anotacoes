<?php

/* 
    Vamos simular uma mensagem de erro. 
    Se a variável eero tiver conteúdo dentro dela, deverá ser
    apresentada a mensagem de erro.
    Caso contrário, se a mensagem de erro estiver vazia, deverá 
    aparecer a mensagem 'SUCESSO'.
*/

$mensagem_erro = 'Erro aconteceu';
$mensagem = null;
if(!empty($mensagem_erro)){
    $mensagem = $mensagem_erro;
} else{
    $mensagem = 'SUCESSO';
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
    <?= $mensagem ?>
</body>

</html>