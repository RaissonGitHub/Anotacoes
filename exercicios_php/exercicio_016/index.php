<?php


if(($argc) >= 3){
    if(is_numeric($argv[1]) && is_numeric($argv[2])){
        echo "{$argv[1]} + {$argv[2]} = " . $argv[1] + $argv[2];
        die();
    }
}
echo 'Erro!';
die(1);