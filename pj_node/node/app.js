// Step 1: 라이브러리와 모듈 불러오기
const express = require('express');
const axios = require('axios');
const morgan = require('morgan');
const path = require('path');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const app = express();
const cors = require('cors');
const router = express.Router();

app.use(cors({
    origin: '*', // 모든 출처 허용 옵션
}))

// Step 2: 애플리케이션 및 포트 설정
app.set('port', process.env.PORT || 8500);

// Step 3: 미들웨어 사용 설정
app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true })); // 합친 코드에서 폼 데이터 처리에 필요한 설정
app.use(cookieParser());

// Step 4: 정적 파일 제공 설정
app.use(express.static(path.join(__dirname, 'public'))); //'public' 폴더 안의 index.html 호스팅

// Step 5: 라우트 설정
// 메인 페이지 라우트
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// form에서 데이터를 받아 처리하는 라우트 - favpath
app.post('/favpath', async (req, res, next) => {
    const { sx, sy, ex, ey } = req.body;

    try {
        // 여기서 'http://127.0.0.1:3500/favpath'는 예시로 사용한 주소입니다.
        const response = await axios.get(`http://127.168.1.71:3500/favpath?sx=${sx}&sy=${sy}&ex=${ex}&ey=${ey}`);
        res.send(response.data);
    } catch (error) {
        console.error('Error calling the API:', error);
        res.status(500).send('An error occurred');
    }
});

// 추가 라우트 모듈 설정 (예: ./routes/main.js)
//var main = require('./routes/index.html');
//app.use('/', main);

// Step 6: 서버 리스닝 시작
app.listen(app.get('port'), () => {
    console.log(`${app.get('port')} Port: Server Started~!!`);
});

module.exports = router;