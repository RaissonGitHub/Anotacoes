<?php

/* 
Construa uma apresentação em HTML que mostre a tabuada do 5.

*/

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php for ($i = 0; $i <= 10; $i++) : ?>
        <p>5 x <?= $i ?> = <?= $i * 5 ?></p>
    <?php endfor; ?>
</body>

</html>