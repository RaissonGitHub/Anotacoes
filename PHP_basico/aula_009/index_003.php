<?php

    // STRINGS

    // Heredoc e Nowdoc podem ser um recurso interessante para textos mais longos

    $valor1 = 100;
    $valor2 = 200;
    $valor3 = 300;

    $relatorio = <<<TEXT
    O valor 1 = $valor1
    O valor 2 = $valor2
    O valor 3 = $valor3
    TEXT;

    echo nl2br($relatorio);

    // Ou para apresentar HTML

    $html = <<<TEXT
    <h1>Título</h1>
    <hr>
    <p>Texto adoadofofijaodfj</p>
    TEXT;

    echo $html;