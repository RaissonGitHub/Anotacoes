/* Criar elementos no DOM */

// Nota: este elemento nao é adicionado automaticamente na página
let novoElemento = document.createElement('p')
novoElemento.innerText = "Este elemento foi adicionado pelo Js"

//Adicionando no documento
document.body.appendChild(novoElemento)
//Adicionado ao final do documento

/*Adicionando texto sem tag atribuida*/

let texto = document.createTextNode('Este texto foi inserido na página e não está em nenhuma tag')
document.body.appendChild(texto)

//Adicionando um div no section

let sec = document.querySelector('section')
let novoDiv = document.createElement('div')
novoDiv.classList.add('quadro')
let divTexto = document.createElement('p')
divTexto.textContent = 'Texto colocado no div pelo Js'
sec.appendChild(novoDiv)
novoDiv.appendChild(divTexto)

/* Adicionando elementos antes */

let div2 = document.querySelector('#div2')
let novoParagrafro = document.createElement('p').textContent = 'Elemento adicionado'
div2.before(novoParagrafro)

/* Adicionando no inicio de um elemento  */

div2.prepend(novoParagrafro)

/* Adicionando no fim de um elemento  */

div2.append(novoParagrafro)

/* Outras formas de adicionar */

let div3 = document.querySelector('#div3')
let maisTexto = document.createElement('p').textContent = 'Mais texto adicionado'

/* Antes do elemento*/
div3.insertAdjacentHTML('beforebegin',maisTexto)

/* No começo do elemento*/
div3.insertAdjacentHTML('afterbegin',maisTexto)

/* Antesdo fim do elemento*/
div3.insertAdjacentHTML('beforeend',maisTexto)

/* Depois do fim do elemento*/
div3.insertAdjacentHTML('afterend',maisTexto)

/* Remover elementos do HTML*/

let div1 = document.querySelector('#div1')
div1.remove()