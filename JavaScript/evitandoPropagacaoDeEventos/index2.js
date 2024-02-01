let elements = document.querySelectorAll('section,article,div')
elements.forEach((event)=>{
    event.addEventListener('click',(e)=>{
        e.stopPropagation()
        console.log(e.target.tagName)
    })
})