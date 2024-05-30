<?php

$f = fopen('dados.txt', 'w');
$total = rand(300,4500);
for($i=0; $i<$total; $i++)
{
    if($i < $total - 1)
        fputs($f, $i . '-'. uniqid() . PHP_EOL);
    else
        fputs($f, $i . '-'. uniqid());
}
fclose($f);