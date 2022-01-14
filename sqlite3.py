import sqlite3

conn = sqlite3.connect(r'C:\repository\first-repo\ssqqll1.sqbpro')

def addNewWorker():
    input()
    Name = Input('enter a name:')
    age = Input('enter a age:')
    address = Input("enter a address: ")
    salary = int(input('enter salary:'))
    conn.execute(f'insert in company (name, age, address, salary) values (conn.execute("INSERT INTO COMPANY (name,age,address,salary) VALUES ('James', 44, 'Norway', 5000.00 );")

    for a in range(3):
    addNewWorker(name = input('Enter name:'), age=int(input('enter age:')), address= input('anter address:')

    for a in range(3):
    addNewWorker()
    cursor.fetchone()

    # conn.execute("INSERT INTO COMPANY VALUES ("(9, 'James', 44, 'Norway', 5000.00")
    conn.commit
    conn.execute("INSERT INTO COMPANY (name,age,address,salary) VALUES ('James', 44, 'Norway', 5000.00 );"cursor.fetchone)



val = input('type the worker : ')
var= val.split('')
 # def printdata(condition=''):
#     cursor = conn.execute(f"'SELECT * FROM COPMPANY' {condition}")
#     for record in cursor:

# printData()
#  input((f" ENTER"))
# conn.execute("DELETE FROM COMPANY WHERE ID>7")
# conn.commit()
#
# def addNewWorker():
#     INSERT INTO COMPANY VALUES (9, 'James', 44, 'Norway', 5000.00 )
#     INSERT INTO COMPANY VALUES (8, 'Paul', 24, 'Houston', 20000.00 );
#     INSERT INTO COMPANY VALUES (10, 'James', 45, 'Texas', 5000.00 );
#
#     input()
#
#
#
# def printData(condition=''):
#     cursor = conn.execute("SELECT * FROM COMPANY "+condition)
#     for record in cursor:
#         print(f"id={record[0]}, name={record[1]}, age={record[2]}, address={record[3]}, salary={record[4]}")
#
# printData("WHERE ADDRESS='TEXAS'")
# pribtData("order by NAME")


# cursor = conn.execute("SELECT * FROM COPMPANY")
# for record in cursor:
#     print(record)
# print(f"id={cursor[0]}, name={cursor}[1]}, age={cursor[2]}, address={cursor[3]}, salary={cursor[4]}")
# print(type(cursor))

