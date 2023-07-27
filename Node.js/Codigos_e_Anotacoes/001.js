const http = require('http')

const server = http.createServer((req,res) =>{
// req.url indica qual a url foi utilizada, por padrao é a "/"
    res.setHeader('Content-Type','text/plain;charset=utf-8') //Especifica o tipo do conteudo e permite caracteres especiais atraves do charset= utf-8
    if(req.url =="/"){
        res.end('URL padrão')
    }
    else{
        res.end('Outro')
    }
}).listen(3000, function(){
    console.log('Servidor rodando na porta 3000')
})

//Headers são metadados transmitidos em requisições e respostas HTTP contendo informações cruciais, como o tipo de conteúdo, autenticação, cache e muito mais, permitindo a comunicação eficiente entre clientes e servidores na web.

/*
Alguns exemplos de cabeçalhos comuns são:

    User-Agent: Identifica o tipo e a versão do navegador ou cliente que está fazendo a requisição.

    Content-Type: Especifica o tipo de conteúdo que está sendo enviado no corpo da requisição ou resposta, por exemplo, "application/json", "text/html", "image/jpeg", etc.

    Content-Length: Indica o tamanho do corpo da mensagem em bytes.

    Authorization: Utilizado para enviar credenciais de autenticação ao servidor.

    Accept: Indica os tipos de mídia que o cliente aceita na resposta, para que o servidor possa responder adequadamente.

    Cache-Control: Define as diretrizes de armazenamento em cache para o cliente ou servidor.

    Location: Usado nas respostas para indicar a localização de um recurso após uma operação de redirecionamento.

    Set-Cookie: Utilizado nas respostas para enviar cookies ao cliente.

    Origin: Enviado nas requisições por navegadores para indicar a origem da solicitação em solicitações Cross-Origin (CORS).

    Host: Especifica o nome do host do servidor para o qual a requisição está sendo feita.
*/