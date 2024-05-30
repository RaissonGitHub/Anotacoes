/* ----------------------------------------------------------------------------

Exercício: 029
Enunciado:
    Começando pelo exercício 28, mas agora queremos apresentar os números numa
    sequência de quatro por cada linha. Deve aparecer com fundo branco e texto 
    de cor verde. Deve ter uma distribuição consistente da informação. 
---------------------------------------------------------------------------- */

let div_row = document.createElement('div')
div_row.classList.add('row')
document.querySelector('.btn').addEventListener('click',()=>{
    div_row.innerHTML = null
    for(let i = 0; i<20;i++){
        let r = Math.floor(Math.random()* 1000) +1
        let div_col = document.createElement('div')
        div_col.classList.add('col-3','text-center')
        div_col.style.background = 'white'
        div_col.style.color = 'green'
        div_col.style.padding = '10px'
        div_col.textContent = r
        div_row.appendChild(div_col)

    }
    document.querySelector('#numeros').appendChild(div_row)
})