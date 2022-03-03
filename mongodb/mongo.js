const mongoose = require('mongoose');

mongodbUri = ''

module.exports = async () => {
    await mongoose.connect(mongodbUri, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    })

    return mongoose
}
