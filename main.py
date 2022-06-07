import mysql.connector
from datetime import datetime
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='UCSDTheasianwowo123@',
    database='testdatabase'
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")

# mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("DESCRIBE Person")
# for x in mycursor:
#     print(x)

# How to add and commit to data base
# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)", ("Dougie", 20))
# db.commit()



# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, race varchar(50) , id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")


# mycursor.execute("INSERT INTO Test (name,created,race) VALUES (%s,%s,%s)", ("Chong", datetime.now(), "Porkbelly"))
# db.commit()
mycursor.execute("SELECT * FROM Test")
for x in mycursor:
    print(x)