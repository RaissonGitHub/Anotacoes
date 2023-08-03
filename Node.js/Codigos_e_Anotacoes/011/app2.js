//Lidando com banco de dados mysql2 externo
//Com o express e mysql2 instalado

const express = require('express');
const mysql = require('mysql2');//Importando o mysql2
const mysql_config = require('./mysql_config'); //Importando as configuracoes da conexao

const app = express();
app.listen(3000, () => {
    console.log('Servidor no ar na porta 3000')
});

//Criando conexao com mysql externo
const connection = mysql.createConnection(mysql_config);//Pega as configuracoes de mysql_config.js


app.get('/', (req, res) => {
    
    connection.query('SELECT * FROM tasks', (err, results, fields) => {
        if (err) { 
            console.log(err)
            res.send('Erro na consulta')
        }
        else {
            res.send(results)
        }
    })
})

