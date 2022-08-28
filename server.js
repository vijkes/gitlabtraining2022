const express = require("express")

const app = express()

function db(req, res){
        res.send("Welcome to dbots")
        console.log("client connected on page...")
}

app.get("/data", db )
app.listen(3000)
