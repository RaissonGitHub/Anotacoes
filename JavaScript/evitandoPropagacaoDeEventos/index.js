alert("Clique nas camadas e olhe o console")

let sec1 = document.querySelector('section')
let art1 = document.querySelector('article')
let div1 = document.querySelector('div')

let sec2 = document.querySelector('#sec')
let art2 = document.querySelector('#art')
let div2 = document.querySelector('#div')

/*Com propagacao*/
sec1.addEventListener('click',()=>{
    console.log('section Com propagacao')
})
art1.addEventListener('click',()=>{
    console.log('article Com propagacao')
})
div1.addEventListener('click',()=>{
    console.log('div Com propagacao')
})

/*Sem propagacao*/
sec2.addEventListener('click',(event)=>{
    event.stopPropagation()
    console.log('section Sem propagacao')
})
art2.addEventListener('click',(event)=>{
    event.stopPropagation()
    console.log('article Sem propagacao')
})
div2.addEventListener('click',(event)=>{
    event.stopPropagation()
    console.log('div Sem propagacao')
})
