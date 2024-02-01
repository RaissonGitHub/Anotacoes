/* Validacao de formularios no front-end melhorado*/
// Formulario_login é o nome do formulario definido no HTML
document.formulario_login.addEventListener("submit",(e)=>{
    
    //buscar os valores
    let  user = e.target.user.value
    console.log(user)
    let  passwd = e.target.passwd.value
    let submit = true

    //remover erros anteriores
    document.querySelectorAll('.erro').forEach(e => e.remove())

    //validar user
    if(user === ""){
        submit = false

        //erro
        let tmp = document.querySelector('input[name="user"]')
        tmp.insertAdjacentHTML('afterend', '<span class="erro">Usuário é obrigatório</span>')
    }

    //validar passwd
    if(passwd === ''){
        submit = false
        //erro
        let tmp = document.querySelector('input[name="passwd"]')
        tmp.insertAdjacentHTML('afterend', '<span class="erro">Senha é obrigatória</span>')
    }

    //se pode ser enviado
    if(!submit){
        e.preventDefault()
    }
})

document.querySelector('input[name="user"]').addEventListener('keyup',()=>{ 
    //procurando um span
    console.log(document.querySelectorAll('input[name="user"] + span'))
    if(document.querySelector('input[name="user"] + span') !== null){
        document.querySelector('input[name="user"] + span').remove()
    }
})
document.querySelector('input[name="passwd"]').addEventListener('keyup',()=>{ 
    //procurando um span
    console.log(document.querySelector('input[name="passwd"] + span'))
    if(document.querySelector('input[name="passwd"] + span') !== null){
        document.querySelector('input[name="passwd"] + span').remove()
    }
})

