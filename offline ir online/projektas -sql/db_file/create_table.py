import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sudoku_db"
    )


mycursor = db.cursor()
mycursor.execute("""
CREATE TABLE Sudoku (
    level1 INT,
    level2 INT,
    level3 INT,
    level4 INT,
    level5 INT,
    all_levels INT
);
""")
#mycursor.execute("INSERT INTO Sudoku (level1, level2, level3, level4, level5, all_levels) VALUES (%s,%s,%s,%s,%s,%s)", (45,45,46,45,45,224))
#db.commit()