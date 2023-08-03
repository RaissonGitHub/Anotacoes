// Usando o cors em APIS

// cors garante que nao acontecam erros quando trabalhar com APIS e
// fizer um pedido atraves de uma entidade externa para um endereco especifico


const express = require('express');
const mysql = require('mysql2');
const mysql_config = require('./mysql_config');
const functions = require('./fucntions');
const cors = require('cors')


const app = express();
app.listen(3000, () => {
    console.log('Servidor no ar na porta 3000')
});
// cors() atua como middleware para todas as rotas
// pode definir whitelists e blacklist para controle
app.use(cors()); 
// Nesse caso qualquer API pode acessar as rotas

const connection = mysql.createConnection(mysql_config);//Pega as configuracoes de mysql_config.js

app.get('/', (req, res) => {
    connection.query('SELECT * FROM tasks', (err, results, fields) => {
        if (err) {
            res.json(functions.response('error', 'Erro na tarefa: ' + err.message))
        }
        else {
            res.json(functions.response('sucess', 'Sucesso na tarefa', results))//resposta em forma de json
        }
    })
})

//Para rotas especificas
app.get('/rota', cors(), (req, res) => {
    connection.query('SELECT * FROM tasks', (err, results, fields) => {
        if (err) {
            res.json(functions.response('error', 'Erro na tarefa: ' + err.message))
        }
        else {
            res.json(functions.response('sucess', 'Sucesso na tarefa', results))//resposta em forma de json
        }
    })
})