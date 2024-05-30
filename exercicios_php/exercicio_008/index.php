<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php for ($i = 2; $i < 7; $i++) : ?>
        <?php for ($m = 0; $m < 11; $m++) : ?>
            <p><?= "$i x $m = " . $i * $m ?></p>
        <?php endfor; ?>
        <?= $i <6 ? '<hr>' : '' ?>
    <?php endfor; ?>
</body>

</html>