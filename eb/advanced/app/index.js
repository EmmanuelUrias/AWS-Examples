const express = require('express')
const app = express()
//const cors = require('cors')
//const bodyParser = require('body-parser')
const path = require('path')
const port = process.env.PORT || 3000

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'))
})

app.get('/style.css', (req, res) => {
    res.sendFile(path.join(__dirname, '/style.css'))
})

app.get('app.js', (req, res) => {
    res.sendFile(path.join(__dirname, '/app.js'))
})

app.listen(port, '0.0.0.0', () => {
    console.log(`Example app listening on port ${port}`)
})