<?php

// OPERADOR TERNÁRIO
$erro = false;

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .erro {
            background-color: red;
            color: white;
        }
    </style>
</head>

<body>
    <div class="<?= $erro ? 'erro' : '' ?>">Resultado</div>
    <!-- 
        O mesmo que:
        <div class"erro">Resultado</div>
     -->
</body>

</html>