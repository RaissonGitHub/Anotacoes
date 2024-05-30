<?php

// ARRAYS

$nome1 = 'João';
$nome2 = 'Ana';
$nome3 = 'Claudio';

$nomes = array('João', 'Ana', 'Claudio');
// ou 

$nomes = ['João', 'Ana', 'Claudio'];

// como consultar cada elemento

echo $nomes[0]; // primeiro elemento

// Podemos definir nossas próprias chaves

$nome = [
    10 => 'João', 
    20 => 'Ana',
    30 => 'Carlos'
];

echo $nomes[20];

// Se tentar consultar uma chave qu e não existe surgirá um aviso

echo $nomes[19];

// Para verrificar se o item existe

var_dump(isset($nomes[200]));

// Podemos alterar os valores de um array

$nomes[1] = 'Fernanda';

// Podemos ver um array com var_dump

var_dump($nomes);

// ou de uma forma mais fácil de ler

echo '<pre>';
print_r($nomes);
echo '<pre>';
