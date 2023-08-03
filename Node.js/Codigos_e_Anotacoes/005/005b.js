const fs = require('fs');

//Criar e remover diretorios/pastas de forma assincrona

//A funcao mkdir e rmdir sao funcoes assincronas
//Entao elas nao serao executadas de forma a seguir o fluxo do codigo
//Elas serao executadas no final

fs.mkdir('./pasta02',(err)=>{ //Cria um diretorio chamado pasta02
    if(err){ //Se houver erro
        console.log('err') //Diga o erro
    }
}); 

fs.rmdir('./pasta02', (err) => { //Remove um diretorio chamado pasta02
    if (err) { //Se houver erro
      console.error(err); //Diga o erro
    } else { //Se não houver erro
      console.log('Diretório removido com sucesso.');
    }
  });

