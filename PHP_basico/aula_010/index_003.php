<?php

// ARRAYS

// Indicies também podem ser alfanuméricos

$empresa = [
    'ceo' => 'joao',
    'administrador' => 'ana',
    'executivo' => 'claudio',
    'contabilista' => 'felipe'
];

echo '<pre>';
print_r($empresa);
echo '</pre>';

// Para apresentar os valor utilizamos a chave

echo $nome["ceo"];

// Podemos adicionar mais valores
$empresa['operario'] = 'antonio';

echo '<pre>';
print_r($empresa);
echo '</pre>';
