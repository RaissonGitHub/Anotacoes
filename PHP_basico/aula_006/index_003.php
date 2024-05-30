<?php

// Inteiros - INT

// Podemos transformar variáveis fazendo 'cast' para inteiros

$valor_str = "145";
$valor_int= (int)$valor_str;

//ou 

$valor_int1= (integer)$valor_str;

echo $valor_int . '<br>';
echo $valor_int1 . '<br>';

// Conversão de string para inteiro

echo (int)100;
echo '<br>';
echo (int)'25teste'; // O texto é ignorado, converte 25
echo '<br>';
echo (int)'teste'; //retorna 0
echo '<br>';

//  Podemos verificar se uma variável é inteira
$final = 'a';
var_dump(is_int($final));
echo '<br>';
$final = 1;
var_dump(is_int($final));
echo '<br>';

// Ainda podemos definir um valor inteiro dessa forma

$outra_valor = 1_500_000;
echo $outra_valor;
