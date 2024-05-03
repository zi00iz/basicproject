// app.use(bodyParser.json())      //json 형태의 입력 데이터를 파싱
// app.use(bodyParser.urlencoded({ extended: false }))
// app.use(express.json())         //json 형태의 입력 데이터를 파싱
// app.use(express.urlencoded({ extended: true }))

// const secret = require('/work/basicproject/pj_py/secret.json')

// MongoDB를 사용하기 위한 mongoose
// const mongoose = require('mongoose')
// const mongoConnectionString = process.env.MONGO_CONNECTION_STRING

//Mongoose를 사용하여 MongoDB에 연결
// mongoose.connect(secret.Mongo_URI, {
//     useNewUrlParser: true,
//     useUnifiedTopology: true,
// }).then(() => console.log('MongoDB에 성공적으로 연결되었습니다.')).catch((err) => console.error('MongoDB 연결 실패:', err))
