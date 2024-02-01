/* ----------------------------------------------------------------------------

Exercício: 003
Enunciado: CONTADOR COM CORES PARA NEGATIVOS, ZERO E POSITIVOS
    
    A partir do HTML existente, apresentar um valor inicial igual a 0 e definir
    funcionalidades nos botões de decremento e incremento.
    No caso do valor ser zero o texto deve ser branco.
    No caso do valor ser negativo o texto deve ser vermelho puro.
    No caso do valor ser positivo o texto deve ser verde puro.

---------------------------------------------------------------------------- */


function mudarCor(e,v){
    v.textContent = e
    if(e ==0){
        v.style.color = 'white'
    } else if(e>0){
        v.style.color = 'green'
    }else{
        v.style.color = 'red'
    }

}
let contador = 0
let valor = document.querySelector('#valor') 

let mais = document.querySelector('#btn_incremento').addEventListener('click',()=>{
     contador++
     mudarCor(contador,valor)
})
let menos = document.querySelector('#btn_decremento').addEventListener('click',()=>{
    contador--
    mudarCor(contador,valor)

})
