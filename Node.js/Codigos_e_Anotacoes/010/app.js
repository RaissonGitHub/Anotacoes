//Colocando parametros nas rotas

const express = require('express');
const app = express();
app.listen(3000);

app.get('/', (req, res) => {
    res.send('Home')
})
// Parametros sao declarados na rota com :nome_parametro
// Parametros sao armazenados em req.params

app.get('/imprimir/:nome', (req, res) => {
    res.send(req.params.nome)
})
//Na url coloque: http://localhost:3000/imprimir/Jubileu
//Retorna na pagina Jubileu

//Dois parametros
app.get('/imprimir/:nome/:sobrenome', (req, res) => {
    res.send('Olá ' + req.params.nome +' ' + req.params.sobrenome)
})
//Na url coloque: http://localhost:3000/imprimir/Jubileu/Silva
//Retorna na pagina: Olá Jubileu Silva

//Exemplo: soma de parametros

app.get('/soma/:a/:b', (req,res)=>{
    res.send('A soma entre '+ req.params.a+ ' e '+ req.params.b+' é = ' + (parseInt(req.params.a)+ parseInt(req.params.b)))
})
// parseInt para mudar de string para number
