<?php 

// BREAK e CONTINUE

// BREAK com vários níveis

/* 
Imagine um cenário em que temos que executar dois loops, um dentro do outro.
O ciclo interior encontra uma condição para ser interrompido. 
Queremos que o ciclo interior e o exterior sejam interrompidos.
*/

$paises = [
    'Portugal' => ['Lisboa', 'Porto', 'Coimbra'],
    'Brasil' => ['Brasília', 'São Paulo', 'Acre'],
    'Angola' => ['Luanda', 'Cabinda', 'Huambo'],
    'Moçambique' => ['Maputo', 'Matola', 'Nampula'],
];

foreach($paises as $pais =>$cidades){
    echo "<h3><ul>$pais</ul></h3>";

    foreach($cidades as $cidade){
        // vamos parar os dois ciclos quando a cidade é Cabinda
        if($cidade == 'Cabinda') break 2;
        echo "<p>$cidade</p>";
    }
}

