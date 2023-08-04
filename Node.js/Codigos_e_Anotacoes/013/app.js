// Acoes no banco de dados com nodejs

// Imports
const express = require('express');
const mysql = require('mysql2');
const mysql_config = require('./mysql_config');
const functions = require('./functions');
const cors = require('cors')
const app = express();

// Server listen
app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000')
})

// MYSQL connection
const connection = mysql.createConnection(mysql_config);

// middlewares config
app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(cors())

//-----------------------------------------------

//Acoes

// Listar tudo de uma tabela
app.get('/listar', (req, res) => {
    // Coloque a querry e uma funcao callback com err e rows 
    // (rows servirao como as linhas afetadas e os dados)
    connection.query('SELECT * FROM tasks', (err, rows) => {
        //Se houver erro
        if (err) {
            //Envie a resposta com o erro
            res.json(functions.response('error', err.message, 0, null))
        }
        //Se nao houver erro
        else {
            //Envie a resposta com sucesso
            res.json(functions.response('Sucess', 'Sucesso na tarefa', rows.length, rows))
        }
    })
})

//Listar por elemento especifico
app.get('/listar/:id', (req, res) => {
    const id = req.params.id
    // Coloque a query normalmente, o campo especifico coloque como ?
    // Apos a querry passe uma lista com o valor que ira para o campo especifico
    connection.query('SELECT * FROM tasks WHERE id = ?', [id], (err, rows) => {
        //Se nao houver erro
        if (!err) {
            //Se retornar dados
            if (rows.length > 0) {
                //Envie a resposta com sucesso
                res.json(functions.response('Sucess', 'Sucesso na tarefa', rows.length, rows))
            }
            //Se nao retornar dados
            else {
                //Envie a resposta com o erro
                res.json(functions.response('error', "task not found", 0, null))
            }
        }
        //Se houver erro
        else {
            //Envie a resposta com o erro
            res.json(functions.response('error', err.message, 0, null))
        }
    })
})

// Atualizar elementos
app.put('/update/:id/task/:task', (req, res) => {
    const id = req.params.id
    const task = req.params.task
    // Coloque a query normalmente, os campos especificos coloque como ?
    // Apos a querry passe uma lista com os valores que irao para os campos especificos
    // A lista deve ser organizada na forma em que ? sera substituido
    // task substituira o 1 ? e id substituira o 2 ?
    connection.query('UPDATE tasks SET task = ? WHERE id = ?', [task, id], (err, rows) => {
        //Se nao houver erro
        if (!err) {
            //Se retornar dados
            if (rows.affectedRows > 0) {
                //Envie a resposta com sucesso
                res.json(functions.response('Sucess', 'Sucesso na tarefa', rows.affectedRows, null))
            }
            //Se nao retornar dados
            else {
                //Envie a resposta com o erro
                res.json(functions.response('error', "task not found", 0, null))
            }
        }
        //Se houver erro
        else {
            //Envie a resposta com o erro
            res.json(functions.response('error', err.message, 0, null))
        }
    })
})

// Deletar de uma tabela
app.delete('/delete/:id', (req, res) => {
    const id = req.params.id
    // Coloque a query normalmente, o campo especifico coloque como ?
    // Apos a querry passe uma lista com o valor que ira para o campo especifico
    connection.query('DELETE FROM tasks WHERE id = ?', [id], (err, rows) => {
        //Se nao houver erro
        if (!err) {
            //Se retornar dados
            if (rows.affectedRows > 0) {
                //Envie a resposta com sucesso
                res.json(functions.response('sucess', 'task deleted', rows.affectedRows, null))
            }
            //Se nao retornar dados
            else {
                //Envie a resposta com o erro
                res.json(functions.response('error', 'task not found', 0, null))
            }
        }
        //Se houver erro
        else {
            //Envie a resposta com o erro
            res.json(functions.response('error', err.message, 0, null))
        }
    })
})

// Inserir dados em uma tabela
app.post('/insert', (req, res) => {
    const post_data = req.body
    //Verificando se os dados estao validos
    if(post_data == undefined){
        //Envie a resposta com o erro
        res.json(functions.response('error','Empty data',0,null))
    }
    //Verificando se os atributos estao validos
    if(post_data.task == undefined|| post_data.status == undefined){
        //Envie a resposta com o erro
        res.json(functions.response('error','Invalid data',0,null))     
    }
    
    const task = post_data.task
    const status = post_data.status

    // Coloque a query normalmente, o campo especifico coloque como ?
    // nao esqueca de definir os campos da tabela tambem como ex: (task,status,created_at,updated_at)
    // Apos a querry passe uma lista com o valor que ira para o campo especifico
    connection.query('INSERT INTO tasks (task,status,created_at,updated_at) VALUES ( ?, ?, NOW(), NOW() )', [task,status], (err, rows) => {
        //Se nao houver erro    
        if (!err) {
            //Envie a resposta com sucesso
            res.json(functions.response('sucess', 'task created', rows.affectedRows, null))
        }
        //Se houver erro
        else {
            //Envie a resposta com o erro
            res.json(functions.response('error', err.message, 0, null))
        }
    })
})

//-----------------------------------------------

// Rota nao encontrada
app.use((req,res)=>{
    //Envie a resposta com o erro
    res.json(functions.response('Error','Route not found',0,null))
})

