import mysql.connector

mydb = mysql.connector.connect(host="192.168.1.5", user="root", passwd="admin1234", database="atmsystem")
mycursor = mydb.cursor()

# mycursor.execute("insert into customer values('Romsky Jr M Bardillon', 5678, 10000)")
mycursor.execute("select * from customer")

for i in mycursor:
    print(i)
