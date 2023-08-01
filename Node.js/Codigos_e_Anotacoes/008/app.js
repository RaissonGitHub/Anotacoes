//Enviando arquivos como resposta com express

const express = require('express');
const app = express();

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000!')
})

//Defina a porta e a funcao callback
//Use sendFile()
// Como parametro coloque o caminho absoluto do arquivo
// Pode concatenar  __dirname com o arquivo
// OU
// Passar um objeto com atributo root:__dirname

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/views/index.html')
})

app.get('/about', (req, res) => {
    res.sendFile('./views/about.html', { root: __dirname })
})

//Redirecionamento

app.get('/sobre', (req,res)=>{
    res.redirect('/about') // Use a funcao redirect e defina a porta para redirecionar
})

// Para pagina nao encontrada
app.use((req, res) => {
    res.status(404).sendFile('./views/404.html', { root: __dirname })
})
