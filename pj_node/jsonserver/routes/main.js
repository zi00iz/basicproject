const express = require('express')
const bodyParser = require('body-parser')
const XMLHttpRequest = require("xhr2");

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.get('/Hello', (req, res) => {
    res.send("Hello World")
})

module.exports = app;