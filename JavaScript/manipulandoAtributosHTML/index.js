let img = document.querySelector('.imagem')

/* Imprimir o valor de um atributo */
console.log(img.getAttribute('src'))

/* Definir ou alterar um atributo*/
//Coloque o nome do atributo uma virgula e o valor
img.setAttribute('src','https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_dark_1x_r5.png')
img.setAttribute('alt', 'logo do gmail')

console.log(img.getAttribute('src'))

/* Remover um atributo*/
console.log(img.getAttribute('alt'))
img.removeAttribute('alt')
console.log(img.getAttribute('alt'))
