<?php


// NULL



$valor= null; // Case insentive

echo "Valor: $valor";
echo '<br>';
var_dump($valor);
echo '<br>';

$valor2 = 100;
echo $valor2;
echo '<br>';
unset($valor2); // Fazendo $valor2 deixar de existir
echo $valor2; // Erro
echo '<br>';

if(is_null($valor)){
    echo 'é nulo';
}

echo '<br>';

if(empty($valor)){
    echo 'é nulo ou vazio';
}