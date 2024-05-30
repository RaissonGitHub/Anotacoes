<?php

    // STRINGS

    // Funções nativas do PHP que envolvem Strings

    $frase = 'Lorem ipsum dolor sit amet consectetur adipisicing elit.';

    /* Apresentar número de caracteres de uma string */

    echo strlen($frase) . "<br>";

    /* Transformar todas as letras em maiúsculas */

    echo strtoupper($frase) . "<br>";

    /* Apresentar apenas parte da frase */

    echo substr($frase,0,20) . "<br>";

    /* Verfica se uma palavra existe dentro da string */

    echo str_contains($frase, 'consectetur');
    

