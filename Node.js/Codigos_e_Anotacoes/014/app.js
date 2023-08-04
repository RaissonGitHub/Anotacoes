const express = require('express');
const bodyParser = require('body-parser')
const app = express();

// Definindo o ejs como emplate engine
// permitindo renderizar as páginas HTML dinamicamente
app.set('view engine', 'ejs')

// Permitir a comunicacao com formularios
app.use(bodyParser.urlencoded({extended:false}))//false para nao tratar com array e objetos

// Inicializacao 
app.listen(3000,()=>{
    console.log('Servidor no ar na porta 3000')
})

//Use get para acessar as paginas
app.get('/', (req,res)=>{
    res.sendFile('./views/index.html', {root:__dirname})
})

//Use post para enviar informacoes de formulario
app.post('/envio', (req,res)=>{
    // Para pegar os dados use req.body.nome_campo_html
    const mensage = req.body.mensagem 
    
    // Use render para enviar uma pagina dinamica
    // Se quiser exportar informacoes passe-as em um objeto
    // render('pagina',{objeto:valores})
    res.render('dinamica',{mensagem:mensage})
})