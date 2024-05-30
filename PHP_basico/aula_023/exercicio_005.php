<?php

/* 
    Uma empresa tem várias lojas, cada uma com um endereço de email.
    A varável $cidade indica que dados de email deverão ser apresentados. 
    Constrói a lógica condicional e de apresentação do email correspondente
    quando é alterado o valor da cidade escolhida.
*/

$lojas = [
    'lisboa' => 'lisboa@gmail.com',
    'porto' => 'porto@gmail.com',
    'coimbra' => 'coimbra@gmail.com'
];

$cidade = 'porto';

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php if(key_exists($cidade,$lojas)) : ?> 
        <p><?=$lojas[$cidade]?></p>
    <?php else :?>
        <p>Loja não encontrada</p>
    <?php endif; ?>
</body>
</html>