const mysql = require ("mysql")
let conexion = mysql.createConnection({
    host: "localhost",
    database: "world",
    user: "root",
    password: "qwmgxpSRg7vn"
})
conexion.connect(function(err){
    if(err){
        throw err;
    }else{
        console.log("conecion lograda")

    }
});