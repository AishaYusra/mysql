import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user="root",
    password="yusramysql21@",
    database = "employees"
)
cursor = mydb.cursor()
# cursor.execute(
#     "CREATE DATABASE employees"
#     "CREATE TABLE information (id INT PRIMARY KEY AUTO_INCREMENT, dept_name VARCHAR(50) NOT NULL, faculty varchar(50) NOT NULL)"
# )
cursor.execute(
    "INSERT INTO information (dept_name, faculty) VALUES ('Computer Science', 'Faculty of Computing'), ('Interior Design', 'Faculty of Arts')"
)
mydb.commit()

cursor.execute(
    "SELECT * FROM information"
)
value = cursor.fetchall()
print(value)

#when using SELECT, after doing its cursor.execute(), you have to do cursor.fetchAll. you can put  it in a variable.
# print(mydb)