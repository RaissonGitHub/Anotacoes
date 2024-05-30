<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php for($i = 20; $i>0; $i--)  : ?>
        <?php $r = rand(1,100) ?>
        <?= "$r x 3 = ". $r*3 . "<br>"?>
        <?php endfor; ?>
</body>
</html>