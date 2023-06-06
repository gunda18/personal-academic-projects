import sqlite3


def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student1 (StdID INTEGER PRIMARY KEY, Firstname text, Lastname text, DoB text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()
    
    
def addStdRec(StdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student1 VALUES (?,?,?,?,?,?,?,?)",(StdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()
    
    
def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student1")
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(ld):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student1 WHERE StdID=?",(ld,))
    con.commit()
    con.close()
    
    
def searchData(StdID="", FirstName="", Lastname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student1 WHERE StdID=? OR Lastname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",(StdID, Lastname, DoB, Age, Gender, Address, Mobile))
    row = cur.fetchall()
    con.close()
    return row


def dataUpdate(id,StdID="", FirstName="", Lastname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student1 SET Firstname=?, Lastname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE StdID=?",(Firstname, Lastname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()
