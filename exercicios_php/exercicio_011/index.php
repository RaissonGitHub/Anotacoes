<?php
$valores = [];

while(count($valores)<20){
    $r = rand(1,100);
    if(!(in_array($r,$valores)) && $r % 10 !=0){
            $valores[] = $r;
    }
}
sort($valores);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php foreach($valores as $valor) : ?>
        <p><?=$valor?></p>
    <?php endforeach; ?>
</body>
</html>