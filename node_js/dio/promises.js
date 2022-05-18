const doSomethingPromise = () => new Promise((resolve, reject) => { resolve('First data') })

const doOtherThing = () => new Promise((resolve, reject) => { resolve('Second data') })

Promise.all([doSomethingPromise(), doOtherThing()])
    .then(data => console.log(data))
    .catch(err => console.log(err))

Promise.race([doSomethingPromise(), doOtherThing()])
    .then(data => console.log(data))
    .catch(err => console.log(err))