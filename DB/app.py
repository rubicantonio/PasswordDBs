import sqlite3

def deleteTable():
    c.execute("""
        
        DROP TABLE apps;

        """)
# connecting to databas
conn = sqlite3.connect("passwords-db")
c = conn.cursor()
def CreateTable():

    c.execute("""


        CREATE TABLE apps (
           name text,
           app text,
           password text

          )
    """)
    print("table created")
    print("now use insert data function(2 to add your data")
    conn.commit()
def delTable():
    c.execute("DROP TABLE apps;")
    print("table deleted")
    conn.close()



def getData():

    c.execute("SELECT * from apps")
    for x in c.fetchall():

        return x

       

    conn.commit()



    

def insertUser():

    app = str(input("Name of your app: "))
    name = str(input("username:"))
    password = input("password: ")

    c.execute("INSERT INTO apps (name, password, app) values (?, ?, ?)",
    (name, password, app))
    print(getData())
    conn.commit()




choice = input("do you want to to see your passwords(1), add new data(2), create table(3), deleteTable(4)?:  ")
if choice == "1":
    try:
     getData()
    except:
        print("Theres no table in database") 


    if getData() == " ":
        print("no data in database")
    else:
        print(getData())



    if choice == "2":

        try:
            insertUser()
        except:
            print("Theres no table in database") 



    if choice == "3":
        CreateTable()


    elif choice == "4":
        try:
            deleteTable()    
        except:
            print("There was no table to delete")