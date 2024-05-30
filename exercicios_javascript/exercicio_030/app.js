/* ----------------------------------------------------------------------------

Exercício: 030
Enunciado:
    No input de texto só podemos inserir números.
    Se clicarmos no botão "Calcular", devemos apresentar o resultado do valor
    inserido no input de texto a dividir por 3.
    Todos os resultados devem ser apresentados com uma casa decimal.
    Se o resultado de qualquer cálculo for incorreto, deve aparecer a mensagem
    "Valor inválido"
---------------------------------------------------------------------------- */

document.querySelector('.btn').addEventListener('click',()=>{
    let n = parseFloat(document.querySelector('#text_valor').value)
    let resultado =  n/3
    if(resultado){
        document.querySelector('#resultado').textContent =resultado.toFixed(1)
    }else{
        document.querySelector('#resultado').textContent =      ('Valor inválido')
    }
})