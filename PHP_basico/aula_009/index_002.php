<?php

    // STRINGS

    // Outras formas de definir strings (menos usadas) são:

    // Heredoc

    $texto1 = <<<TEXT
    frase1
    frase2
    frase3
    TEXT;

    echo $texto1; // as linhas irão aparecer sem quebras

    echo nl2br($texto1); // as linhas irão aparecer com quebras

    // Nowdoc

    $texto = <<<'TEXT'
    frase1
    frase2
    frase3
    TEXT;