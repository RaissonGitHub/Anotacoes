/* ----------------------------------------------------------------------------

Exercício: 028
Enunciado:
    Existe um botão o qual, ao ser clicado, cria 20 números aleatórios entre 1 e 1000.
    Esses números devem ser apresentados cada um em sua própria linha dentro do elemento
    cujo id é igual a "numeros".
---------------------------------------------------------------------------- */

document.querySelector('.btn').addEventListener('click',()=>{
    document.querySelector('#numeros').innerHTML = null
    for(let i = 0; i<=20;i++){
        let r = Math.floor(Math.random()* 1000) +1
        document.querySelector('#numeros').innerHTML += `${r}<br>`
    }
})