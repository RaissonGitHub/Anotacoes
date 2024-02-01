/* ----------------------------------------------------------------------------

Exercício: 014
Enunciado:
    Ao clicar no botão "Adicionar", se o input de texto não estiver vazio, adicionar
    um parágrafo com esse texto por baixo do botão. 
    Depois da inserção com sucesso, o input deve ser limpo e receber o focus para
    nova inserção.
    Não são permitidas as palavras "teste", "obrigado" e "hoje"
---------------------------------------------------------------------------- */
let lista = ['obrigado','teste','hoje']
document.querySelector('.btn').addEventListener('click',()=>{
    let texto = document.querySelector('#text_post')
        if(texto.value && lista.includes(texto.value) ==false){
            let p = document.createElement('p')
            p.textContent = texto.value
            document.querySelector('#posts').appendChild(p)
            texto.value = ''
            texto.focus()
    }
})

