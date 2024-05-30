<?php

// FUNÇÕES ASSOCIADAS AOS ARRRAYS

$empresa = [
    'ceo' => 'joao',
    'administrador' => 'ana',
    'executivo' => 'claudio',
    'contabilista' => 'felipe'
];

// Apresentar um valor de array associativo

echo $empresa['administrador'];

// Verificar se existe uma determinada chave no array

var_dump(key_exists('funcionario',$empresa));// bool/false

// Array para String

$resultado = implode(',',$empresa); // "joao,ana,claudio,felipe"

var_dump($resultado);

// Criar um outro array a partir de uma porção de outro array

$nomes = ["joao","ana","claudio","felipe"];
$nomes_parte = array_slice($nomes,2); //"cluadio", "felipe" 