const mongo = require('./mongo')
const userSchema = require('./schemas/user-schema')

const connectToMongoDb = async () => {
    await mongo().then(async (mongoose) => {
        try{
            console.log('Conectado ao MongoDB')

            //adicionando data
            // const user = {
            //     email: 'sas@gmail.com',
            //     username: 'Sapo2',
            //     password: '1234567',
            // }

            // await new userSchema(user).save()

            //encontrando data
            // const result = await userSchema.find({
            //     password: 'test123'
            // })
            // console.log(result)

            // const result1 = await userSchema.findOne({
            //     password: 'test123'
            // })
            // console.log(result1)

            //uptading data
            // await userSchema.updateOne({
            //     username: 'Sapo'
            // }, {
            //     messages: 1
            // })

            // await userSchema.updateMany({
            //     password: 'test123'
            // }, {
            //     password: 'testabc'
            // })

            //delete data
            // await userSchema.deleteOne({
            //     username: 'Bob'
            // })

            // await userSchema.deleteMany({
            //     username: 'Frank'
            // })

            // //find and update data
            // const result = await userSchema.findOneAndUpdate(
            // //procura por um registro que corresponda com isso
            // {
            //     username: "Bob" 
            // },
            // //se achar o registro, ele atualiza por isso 
            // {
            //     email: "test@email.com",
            //     username: "Frank",
            //     password: "testabc",
            //     //increase a number
            //     $inc: {
            //         messages: -2
            //     }
            // },
            // {   
            //     //diz que caso não ache um que corresponda, ele cria um com as informações passadas
            //     upsert: true,
            //     //retorna os valores atualizados
            //     new: true
            // })

            // console.log(result)

            // //adicionando e removendo valores de um array
            // const newName = "Joe"

            // await userSchema.findOneAndUpdate({
            //     username: "Frank"
            // },{
            //     //colocando um valor dentro do array, use $addToSet
            //     //caso só queira que o valor seja adicionado se ele não estiver no array
            //     $push: {
            //         nameHistory: newName
            //     },
            //     //caso queira remover um valor do array, use $pull
            //     //$pull: {
            //     //     nameHistory: newName
            //     //}
            // })

            // //sorting and limiting data
            // const results = await userSchema.find({}).sort({
            //     messages: -1
            // }).limit(3)

            // console.log(results)

            //validando data
            // const newUser = await new userSchema({
            //     email: "test@testing.com.br",
            //     username: "test",
            //     password: "test123",
            //     messages: 10
            // })

            // const valid = await new Promise((resolve) => {
            //     newUser.validate((err) => {
            //         if (err) {
            //             console.log(err)
            //             resolve(false)
            //         } else {
            //             resolve(true)
            //         }
            //     })
            // })

            // if (valid) {
            //     await newUser.save()
            //     console.log('Salvo com sucesso')
            // }

            // await userSchema.insertMany([
            //     {
            //         email: "test1@email.com",
            //         username: "test1",
            //         password: "test123",
            //     },
            //     {
            //         email: "test2@email.com",
            //         username: "test2",
            //         password: "test123",
            //     },
            //     {
            //         email: "test3@email.com",
            //         username: "test3",
            //         password: "test123",
            //     },
            // ])

            // await userSchema.deleteMany({
            //     username: [
            //         "test1",
            //         "test2",
            //     ]
            // })

            // //operações condicionais
            // const results = await userSchema.find({
            //     level: {
            //         //lt, lte, gt, gte
            //         $exists: true
            //     }
            // })
            // console.log(results)

            //renaming and removing fields
            // await userSchema.updateMany({}, {
            //     $rename: {
            //         password: "pass"
            //     }
            // })

            // await userSchema.updateMany({}, {
            //     $unset: {
            //         nameHistory: ""
            //     }
            // })

            //array queries
            // result = await userSchema.find({
            //     testScore: {
            //         //mostra todos os registros que tenham o valor dentro do array
            //         $all: [85, 90, 77]
            //     }
            // })

            // result = await userSchema.find({
            //     testScore: {
            //         //mostra todos os registros que tenham esse tamanho de array
            //         $size: 3
            //     }
            // })

            // result = await userSchema.find({
            //     testScore: {
            //         $elemMatch: {
            //             //mostra todos os registros que tenham valores maiores de 80 em seus testScore arrays
            //             $gt: 80
            //         }
            //     }
            // })

            // console.log(result)

            //primary key
            await new userSchema({
                _id: '8237467243',
                email: 'sexo',
                username: 'sexo',
                password: 'sexo'
            }).save()
        } finally {
            mongoose.connection.close()
        }
    })
}

connectToMongoDb()