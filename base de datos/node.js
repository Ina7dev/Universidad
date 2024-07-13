const mysql = require ("mysql")
const connection = mysql.createConnection({
    host:"127.0.0.1",
    user:"root",
    password:"root",
    database:"world"
})
connection.connect((err)=>{
    if(err) throw err
    console.log("la conexion se a establecido correctamente")
})
connection.end