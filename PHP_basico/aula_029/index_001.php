<?php

// LOOP FOREACH

/* 

É a melhor opção para iterações em arrays ou objetos. 
foreach([array] as $value ou $key=>$value){
    #código
}

*/

$nomes = ['joao', 'ana', 'carlos', 'andre', 'ricardo'];
foreach($nomes as $nome){
    echo "$nome<br>";
}

echo '<hr>';

$posicoes = [
    'administrador' => 'joao',
    'secretario' => 'ana',
    'colaborador' => 'carlos',
    'gerente' => 'andre',
    'zelador' => 'ricardo'
];

foreach($posicoes as $chave=>$valor){
    echo "Com a posição de $chave, temos a seguinte pessoa: $valor<br>";
}

// no final da execução, a varável $valor e a $chave vão permanecer dispníveis
echo "<hr>$valor<br>$chave";