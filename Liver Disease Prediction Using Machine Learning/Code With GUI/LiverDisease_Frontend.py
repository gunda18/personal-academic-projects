from tkinter import *
import tkinter.messagebox
import tkinter.font
import LiverDisease_Backend1
import LiverDisease_Backend2



class Liver:
    def __init__(self, root):
        self.root = root
        self.root.title("Liver Disease Predictor")
        self.root.geometry("1490x790+0+0")
        self.root.config(bg="white")
        
        # Variables
        Age = StringVar()
        Gender = StringVar()
        TB = StringVar()
        DB = StringVar()
        AP = StringVar()
        ALA = StringVar()
        ASA = StringVar()
        TP = StringVar()
        A = StringVar()
        AGR = StringVar()
        lst = []
        
            
        # Graph Buttons   
        def Distribution():
            LiverDisease_Backend2.show_Distribution()
            
        def Scatter_Plots():
            LiverDisease_Backend2.show_Scatter_Plots()
            
        def CorGraph():
            LiverDisease_Backend2.show_CorGraph()
            
        def Accuracy():
            stdDatabase_BackEnd.show_Accuracy()
            
        def remove_Outliers():
            LiverDisease_Backend2.show_Outliers()
         
            
        # Machine Learning Methods
        def LR():
            lst.append(float(Age.get()))
            lst.append(float(Gender.get()))
            lst.append(float(TB.get()))
            lst.append(float(DB.get()))
            lst.append(float(AP.get()))
            lst.append(float(ALA.get()))
            lst.append(float(ASA.get()))
            lst.append(float(TP.get()))
            lst.append(float(A.get()))
            lst.append(float(AGR.get()))
            x = LiverDisease_Backend1.show_LR(lst)
            y = LiverDisease_Backend1.acc_LR()
            y = round(y,2)
            if x[0]==1:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has liver disease")
            elif x[0]==0:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has no liver disease")
            lst.clear()
            
            
        def SVM():
            lst.append(float(Age.get()))
            lst.append(float(Gender.get()))
            lst.append(float(TB.get()))
            lst.append(float(DB.get()))
            lst.append(float(AP.get()))
            lst.append(float(ALA.get()))
            lst.append(float(ASA.get()))
            lst.append(float(TP.get()))
            lst.append(float(A.get()))
            lst.append(float(AGR.get()))
            x = LiverDisease_Backend1.show_SVM(lst)
            y = LiverDisease_Backend1.acc_SVM()
            y = round(y,2)
            if x[0]==1:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has liver disease")
            elif x[0]==0:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has no liver disease")
            lst.clear()
            
        
        def NN():
            lst.append(float(Age.get()))
            lst.append(float(Gender.get()))
            lst.append(float(TB.get()))
            lst.append(float(DB.get()))
            lst.append(float(AP.get()))
            lst.append(float(ALA.get()))
            lst.append(float(ASA.get()))
            lst.append(float(TP.get()))
            lst.append(float(A.get()))
            lst.append(float(AGR.get()))
            x = LiverDisease_Backend1.show_NN(lst)
            y = LiverDisease_Backend1.acc_NN()
            y = round(y,2)
            if x[0]==1:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has liver disease")
            elif x[0]==0:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has no liver disease")
            lst.clear()
                
                
        def RF():
            lst.append(float(Age.get()))
            lst.append(float(Gender.get()))
            lst.append(float(TB.get()))
            lst.append(float(DB.get()))
            lst.append(float(AP.get()))
            lst.append(float(ALA.get()))
            lst.append(float(ASA.get()))
            lst.append(float(TP.get()))
            lst.append(float(A.get()))
            lst.append(float(AGR.get()))
            x = LiverDisease_Backend1.show_RF(lst)
            y = LiverDisease_Backend1.acc_RF()
            y = round(y,2)
            if x[0]==1:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has liver disease")
            elif x[0]==0:
                tkinter.messagebox.showinfo("Output", "The Algorithm is "+ str(y) +"% sure that the patient has no liver disease")
            lst.clear()
            
            
         # Clear Method
        def clearData():
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtTB.delete(0,END)
            self.txtDB.delete(0,END)
            self.txtAP.delete(0,END)
            self.txtALA.delete(0,END)
            self.txtASA.delete(0,END)
            self.txtTP.delete(0,END)
            self.txtA.delete(0,END)
            self.txtAGR.delete(0,END)    
            
            
        # Exit Method   
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit","Are you sure?")
            if iExit > 0:
                root.destroy()
                return
            
        
       
        
        MainFrame = Frame(self.root, bg="red")
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="tomato", relief = RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame, font=('arial', 47,'bold'), text="Liver Disease Predictor", bg="coral")
        self.lblTit.grid()
        
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=10, pady=10, bg="orange red", relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="orange red", relief = RIDGE)
        DataFrame.pack(side=LEFT)
        
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief = RIDGE, font=('arial', 20, 'bold'), text="Details:\n")
        DataFrameLEFT.pack(side=LEFT)
        
        ButtonFrame2 = Frame(DataFrame, bd=2, width=135, height=600, padx=180, pady=10, bg="orange red", relief = RIDGE)
        ButtonFrame2.pack(side=RIGHT)
        
        
        
        
        
        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=0, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=9)
        self.txtAge.grid(row=0, column=1)
        
        
        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=1, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=9)
        self.txtGender.grid(row=1, column=1)
        
        self.lblTB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Total Bilirubin", padx=2, pady=2, bg="Ghost White")
        self.lblTB.grid(row=2, column=0, sticky=W)
        self.txtTB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=TB, width=9)
        self.txtTB.grid(row=2, column=1)
        
        self.lblDB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Direct Bilirubin", padx=2, pady=2, bg="Ghost White")
        self.lblDB.grid(row=3, column=0, sticky=W)
        self.txtDB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DB, width=9)
        self.txtDB.grid(row=3, column=1)
        
        self.lblAP = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Alkaline Phosphotase", padx=2, pady=2, bg="Ghost White")
        self.lblAP.grid(row=4, column=0, sticky=W)
        self.txtAP = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=AP, width=9)
        self.txtAP.grid(row=4, column=1)
        
        self.lblALA = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Alamine Aminotransferase", padx=2, pady=2, bg="Ghost White")
        self.lblALA.grid(row=5, column=0, sticky=W)
        self.txtALA = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ALA, width=9)
        self.txtALA.grid(row=5, column=1)
        
        self.lblASA = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Aspartate Aminotransferase", padx=2, pady=2, bg="Ghost White")
        self.lblASA.grid(row=6, column=0, sticky=W)
        self.txtASA = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ASA, width=9)
        self.txtASA.grid(row=6, column=1)
        
        self.lblTP = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Total Proteins", padx=2, pady=2, bg="Ghost White")
        self.lblTP.grid(row=7, column=0, sticky=W)
        self.txtTP = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=TP, width=9)
        self.txtTP.grid(row=7, column=1)
        
        self.lblA = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Albumin", padx=2, pady=2, bg="Ghost White")
        self.lblA.grid(row=8, column=0, sticky=W)
        self.txtA = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=A, width=9)
        self.txtA.grid(row=8, column=1)
        
        self.lblAGR = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Albumin and Globulin Ratio", padx=2, pady=2, bg="Ghost White")
        self.lblAGR.grid(row=9, column=0, sticky=W)
        self.txtAGR = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=AGR, width=9)
        self.txtAGR.grid(row=9, column=1)
        

        
        
        self.btnAddData = Button(ButtonFrame, text="Logistic Regression", font=('arial', 20, 'bold'), height=1, width=15, bd=4, command=LR)
        self.btnAddData.grid(row=0, column=0)
        
        self.btnAddData = Button(ButtonFrame, text="SVM", font=('arial', 20, 'bold'), height=1, width=8, bd=4, command=SVM)
        self.btnAddData.grid(row=0, column=1)
        
        self.btnAddData = Button(ButtonFrame, text="Neural Network", font=('arial', 20, 'bold'), height=1, width=15, bd=4, command=NN)
        self.btnAddData.grid(row=0, column=2)
        
        self.btnAddData = Button(ButtonFrame, text="Random Forest", font=('arial', 20, 'bold'), height=1, width=15, bd=4, command=RF)
        self.btnAddData.grid(row=0, column=3)
        
        self.btnAddData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=8, bd=4, command=clearData)
        self.btnAddData.grid(row=0, column=4)
        
        self.btnAddData = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=8, bd=4, command=iExit)
        self.btnAddData.grid(row=0, column=5)
        
        self.btnAddData = Button(ButtonFrame2, text="Distribution Graphs", font=('arial', 20, 'bold'), height=1, width=17, bd=4, command=Distribution)
        self.btnAddData.grid(row=0, column=0)
        
        self.btnAddData = Button(ButtonFrame2, text="2D Scatter Plots", font=('arial', 20, 'bold'), height=1, width=17, bd=4, command=Scatter_Plots)
        self.btnAddData.grid(row=1, column=0)
        
        self.btnAddData = Button(ButtonFrame2, text="Correlation Graph", font=('arial', 20, 'bold'), height=1, width=17, bd=4, command=CorGraph)
        self.btnAddData.grid(row=2, column=0)
        
        self.btnAddData = Button(ButtonFrame2, text="Accuracy Comparison", font=('arial', 20, 'bold'), height=1, width=17, bd=4, command=Accuracy)
        self.btnAddData.grid(row=3, column=0)
        
        self.btnAddData = Button(ButtonFrame2, text="Outliers", font=('arial', 20, 'bold'), height=1, width=17, bd=4, command=remove_Outliers)
        self.btnAddData.grid(row=4, column=0)
        
        
        
        
if __name__=='__main__':
    root = Tk()
    application = Liver(root)
    root.mainloop()

