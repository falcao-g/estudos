const mongoose = require('mongoose')

const reqString = {
    type: String,
    required: true
}

const userSchema = mongoose.Schema({
    _id: reqString,
    email: reqString,
    username: reqString,
    password: reqString,
    level: Number,
    messages: {
        type: Number,
        //valor default
        default: 5,
        min: 0,
        max: 10
    },
    nameHistory: [String],
    testScore: [Number]
}, {
    //automaticamente cria timestamps (createdAt, updatedAt)
    timestamps: true
})
                                                    //se você não quiser que o mongoose crie uma collection no plural, passe o nome de novo como o terceiro argumento
module.exports = mongoose.model('users', userSchema)