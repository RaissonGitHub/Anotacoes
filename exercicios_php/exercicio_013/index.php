<?php

$profissoes = [
    'Programador',
    'Designer',
    'Engenheiro',
    'Médico',
    'Advogado',
    'Professor',
    'Bombeiro',
    'Policial',
    'Piloto',
    'Cientista'
];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
<body>
    
<table class="table table-dark table-striped table-bordered">
<thead>
    <tr>
        <th>Profissão</th>
        <th>Em maiúsculas</th>
        <th>Em minúsculas</th>
        <th>Primeiras 4 letras</th>
        <th>Total caracteres</th>
    </tr>
</thead>
<tbody>
    <?php foreach($profissoes as $profissao) : ?>
        <tr>
            <td><?=$profissao?></td>
            <td><?=mb_strtoupper($profissao)?></td>
            <td><?=mb_strtolower($profissao)?></td>
            <td><?=substr($profissao,0,4)?></td>
            <td><?=strlen($profissao)?></td>
        </tr>
    <?php endforeach; ?>
</tbody>
</table>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>
</body>
</html>