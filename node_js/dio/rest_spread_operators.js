//rest operator ...

function sum(...args) {
    return args.reduce((acc, value) => acc + value, 0);
}

console.log(sum(5, 6, 7, 8, 9))

//arrow functions não possuem a palavra reservada arguments, necessário usar o rest operatot
// const sumi = () => {
//     console.log(arguments)
// }

//o rest pega os valores que sobram e os colocam dentro de um array
const sumii = (a, b, ...args) => {
    console.log(a, b, args)
}

sumii(1, 2, 3, 4, 5)


//spread operator ...
const multiply = (...args) => args.reduce((acc, value) => acc * value, 1);

//o spread funciona como o oposto do rest, pegando os valores de um array e os transformando em parametros
const sumiii = (...rest) => {
    return multiply(...rest)
}

console.log(sumiii(1, 2, 3, 4, 5))

//mas o spread também funciona em strings, objetos e objetos iteráveis

//com strings
const str = "Digital Innovation One"

function logArgs (...args) {
    console.log(args)
}

logArgs(...str)

//com objetos literais

const obj = {
    test: 123
}

// importante destacar que o spread só funciona com objetos literais quando criando outros objetos literais
const obj2 = {
    ...obj,
    test2: "hello"
}

console.log(obj2)

//note que ele só passa os valores que a função espera, não passa os valores que sobraram

const arr = [1, 2, 3, 4, 5]

function logArgs2 (a, b, c) {
    console.log(a, b, c)
}

logArgs2(...arr)

//o spread também pode ser usado para criar arrays
const arr2 = [1, 2, 3, 4, 5]

const arr3 = [...arr2, 6, 7, 8, 9]

console.log(arr3)