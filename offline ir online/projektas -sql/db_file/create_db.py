import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
mycursor = db.cursor()
mycursor.execute("CREATE DATABASE sudoku_db")