/* ----------------------------------------------------------------------------

Exercício: 018
Enunciado:
    Ao clicar em "Adicionar", se o input tiver texto, adicionar o mesmo num
    parágrafo por baixo do botão. 
   
    Cada texto inserido deve ser precedido da expressão "Eliminar" com cor vermelha
    e como efeito de um mouse hover.

    Se clicar em "Eliminar" apenas poderá ser removida a palavra ou frase
    correspondente.
---------------------------------------------------------------------------- */
/* ----------------------------------------------------------------------------

Exercício: 017
Enunciado:
    Ao clicar em "Adicionar", se o input tiver texto, adicionar o mesmo num
    parágrafo por baixo do botão. 
   
    Não pode ser adicionada uma palavra ou frase repetida.
---------------------------------------------------------------------------- */
    
document.querySelector('.btn').addEventListener('click',()=>{
    let texto = document.querySelector('#text_post')
    if(texto.value){
        let s = document.createElement('span')
        s.textContent = 'Eliminar'
        s.style.color = 'red'
        s.style.cursor = 'pointer'
        s.addEventListener('click',()=>{
            s.parentNode.remove()
        })
        let p = document.createElement('p')
        p.appendChild(s)
        p.append(` | ${texto.value}`)
        document.querySelector('#posts').prepend(p)
        texto.value = ''
        texto.focus()
    }
})