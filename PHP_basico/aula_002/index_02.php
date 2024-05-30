<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .cor_texto{
            color: red;
        }
    </style>
</head>
<body>
    <h1>O meu nome é João</h1>
    <!-- O php utilizado em uma parte do código fica visível por todo ele -->
    <?php 
    $nome = 'João Ribeiro'
    ?>
    <h3>O meu nome é <?php echo $nome?>!</h3>
    <h3>O meu nome é <?= $nome?>!</h3>
    <!-- Escrever HTML a partir do php -->
    <?php
        echo '<p>Vamos criar um parágrafo de HTML</p>';
        echo '<p class="cor_texto">Este parágrafo possui uma classe CSS.</p>';
    ?>
</body>
</html>