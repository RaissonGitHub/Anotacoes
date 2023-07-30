# Comandos Node.js

## Criar um servidor web

```
const http = require('http');

const server = http.createServer((request,response) => {
    response.end('Teste')
}).listen(3000,function(){
    console.log('Servidor rodando na porta 3000')
})
```

`const http = require('http');` 

O que faz:

Carrega o modulo http.

```
const server = http.createServer((request,response) => {
    response.end('Teste')
})
``` 

O que faz:

Cria uma conexão atraves do metodo `createServer()` que possui uma arrow function com dois parametros:request ou req e response ou res.

request: Representa a requisição feita pelo cliente ao servidor. 

response: Representa a resposta que o servidor enviará de volta ao cliente.

`response.end('Teste')` envia o texto "Teste" quando a página é carregada.

```
server.listen(3000,function(){
    console.log('Servidor rodando na porta 3000')
})
```

O que faz:

Inicializa o servidor que fica escutando as conexoes na porta definida

O metodo `listen()` recebe dois parametros: a porta que ficara sendo ouvida e uma função que imprime uma mensagem no terminal quando o servidor é inicializado.

\# A porta escolhida foi a 3000, mas é possivel colocar outras portas também

\# Para verificar o servidor criado, no navegador, coloque a URL http://localhost:3000

__dirname => representa o diretorio atual
__filename => representa o arquivo atual
