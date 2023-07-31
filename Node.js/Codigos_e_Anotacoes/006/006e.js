const fs = require('fs');

//Remover arquivos de forma assincrona


fs.unlink('./logs.log', (err)=>{
    if(err){
        console.log(err)
    }
})
