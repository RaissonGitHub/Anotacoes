//Colocando parametros nas rotas

const express = require('express');
const app = express();
app.listen(3000);



//Parametros podem ser separados, alem de / (barra) por - (hifen) e por . (ponto)
// Mais comum é o / (barra)

//Tres resultados diferentes

app.get('/imprimir/:nome/:sobrenome', (req, res) => {
    res.send('Olá ' + req.params.nome +' ' + req.params.sobrenome)
})

app.get('/imprimir/:nome-:sobrenome', (req, res) => {
    res.send('Hello ' + req.params.nome +' ' + req.params.sobrenome)
})

app.get('/imprimir/:nome.:sobrenome', (req, res) => {
    res.send('Hola ' + req.params.nome +' ' + req.params.sobrenome)
})
