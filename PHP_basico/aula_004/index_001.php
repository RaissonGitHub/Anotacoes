<?php

// Data types == Tipo de dados

// No PHP as variáveis não são tipadas

// Tipos ESCALARES

// bool/boolean verdadeiro ou falso true/false

// Valores booleanos são apresentados com 1 para true e nada para false
$verdade = true;
$falso = false;

// int/interger interiros sem casas decimais

$valor1 = 0;
$valor2 = 12345667;
$valor3 = -1212334;

// float - valores flutuantes - números com casa decimais

$f1 = 0.342;
$f2 = 3.14;
$f3 = 3423.432;
$f4 = -0.42;

// strings - valores alfanumericos (letras, palavras, frases, textos, ...)

$texto1 = 'Olá, tudo bem?';
$nome1 = 'Jorge';
$sobrenome = 'Thomas';
$letra = 'E';

// Mostando as variáveis

echo $verdade;
echo '<br>';

echo $falso;

echo '<br>';
echo '-------------';
echo '<br>';

echo $valor1;
echo '<br>';

echo $valor2;
echo '<br>';

echo $valor3;

echo '<br>';
echo '-------------';
echo '<br>';

echo $f1;
echo '<br>';

echo $f2;

echo '<br>';
echo $f3;

echo '<br>';
echo $f4;

echo '<br>';
echo '-------------';
echo '<br>';

echo $texto1;

echo '<br>';
echo $nome1;
echo '<br>';
echo $sobrenome;

echo '<br>';
echo $letra;

echo '<br>';
echo '-------------';
echo    '<br>';

// Apresentar o tipo de cada variável

echo gettype($verdade) . '<br>';
echo gettype($valor1) . '<br>';
echo gettype($f1) . '<br>';
echo gettype($texto1) . '<br>';

echo '-------------';
echo    '<br>';

// Apresentar informações da variável
var_dump($verdade);
echo    '<br>';
var_dump($falso);
echo    '<br>';
var_dump($valor2);
echo    '<br>';
var_dump($f1);
echo    '<br>';
var_dump($nome1);
echo    '<br>';



