// Passando resultados em json

const express = require('express');
const mysql = require('mysql2');
const mysql_config = require('./mysql_config'); //Importando as configuracoes da conexao

const app = express();
app.listen(3000, () => {
    console.log('Servidor no ar na porta 3000')
});

//Criando conexao com mysql externo
const connection = mysql.createConnection(mysql_config);//Pega as configuracoes de mysql_config.js

// Utilizando uma estrutura padronizada para exibir os dados e erros
app.get('/', (req, res) => {
    // Criando a estrutura que sera exibida
    let result = {
        status:'sucess',
        mensage:null,
        data:null
    }
    connection.query('SELECT * FROM tasks', (err,results,fields)=>{
        if(err){//Se ouver erro
            result.status = 'error'
            result.mensage = 'Erro na consulta'
            result.data = []//exibe nada
            res.json(result)//resposta em forma de json
        }
        else{//Se nao ouver erro
            result.status = 'sucess'
            result.mensage = 'Sucesso ao obter as tarefas'
            result.data = results//exibe os resultados
            res.json(result)//resposta em forma de json
        }
    })
    
})

