/* Copiando e referenciando Objetos */
let obj ={
    nome:`Roberto`,
};

let ref_obj = obj; 
/*
Não está criando uma copia, mas sim criando uma referencia
Se mudar o nome da referencia estará mudando o nome do original também
*/
console.log(obj.nome); //Roberto
console.log(ref_obj.nome);//Roberto
ref_obj.nome = `Carlos`;
console.log(obj.nome); //Carlos
console.log(ref_obj.nome); //Carlos

/* Para criar uma cópia pode fazer dessa maneira */
let new_obj = Object.assign({},obj);
new_obj.nome = `João`
console.log(obj); //Carlos
console.log(new_obj); //João

/* Ou pode ser feito assim com o spread operator */

let final_obj = {...obj};
// Os três pontos são o spread operator que vai pegar tudo dentro do objeto obj
final_obj.nome = 'Joaquim';
console.log(obj); //Carlos
console.log(final_obj); //Joaquim