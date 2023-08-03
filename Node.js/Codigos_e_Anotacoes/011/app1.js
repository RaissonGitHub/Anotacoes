//Lidando com banco de dados mysql2
//Com o express e mysql2 instalado

const express = require('express');
const mysql = require('mysql2');//Importando o mysql2

const app = express();
app.listen(3000, () => {
    console.log('Servidor no ar na porta 3000')
});

//Criando conexao com mysql
// Crie uma conexao com mysql.createConnection()
// Passe um objeto com propriedades host,user,password e database com seus respectivos nomes
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'doge',
    password: '12345678',
    database: 'nodejs_tasks'
});

// Estabelecendo a conexao e verificando erros

// connect(), quando usada com outras funcoes como query() que possui verificacao de erros,
// passa a ser redundante

connection.connect(error => {
    if (error) {//Se houver erro
        console.log('Erro na conexao ao MYSQL' + error.stack)//Exiba o erro
        return
    }
    //Se nao 
    console.log('Conexao com sucesso')
});

//Usando com rotas
app.get('/', (req, res) => {
    //query() executa um comando sql
    // Passe o comando e uma funcao callback com err, results e fields
    connection.query('SELECT * FROM tasks', (err, results, fields) => {
        if (err) { //Se houver erro
            console.log(err)//Exiba o erro
            res.send('Erro na consulta')//Exiba uma mensagem
        }
        else {//Se nao 
            res.send(results)//Exiba os resutados
        }
    })
})

