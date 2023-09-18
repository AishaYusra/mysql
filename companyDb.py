import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="yusramysql21@",
    database = "company"
)


cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE company")

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS staff (id INT PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(50) NOT NULL, lastname VARCHAR(50) NOT NULL, ADDRESS TEXT, salary INT)"
#     )

# cursor.execute(
#     'INSERT INTO staff (firstname, lastname, ADDRESS, salary) VALUES (%s, %s, %s, %s)', ("Ahmad", "Shafii", "Kaduna, Nigeria", 500000)
#     )
# mydb.commit()

cursor.execute("SELECT * FROM staff")
# cursor.execute("SELECT * FROM staff WHERE firstname LIKE %s', ('J%',)")
results = cursor.fetchall()
print(results)
