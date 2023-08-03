// Aprimorando exibicao de resultados

const express = require('express');
const mysql = require('mysql2');
const mysql_config = require('./mysql_config'); //Importando as configuracoes da conexao
const functions = require('./fucntions'); //Importando a funcao de resposta 
const app = express();
app.listen(3000, () => {
    console.log('Servidor no ar na porta 3000')
});

//Criando conexao com mysql externo
const connection = mysql.createConnection(mysql_config);//Pega as configuracoes de mysql_config.js

// Utilizando uma estrutura padronizada para exibir os dados e erros
app.get('/', (req, res) => {


    connection.query('SELECT * FROM tasks', (err, results, fields) => {
        if (err) {//Se ouver erro

            //resposta em forma de json utilizando a funcao externa de resposta
            res.json(functions.response('error', 'Erro na tarefa: ' + err.message))
        }
        else {//Se nao ouver erro

            //resposta em forma de json utilizando a funcao externa de resposta
            res.json(functions.response('sucess', 'Sucesso na tarefa', results))//resposta em forma de json
        }
    })

})

