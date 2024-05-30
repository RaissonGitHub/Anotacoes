<?php
// Neste exemplo muito simples, vamos usar um cookie 
// para definir o tema claro ou escuro do nosso site.

// verifica se existe um cookie com o tema
$theme = !empty($_COOKIE['theme']) ? $_COOKIE['theme'] : 'light';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            margin: 0;
            padding: 0;
        }
        .light{
            background-color: white;
            color: black;
        }
        .dark{
            background-color: black;
            color: white;
        }
        a{
            color: red;
        }
    </style>
</head>
<body class="<?= $theme?>">
    <a href="theme_dark.php">Dark Mode</a>| <a href="theme_light.php">Light mode</a>
    <h1>Exemplo simples de tema com cookie</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque, excepturi accusantium quidem vel dolorum obcaecati magni temporibus vero consequuntur nemo.</p>
</body>
</html>