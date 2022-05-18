//Symbols

const uniqueId = Symbol("Hello")

//Well known symbols
Symbol.iterator //<- isso que da a possibilidade de iterar sobre um objeto, como um array

//adicionando iteração a um objeto

const obj = {
    values: [1, 2, 3, 4],
    [Symbol.iterator]() {
        let i = 0

        return {
            next: () => {
                i++

                return {
                    value: this.values[i - 1],
                    done: i > this.values.length
                }
            }
        }
    }
}

//agora podemos fazer coisas que previamente não poderiamos

const it = obj[Symbol.iterator]()

console.log(it.next())
console.log(it.next())
console.log(it.next())
console.log(it.next())
console.log(it.next())

for (let value of obj) {
    console.log(value)
}

const arr = [...obj] 

console.log(arr)

//generators
function* hello() {
    console.log("Hello")
    yield 1

    console.log("From")
    const value = yield 2

    console.log(value)
}

const it2 = hello()

console.log(it2.next())
console.log(it2.next())
console.log(it2.next("Outside!"))

function* naturalNumbers() {
    let number = 0
    while (true) {
        yield number
        number++
    }
}

const it3 = naturalNumbers()

console.log(it3.next())
console.log(it3.next())
console.log(it3.next())
console.log(it3.next())

//mesclando symbols e generators
const obj2 = {
    values: [1, 2, 3, 4],
    *[Symbol.iterator]() {
        for (var i = 0; i < this.values.length; i++) {
            yield this.values[i]
        }
    }
}

for (var value of obj2) {
    console.log(value)
}