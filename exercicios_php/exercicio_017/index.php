<?php

$inicio = microtime(true);
for($i = 0; $i<30000 ; $i++){
    echo $i . PHP_EOL;
}
$fim = microtime(true);
$resultado = $fim - $inicio;
$resultado = round($resultado,3, PHP_ROUND_HALF_UP);
echo "Tarefa concluída em: $resultado segundos ";