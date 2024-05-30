<?php

// FUNÇÕES ASSOCIADAS AOS ARRRAYS

$nomes = ['Jorge', 'Ana', 'Felipe', 'Joaquim'];

// Saber se uma variável é um arrray

$resultado = is_array($nomes); // true

// Saber quantos elementos tem um array

$resultado = count($nomes); // 4

// Adicionar valores no final do array

array_push($nomes, 'Fernanda', 'Matheus');

// Adicionar valores no inicio do array

array_unshift($nomes,'Bianca');

// Retirar um valor do final do array

$resultado = array_pop($nomes); // Matheus

print_r($nomes);

// Retirar um valor do inicio do array

$resultado = array_shift($nomes); // Bianca

// Eliminar determinado elemento pelo indice

unset($nomes[2]); // Remove o 3 elemento do array 
