//destructuring assignment

var array = ['Maçã', 'Banana', 'Pêra', ['Tomate']]

var [maca, banana, pera, [tomate]] = array

console.log(maca, banana, pera, tomate)

//funciona tambem com objetos

const obj = {
    name: 'Celso',
    props: {
        age: 23,
        favoriteColors: ['purple', 'more_purple']
    }
}

//caso o nome da variavel seja diferente da chave do objeto, é necessário especificar o nome da chave
//note que caso o valor da variavel seja mudado, não afetara o objeto inicial
var {name: name2} = obj
var {props: {age: age2, favoriteColors: [color1, color2]}} = obj

console.log(name2, age2, color1, color2)

//destructuring assignment com funções

function sum ([a, b] = [0, 0]) {
    return a + b
}

console.log(sum([1, 2]))

function sumi ({a, b} = {a: 0, b: 0}) {
    return a + b
}

console.log(sumi({a: 1, b: 2}))