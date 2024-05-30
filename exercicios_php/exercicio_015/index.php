<?php

if(!(empty($argv[1]))){
    if($argv[1] == 'run'){
        echo 'Sucesso' . PHP_EOL;
        die();
    }
}
echo 'Erro! ' . PHP_EOL;