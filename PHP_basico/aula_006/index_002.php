<?php

// Inteiros - INT

// os valores são comumente definidos com números 

$valor1 = 100; 
echo $valor1 . '<br>';

// mas podem ser definidos com valores hexadecimais

$valor2 = 0xa3;
echo $valor2 . '<br>';

// ou ainda sistema octal

$valor3 = 045;
echo $valor3 . '<br>';

// ou ainda com sistema binário

$valor4 = 0b101;

echo $valor4 . '<br>';

// O que acontence se passar o valor máximo de um inteiro?

$valor_ultrapassado =  PHP_INT_MAX + 1;
echo $valor_ultrapassado . '<br>';
var_dump($valor_ultrapassado);
echo '<br>';

// passou a ser do tipo float com casas decimais

