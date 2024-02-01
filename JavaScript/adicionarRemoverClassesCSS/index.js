/* Classes CSS e JS */
let div = document.querySelector("#div1")
let sec  = document.querySelector(`.sec`)
let p = document.querySelector('p')

// Forma trabalhosa
console.log(sec.className) 
console.log(div.className)
/* Adicionar classe */        
div.className = 'div'
console.log(div.className)
div.className += ' dir'
console.log(div.className)

// Forma prática
/* Imprimir */
console.log(div.classList)

/* Adicionar classe */        
p.classList.add('texto')
console.log(p.classList)

/* Adicionar multíplas classes */        

p.classList.add('outra-classe1',"outraclasse")
console.log(p.classList)

/* Remover classes */        
p.classList.remove('outra-classe1',"outraclasse")
console.log(p.classList)

/* Alternar  classe */        
//Se já tem a classe remove, se não tem adiciona

div.classList.toggle('dir')
div.classList.toggle('texto')
p.classList.toggle('texto')
p.classList.toggle('dir')

/* Verificar se um elemento possui uma classe */ 

if(sec.classList.contains('sec')){
    console.log('A classe sec está presente')
}
else{
    console.log('A classe sec não está presente')
}