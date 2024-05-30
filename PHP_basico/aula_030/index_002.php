<?php

// BREAK e CONTINUE

// CONTINUE - permite passar para a iteração seguinte

$nomes = ['joao', 'ana', 'carlos', 'andre', 'ricardo'];
$ignorar = 'ana';
foreach($nomes as $nome){
    if($nome  == $ignorar) continue;
    echo "$nome<br>";
}

