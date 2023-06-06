from tkinter import *
import tkinter.messagebox
import tkinter.font
import stdDatabase_BackEnd
import sqlite3


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database")
        self.root.geometry("1325x620+0+0")
        self.root.config(bg="white")
        
        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit","Are you sure?")
            if iExit > 0:
                root.destroy()
                return
            
        
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtlna.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAdr.delete(0,END)
            self.txtMobile.delete(0,END)
            
            
        def addData():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.studentData()
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
                    
            
        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.viewData():
                studentlist.insert(END,row,str(""))
        
        
        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection() [0]
            sd = studentlist.get(searchStd)
            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtlna.delete(0,END)
            self.txtlna.insert(END,sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[6])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[8])
            
        
        def DeleteData():
            if(len(StdID.get())!=0):
                ld = StdID.get()
                stdDatabase_BackEnd.deleteRec(ld)
                clearData()
                DisplayData()
                
                
        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.searchData(StdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END,row,str(""))
                
                
        def update():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        
        
        
        
        
        MainFrame = Frame(self.root, bg="red")
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="tomato", relief = RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame, font=('arial', 47,'bold'), text="Student Database Management", bg="coral")
        self.lblTit.grid()
        
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="orange red", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="orange red", relief = RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief = RIDGE, font=('arial', 20, 'bold'), text="Details:\n")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief = RIDGE, font=('arial', 20, 'bold'), text="DataBase:\n")
        DataFrameRIGHT.pack(side=RIGHT)
        
        
        
        
        
        
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)
        
        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="First Name", padx=2, pady=2, bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)
        
        self.lbllna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Last name", padx=2, pady=2, bg="Ghost White")
        self.lbllna.grid(row=2, column=0, sticky=W)
        self.txtlna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=39)
        self.txtlna.grid(row=2, column=1)
        
        self.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date Of Birth", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)
        
        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)
        
        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)
        
        self.lblAdr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address", padx=2, pady=2, bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAdr.grid(row=6, column=1)
        
        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile", padx=2, pady=2, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)
        
        
        
        
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.grid(row=0, column=0,padx=8)
        scrollbar.config(command = studentlist.yview)
        
        
        
        
        
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)
        
        self.btnAddData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnAddData.grid(row=0, column=1)
        
        self.btnAddData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnAddData.grid(row=0, column=2)
        
        self.btnAddData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.btnAddData.grid(row=0, column=3)
        
        self.btnAddData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=searchDatabase)
        self.btnAddData.grid(row=0, column=4)
        
        self.btnAddData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=update)
        self.btnAddData.grid(row=0, column=5)
        
        self.btnAddData = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnAddData.grid(row=0, column=6)
        
        
if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()

