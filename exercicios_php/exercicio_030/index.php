<?php
?>
<!DOCTYPE html>
<html lang="pt">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../assets/bootstrap/bootstrap.min.css">
</head>

<body>

    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-sm-4">
                <form action="login.php" method="post">
                    <div class="mb-3">
                        <input type="email" name="text_usuario" class="form-control" placeholder="Usuario">
                    </div>
                    <div class="mb-3">
                        <input type="password" name="text_senha" class="form-control" placeholder="Senha">
                    </div>
                    <div class="mb-3 text-center">
                        <input type="submit" value="Entrar" class="btn btn-primary">
                    </div>
                </form>
            </div>
        </div>
    </div>

    <script src="../assets/bootstrap/bootstrap.bundle.min.js"></script>

</body>

</html>