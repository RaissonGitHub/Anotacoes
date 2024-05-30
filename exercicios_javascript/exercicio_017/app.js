/* ----------------------------------------------------------------------------

Exercício: 017
Enunciado:
    Ao clicar em "Adicionar", se o input tiver texto, adicionar o mesmo num
    parágrafo por baixo do botão. 
   
    Não pode ser adicionada uma palavra ou frase repetida.
---------------------------------------------------------------------------- */


let inputs = []

document.querySelector('.btn').addEventListener('click',()=>{
    let texto = document.querySelector('#text_post')
    if(texto.value && inputs.includes(texto.value)==false){
        let p = document.createElement('p')
        p.textContent = texto.value
        inputs.push(texto.value)
        document.querySelector('#posts').prepend(p)
        texto.value = ''
        texto.focus()
    }
})