/* ----------------------------------------------------------------------------

Exercício: 002
Enunciado: CONTADOR COM INTERVALO DE VALORES
    
    A partir do HTML existente, apresentar um valor inicial igual a 0 e definir
    funcionalidades nos botões de decremento e incremento.
    O valor nunca poderá ser inferior a -10 ou superior a 10.

---------------------------------------------------------------------------- */
let contador = 0
let mais = document.querySelector('#btn_decremento').addEventListener('click',()=>{
    if(contador>-10 && contador <=10){
        contador--
        let valor = document.querySelector("#valor").textContent = contador
    }
})
let menos = document.querySelector('#btn_incremento').addEventListener('click',()=>{
    if(contador>=-10 && contador <10){
        contador++
        let valor = document.querySelector("#valor").textContent = contador
    }
})
