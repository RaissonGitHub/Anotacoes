//Enviando paginas html como resposta

const fs = require('fs');
const http = require('http');
const host = 'localhost';
const port = 3000;

const server = http.createServer((req,res)=>{ // criando a conexao

    res.setHeader('Content-Type', 'text/html') //definindo o header para html

    fs.readFile('./html/index.html', (err,data) =>{ //lendo o arquivo
        if(err){ //para erros
            console.log(err) //escreva o erro 
            res.write('Erro!') // na pagina escreva Erro!
            res.end() // termine com a resposta
        }
        else{ //se nao houver erros
            res.write(data) //escreva a pagina
            res.end() // termine com a resposta
        }
    })
    
});

server.listen(port,host, ()=>{ //porta que sera ouvida, host e mensagem de execucao
    console.log('Servidor iniciado na porta 3000!')
})