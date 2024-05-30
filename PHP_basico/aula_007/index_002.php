<?php
 
// FLOATS

// Assim como os inteiros os floats possuem valores diferentes para as plataformas 32 e 64 bits

echo PHP_FLOAT_MIN  . '<br>';
echo PHP_FLOAT_MAX  . '<br>';

// Infinity - INF - é um valor muito alto para ser mostrado

$valor = PHP_FLOAT_MAX *2;

echo $valor;
echo "<br>";
var_dump($valor);
echo "<br>";

// Converter para float

$valor = 10;
$valor_float = (float)$valor;
echo $valor_float;
echo "<br>";
var_dump($valor_float);
echo "<br>";

// ou ainda

$valor = 20;
$valor_float = floatval($valor);
echo $valor_float;
echo "<br>";
var_dump($valor_float);
