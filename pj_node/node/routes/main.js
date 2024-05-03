// const express = require('express');
// const bodyParser = require('body-parser');
// const axios = require('axios');
// const port = 3500;

// const app = express()
// app.use(cors({
//     origin: '*', // 모든 출처 허용 옵션
// }))

// app.use(bodyParser.urlencoded({ extended: true }));
// app.use(express.static('public')); // 'public' 폴더 안의 index.html을 호스팅합니다.
// const cors = require('cors');



// app.get('/', (req, res) => {
//     res.sendFile(__dirname + '/public/index.html');
// });

// // form에서 데이터를 받아 처리하는 라우트
// app.post('/favpath', async (req, res, next) => {
//     const { sx, sy, ex, ey } = req.body;

//     try {
//         const response = await axios.get(`http://127.0.0.1:3500/favpath?sx=${sx}&sy=${sy}&ex=${ex}&ey=${ey}`);
//         res.send(response.data);
//     } catch (error) {
//         console.error('Error calling the API:', error);
//         res.status(500).send('An error occurred');
//     }
//     });
    
// app.listen(port, () => {
//     console.log(`Example app listening at http://localhost:${port}`);
// });