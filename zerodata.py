import mysql.connector

cekdb = mysql.connector.connect(
    host = "localhost",
    user = "zeromind",
    passwd = "1",
    database = "testdb"
)

hayuk = cekdb.cursor()