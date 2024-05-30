<?php

// EXPRESSÃO MATCH

// Podemos também analisar m;ultiplas condições de comparação.

$valor = 100;

$resultado =  match(true){
    $valor > 100 => 'valor maior que 100.',
    $valor == 100 => 'valor igual a  100.',
    $valor < 100 => 'valor menor que 100.',
};

echo $resultado;