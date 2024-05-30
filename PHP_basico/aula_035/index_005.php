<?php


// INCLUDE e REQUIRE

/* 
Imagine um cenário onde tens um conjunto de dados considerável
e queres definir isso dentro de um script à parte.
Também é possível seguindo o seguinte exemplo:
*/

$nomes = require_once('dados.php');

echo '<pre>';
print_r($nomes);