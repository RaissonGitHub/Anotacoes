# Tags HTML

## Tipo de documento

```
<!DOCTYPE html>   
```

## Raiz do documento

```
<html lang="pt-br"> 	 
```

Atributos:

* `lang=""` => linguagem da pagina

---

## Cabecario

```
<head>  
<meta charset="UTF-8" /> 
``` 

Atributos:

* `charset="UTF-8"` => Permite caracteres especiais

---

## ICONE DE PAGINA

```
<link   rel="shortcut icon"   href=""  type="image/x-icon"/>
```

Atributos:

* `rel=""` => relacionamento do link

* `href=""` => hyperlink

* `type=""` => tipo do arquivo

---

## TITULO DA PAGINA

```
<title></title>
```

---

## Corpo do documento

`<body></body>` 

---

## Inicio do Cabeçalho

`<header></header>`  

---

## Barra de Navegação

`<nav></nav>`  

---

## Conteudo principal

`<main></main>`  

---

## Seção generica dentro de um documento

`<section></section>`  

---

## Conteudo independente e autônomo

`<article></article>`  

---

## Conteudo relacionado

`<aside></aside>`  

---

## Rodape

`<footer></footer>`

---

## COMENTARIO

```
<!-- texto --> 
```
---

## TITULOS


`<h1></h1>` => titulo principal

`<h2></h2>` => sub titulo

...

`<h6></h6>` => sub titulo

---

## PARAGRAFO

`<p></p>` => paragrafo

---

## NEGRITO

`<b></b>` => nao semantico

`<strong></strong>`  => semantico

---

## ITALICO

`<i></i>`    => nao semantico

`<em></em>`  => semantico

---

## MARCACOES efeito de marcatexto

`<mark></mark>`

---

## LETRAS MIUDAS

`<small></small>`

---

## TEXTO DELETADO

`<del></del>` 

---

## TEXTO INSERIDO

`<ins></ins>`

---

## TEXTO SOBRESCRITO

`<sup></sup>`

---

## TEXTO SUBSCRITO

`<sub></sub>`

---

## SUBLINHADO 

`<u></u>` => nao semantico

---

## CODIGO FONTE/ PRE-FORMATACAO

`<code></code>`

ex:

`<p>O comando <code>document.getElementById('teste')</code> é escrito em JavaScript.</p>`

ex:

```
<pre>
        <code>
        num => int(input('Digite um número'))
        if num % 2 ==> 0:
            print(f'o número {num} é Par)
        else:
            print(f'O número {num} é Ímpar)
        print('Fim do programa')
        </code>
</pre>
```

---

## CITACAO

`<q></q>`

---

## CITACAO COMPLETA

`<blockquote cite="https://"> citacao </blockquote>`

Atributos:

* `cite=""` => fonte da citacao

---

## ABREVIACAO

`<abbr title=" termo completo" > termo abreviado</abbr>`

Atributos: 

* `title=""` => descricao completa do termo abreviado

---

## TEXTO INVERTIDO

`<bdo dir="rtl"></bdo>`

Atributos: 

* `dir=""` => orientacao do texto

---

## ENDERECO

`<address></address>`

---

## QUEBRA DE LINHA

`<br>`

---

## ELEMENTO GENERICO DIV

```
<div class=""></div>
```

ou 

```
<div id=""></div>
```
Uso:

Elemento generico para se colocar class ou id

---

## ELEMENTO GENERICO DE TEXTO SPAN

`<span class="">texto</span>`

ou 

`<span id="">texto</span>`

Uso:

Elemento generico de texto para se colocar class ou id

---

## CARACTERES ESPECIAIS

Para por o sinal de <

`&lt;`

Para por o sinal de >

`&gt;`

Outros:

® => `&reg;`

© => `&copy;`

™ => `&trade;`

€ => `&euro;`

£ => `&pound;`

¥ => `&yen;`

¢ => `&cent;`

Δ => `&Delta;`

δ => `&delta;`

↑ => `&uarr;`

---

## EMOJIS

&#x e depois o codigo do emogi

ex:

`&#x1F60E;`

`&#x1F44D;`

---

## ELEMENTO COM MAIS DETALHES

```
<details>
	<summary>
	      Elemento
	</summary>
	Detalhes
</details>
```

---

## BARRA DE PROGRESSO

`<meter min="0" max="100" low="40" high="90" optimum="100" value="70"></meter>`

Atributos:

* `min=""` => valor minimo

* `max=""` => valor maximo

* `low=""` => cor vermelha

* `high=""` => cor verde

* `optimum=""` =>  valor ideal entre os valores

* `value=""` => valor atual

---

## BARRA DE CARREGAMENTO

`<progress></progress>`

---

## LISTA ORDENADA

```
<ol type="">
        <li>topico<li> => linha ou topico da lista
</ol>
```

Atributos:

* `type=""` => indicar a marcacao da lista, variando entre 1, A, a, I,  i

\# Existe também a possibilidade de começar por outros números como 3 ao invés de 1 com o atributo start

---

## LISTA NAO ORDENADA

```
<ul type="">
      <li>topico<li> 
</ul>
```

Atributos:

* `type=""` => indicar a marcacao da lista, variando entre disc, circle, square

---

## MISTURA DE LISTAS

ex:

```
<ol>
	<li>SNES</li>
	<ul type="disc">
		<li>Donkey Kong Country</li>
		<li>TMNT</li>
	</ul>
	<li>Playstation 2</li>
	<ul type="disc">
		<li>God of war 2</li>
		<li>Gta San Andreas</li>
	</ul>
</ol>
```

---

## LISTA DE DEFINICOES

```
<dl>
	<dt>Termo</dt>
	<dd>Descricao</dd>
</dl>
```

---

## LINKS E ANCORAS


`<a href="" target=""  rel="">Texto do link</a>`

Atributos:

* `href=""` => hyperlink do arquivo

	* `href=""` Pode ser tanto externo quanto interno, ou até dentro da pagina

* `target=""` => destino do link

	* `target="_blank"` => para uma nova página em branco

	* `target="_self"` => (padrão) para abrir na página atual

* `rel=""` => natureza do destino

	* `rel="next"`  => indica uma proxima parte

	* `rel-"prev"`  => indica parte anterior

	* `rel="external"`  => indica um link para fora do seu site

	* `rel="nofollow"`  => indica que é um link não endossado, como um link pago

O rel ajuda o mecanismo de busca encontrar qual o mecanismo de navegação que você está criando;

Quando utilizar links externos, ou seja, links que te levam para fora do seu site, é recomendado utilzar parametros para que seu site não seja fechado;

---

## LINK DE DOWNLOAD

`<a href="" download="" type="" target="_blanck" rel="external">texto do link</a>`

Atributos:

* `href=""` => hyperlink do arquivo

* `download=""` => nome que o arquivo tera ao ser baixado

* `type=""` => tipo do arquivo

Para arquivos PDF: `type="application/pdf"`

Para arquivos de imagem JPEG: `type="image/jpeg"`

Para arquivos de imagem PNG: `type="image/png"`

Para arquivos de planilha Excel: `type="application/vnd.ms-excel"`

Para arquivos de documento Word: `type="application/msword"`

Para arquivos de apresentação PowerPoint: `type="application/vnd.ms-powerpoint"`

Para arquivos de áudio MP3: `type="audio/mpeg"`

Para arquivos de vídeo MP4: `type="video/mp4"`

* `target=""` => destino do link

	* `target="_blank"` => para uma nova página em branco

	* `target="_self"` => (padrão) para abrir na página atual

* `rel=""` => natureza do destino

	* `rel="next"`  => indica uma proxima parte

	* `rel-"prev"`  => indica parte anterior

	* `rel="external"`  => indica um link para fora do seu site

	* `rel="nofollow"`  => indica que é um link não endossado, como um link pago

O rel ajuda o mecanismo de busca encontrar qual o mecanismo de navegação que você está criando;

Quando utilizar links externos, ou seja, links que te levam para fora do seu site, é recomendado utilzar parametros para que seu site não seja fechado;


---

## IMAGENS

`<img src="" alt="" />`

Atributos:

* `src=""` => fonte da imagem

	* `src=""` Pode ser interno ou externo

* `alt="" =` => descricao da imagem, ajuda na acessibilidade

---

## IMAGENS DINAMICAS

```
<picture>
	<source media="(max-width:750px)" srcset="" type="image/png" />
	<source media="(max-width: 1050px)" srcset="" type="image/png" />
	<img src="" alt="imagem flexivel" />
</picture>
```

A tag picture permite que vc crie varios sources => várias fontes para imagens

A ordem é: 1° img, 2° source media="(max-width: 1050px)", 3° source media="(max-width:750px)"

Atributos:

* `src=""` => fonte da imagem

	* `src=""` Pode ser interno ou externo

* `alt=""` => descricao da imagem, ajuda na acessibilidade

* `type=""` => indica o tipo de imagem a ser definida

* `media=""` => indica o tamanho maximo

* `srcset =""` =>  configura o link da imagem que será carregada quando o tamanho indicado for atingido

---

## AUDIO
`<audio src=" controls autoplay loop></audio>`

Atributos:

* `src=""` => fonte do audio

* `controls` => controles de audio

* `autoplay` => reprodução automatica

* `loop` => repetição do audio sem interrupções

\# Não esqueça de colocar controls para que os controles de audio apareçam na pagina

Os formatos compartiveis de áudio são MP3, WAV e OGG

\# WAV não é recomendado, já que são arquivos de grande porte


## AUDIO opcao recomendada

```
<audio preload="metadata" controls autoplay loop>
	<source src="" type="audio/mpeg" />
	<source src="" type="audio/ogg" />
	<source src="" type="audio/wav" />
	<p>Infelizmente seu navegador não consegue reproduzir audio.</p>         
</audio>
```

Ordem: 1° mpeg, 2° ogg, 3° wav, 4° `<p>`

Atributos:

* `preload=""` => o que deve ser feito com o audio

	* `preload="auto"` => a pagina só é carregado após o áudio ser carregado => PERIGOSO!!!

	* `preload="metadata"` => a pagina carrega algumas informações do áudio como data e duração antes

	* `preload="none"` => não carrega nada antes do usuario requisitar o botão nos controles


* `src=""` => fonte do audio

* `type=""` => tipo do arquivo de audio

---

## VIDEOS

internos:

```
<video poster="" width="" height="" controls autoplay loop> 
	<source src="" type="video/webm">
	<source src="" type="video/m4v">
	<source src="" type="video/mp4">
	<source src="" type="video/ogv">
	<p>Seu navegador não tem suporte a videos.</p>
</video>
```

Ordem: 1° webm, 2° m4v, 3° mp4, 4° ogv, 5° `<p>`

Atributos:

* `poster=""` => define uma capa para o video, especificar o local

* `width=""` => define a largura da tela do video

* `height=""` => define a largura da tela do video

* `controls` => controles de audio

* `autoplay` => reprodução automatica

* `loop` => repetição do video sem interrupções

* `src=""` => fonte do audio

* `type=""` => tipo do arquivo de audio

externos:

\# Para vídeos retirados do youtube

\# Clique com compartilhar, incorporar, copie e cole o link

ex:

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/j5RGWhxiI_M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
```
---

## FORMULARIO

```
<form method="" action="">
</form>
```

Atributos:

* `method=""` => especifica o metodo do formulario

	* `method="get"` => pega dados dos campos do formulario e coloca na url

	* `method="post"` => envia os dados dos campos do formulario

* `action=""` => especifica para onde enviar os dados do formulário

---

# A PARTIR DAQUI TUDO DEVE ESTAR DENTRO DA TAG `<form>`  

## FIELDSET

`<fieldset></fieldset>`


Agrupar elementos do formulario

---

## LEGEND

```
<fieldset>
	<legend>Title</legend> 
<fieldset>
```
Uso:

Titulo para o agrupamento

---

## LABEL

``<label for="">Nome</label>`` 

Uso:

Nome para o input

Atributos:

* `for=""` => especifica o input

\# Deve ser colocado ou id, class referente ao input

---

## INPUTS

`<input type="">`

---

### BUTTON

`<input type="button" value=""> `

Uso:

Botao generico

Atributos:

* `value=""` => texto dentro do botao

---

### CHECKBOX

`<input type="checkbox" name="">` 

Uso:

Caixa de multiselecao 0 ou nenhuma ocorrencia

Atributos:

* `name=""` => identificar campos de formulários

---

### COLOR

`<input type="color" value="#ff0000">` 

Uso:

Input que permite a selecao de uma cor

Atributos:

* `value=""` => texto dentro do input

\# Pode ser definido uma cor no `value`

---

### DATE

`<input type="date">` 

Uso:

Input que permite a selecao de uma data

Formato:  dd/mm/aaaa

---

### DATETIME-LOCAL

`<input type="datetime-local">` 

Uso:

Input que permite a selecao de uma data e horario

Formato:  dd/mm/aaaa h:min

---

### EMAIL

`<input type="email">` 

Uso:

Caixa de email

Por padrao pede um @ para ser verdadeiro

---

### FILE

`<input type="file">` 

Uso:

Input que permite o envio de um arquivo

---

### HIDDEN

`<input type="hidden">` 

Uso:

Campo oculto na pagina

---

### IMAGE

`<input type="image" src="" alt="" width="" height="">`

Uso:

Input que permite o uso de uma imagem como botao de envio de formulario

Atributos:

* `src=""` => fonte da imagem

* `alt=""` => descricao

* `width=""` => largura da imagem

* `heigth=""` => altura da imagem

---

### MOUTH

`<input type="month">` 

Uso:

Input que permite a selecao de um mes

Formato: m de a

---

### NUMBER

`<input type="number" min="" max="" step="">`

Uso:

Input que permite a entrada somente de numeros

Atributos:

* `min=""` => valor minimo 

* `max=""` => valor maximo

* `step=""` => multiplo ou casa decimal

ex: de casa decimal

`step=".01"` => duas casas decimais.

---

### PASSWORD

`<input type="password">` 

Uso:

Caixa de senha (com mascara)

---

### RADIO

`<input type="radio" name="">` 

Uso:

Caixa de selecao unica ocorrencia obrigatoria

Atributos:

* `name=""` identificar campos de formulários

---

### RANGE

`<input type="range" min="" max="">` 

Uso:

Input de controle para inserir um número cujo valor exato não é importante  (como um controle deslizante)

Atributos:

* `min=""` => valor minimo 

* `max=""` => valor maximo

---

### RESET

`<input type="reset">` 

Uso:

Limpa todos os campos preenchidos do formulario

---

### SEARCH

`<input type="search">` 

Uso:

Input de texto para pesquisa

---

### SUBMIT

`<input type="submit" value="">` 

Uso:

Botao de envio de informacoes do formulario

Atributos:

* `value=""` => texto dentro do botao

---

### TEL

`<input type="tel">`

Uso:

Input para telefone

---

### TEXT

`<input type="text">` 

Uso:

Input para texto

---

### TIME

`<input type="time">` 

Uso:

Input para selecionar uma hora

Formato: h:min

---

### URL

`<input type="url">` 

Uso:

Input para adicionar uma URL

---

### WEEK

`<input type="week">` 

Uso:

Permite a selecao de uma semana especifica do ano

Formato: semana n, de a

---

### Atributos para inputs 

| Atributo | Value | Uso | Descricao |
| ---     | ---  | ---| ---|
| `value=""` | text | Valor | a  |

|`readonly` |  none | Somente leitura | a | 

|`disabled` | none | Desabilitado| a |  

 |`size=""`| number | Tamanho | Para types: text, search, tel, url, email, and password.|

 |`autocomplete=""`| on,off | Autocompletar | Para types: text, search, url, tel, email, password, datepickers, range, and color. |

---
