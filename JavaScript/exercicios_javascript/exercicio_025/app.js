/* ----------------------------------------------------------------------------

Exercício: 025
Enunciado:
    O input number text_numero é o multiplicando. O seu valor só pode variar
    entre 1 e 20. Ao alterar o valor, deve ser apresentada a tabuada do número definido
    no div cujo id = resultados.
---------------------------------------------------------------------------- */

document.querySelector('#text_numero').setAttribute('max',20)
document.querySelector('#text_numero').setAttribute('min',1)
document.querySelector('#text_numero').addEventListener('change',(e)=>{
    document.querySelector('#resultados').innerHTML = null
    for(let i = 0; i<=10;i++){
        let n = document.createElement('p')
        n.textContent = `${parseInt(e.target.value)} X ${i} = ${parseInt(e.target.value) * i}`;
        document.querySelector('#resultados').append(n)

    }
})