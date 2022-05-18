const EventEmitter = require('events')

class Users extends EventEmitter {
    userLogged(data) {
        this.emit('user logged', data)
    }
}

const users = new Users()

//tem o once que é um evento que só é executado uma vez
users.on('user logged', (data) => {
    console.log(data)
})

users.userLogged({ user: 'Rodrigues Alves', cidade: 'Rio de Janeiro' })