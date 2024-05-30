<?php

// ARRAYS

// Como adicionar e remover valores de um array

$nomes = ['Ana', 'Claudio', 'Leo'];

// adicionar (push)
$nomes[] = 'Novo nome';
// $nomes = ['Ana', 'Claudio', 'Leo', 'Novo nome'];

// ou

array_push($nomes,'Pedro');
// mais de um valor
array_push($nomes,'Amanda', 'Alana', 'Alan');

// Remover elementos (a chave vai desaparecer)

unset($nomes[5]);
echo '<pre>';
print_r($nomes);
echo '<pre>';