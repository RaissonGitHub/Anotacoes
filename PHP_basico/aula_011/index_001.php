<?php

//  ARRAYS MULTIDIMENSIONAIS
// arrays com outros arrays

$lojas = [
    'porto' => [
        'email' => 'porto@gmail.com',
        'telefone' => '1223123'
    ],
    'lisboa' => [
        'email' => 'lisboa@gmail.com',
        'telefone' => '12123123'    
    ],
    'coimbra' => [ 
        'email' => 'coimbra@gmail.com',
        'telefone' => '121'    
    ]
];

echo '<pre>';
print_r($lojas);
echo '</pre>';

// Apresentar um valor específico
echo $lojas['coimbra']['telefone'];

// Nos arrays com indices númericos também podemos ter multidimensão

$notas = [
    [10,20,30],
    [100,200,300],
    [1000,2000,3000]
];

echo '<pre>';
print_r($notas);
echo '</pre>';

echo $notas[2][0]; // 1000