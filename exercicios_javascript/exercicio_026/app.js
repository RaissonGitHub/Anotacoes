/* ----------------------------------------------------------------------------

Exercício: 026
Enunciado:
    Existem 4 inputs de texto, cada um com um id diferente.
    Cada input só pode receber um caracter.
    O focus deve iniciar no primeiro input.
    Ao digitar um algarismo, o focus deve ir para o próximo input.
    Ao digitar o último algarismo, o focus deve ir para o primeiro input.
    Se todos os inputs estiverem preenchidos, o sistema deve verificar se o
    número constituído pela concatenacao dos 4 algarismos é igual a 1234.
    Se for igual, deve aparecer uma mensagem de sucesso, caso contrário,
    a mensagem de sucesso deve estar escondida.
---------------------------------------------------------------------------- */

let index = 0
document.querySelectorAll('input[type="text"]')[0].focus()
let h1 = document.querySelector('.text-success')


document.querySelectorAll('input[type="text"]').forEach((e)=>{
    e.setAttribute('maxlength',1)
    e.addEventListener('input',(s)=>{
        if(e.value !== ''){
            index++
            if(index>=4){ index=0}
            document.querySelectorAll('input[type="text"]')[index].focus()
            verificar()
        }
        
    })
}
)
function verificar(){
    let combinacao = ''
    document.querySelectorAll('input[type="text"]').forEach((e)=>{
        combinacao += e.value
    })
    if(combinacao == '1234'){
        document.querySelector('.text-success').style.display = 'block'
    }
    else{
        document.querySelector('.text-success').style.display = 'none'
    }
}