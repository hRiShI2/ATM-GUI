import tkinter
import os

global StartW
DB = dict()
row_num = 3
col_num = 3


class Main_Window():

    def startWindow(self):
        global StartW
        StartW = tkinter.Tk()
        StartW.geometry("300x100+400+200")
        StartW.title("Main Menu")
        StartW.resizable(width=False, height=False)
        i = 0
        while i < row_num:
            StartW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < col_num:
            StartW.grid_columnconfigure(i, minsize=50)
            i += 1
        lbl = tkinter.Label(StartW, text="Welcome")
        lbl.grid(row=1, column=2)
        btn = tkinter.Button(StartW, text="Start", width=10, command=self.mainWindowInit)
        btn.grid(row=2, column=2)

    def mainWindowInit(self):
        self.mainW = tkinter.Toplevel()
        self.mainW.geometry("300x100+400+200")
        self.mainW.title("Main Menu")
        self.mainW.resizable(width=False, height=False)
        i = 0
        while i < row_num:
            self.mainW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < col_num:
            self.mainW.grid_columnconfigure(i, minsize=20)
            i += 1
        self.var = tkinter.IntVar()
        rd1 = tkinter.Radiobutton(self.mainW, text="Admin", variable=self.var, value=0)
        rd2 = tkinter.Radiobutton(self.mainW, text="User", variable=self.var, value=1)
        rd1.grid(row=0, column=1)
        rd2.grid(row=1, column=1)

        btn = tkinter.Button(self.mainW, text="Enter", command=self.mwBtn)
        btn.grid(row=2, column=2)
        # read Database
        global DB
        try:
            r = open("Database/DB.txt", "r")
            DB = eval(r.read())
            r.close()
        except:
            os.system("mkdir Database")
            w = open("Database/DB.txt", "w")
            w.write(str(DB))
            w.close()

    def mwBtn(self):
        if self.var.get() == 0:
            obj = Admin()
            obj.adminPass()
            self.mainW.destroy()
        else:
            self.User()
            self.mainW.destroy()

    def User(self):
        self.usrW = tkinter.Toplevel()
        self.usrW.geometry("300x100+400+200")
        self.usrW.title("User Menu")
        self.usrW.resizable(width=False, height=False)
        i = 0
        while i < row_num:
            self.usrW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < col_num:
            self.usrW.grid_columnconfigure(i, minsize=20)
            i += 1
        self.varU = tkinter.IntVar()
        rd1 = tkinter.Radiobutton(self.usrW, text="Current User", variable=self.varU, value=0)
        rd2 = tkinter.Radiobutton(self.usrW, text="  New User  ", variable=self.varU, value=1)
        rd1.grid(row=0, column=1)
        rd2.grid(row=1, column=1)

        btn = tkinter.Button(self.usrW, text="Enter", command=self.usrWBtn)
        btn.grid(row=2, column=2)

    def usrWBtn(self):
        if self.varU.get() == 0:
            self.usrW.destroy()
            obj = Current_User()
            obj.curUser()
        else:
            self.usrW.destroy()
            obj = New_User()
            obj.newUser()


class Admin():

    def adminPass(self):
        self.admminPassW = tkinter.Toplevel()
        self.admminPassW.geometry("300x100+400+200")
        self.admminPassW.title("Admin Menu")
        self.admminPassW.resizable(width=False, height=False)
        i = 0
        while i < 4:
            self.admminPassW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < col_num:
            self.admminPassW.grid_columnconfigure(i, minsize=20)
            i += 1
        # Lable
        lbl = tkinter.Label(self.admminPassW, text="Password")
        lbl.grid(row=0, column=1)
        # Button
        btn = tkinter.Button(self.admminPassW, text="Enter", command=self.adminPassBtn)
        btn.grid(row=2, column=2)
        # Entry
        self.adminPass_Entry = tkinter.Entry(self.admminPassW, show="*")
        self.adminPass_Entry.grid(row=0, column=2)

    def adminPassBtn(self):
        if self.adminPass_Entry.get() == "0000":
            self.adminServ()
            self.admminPassW.destroy()
        else:
            # Lable
            lbl = tkinter.Label(self.admminPassW, text="Password incorrect")
            lbl.grid(row=1, column=2)

    # Admin Services
    def adminServ(self):
        self.adminServW = tkinter.Toplevel()
        self.adminServW.geometry("350x300+600+150")
        self.adminServW.resizable(False, False)
        self.adminServW.title("Admin Services")
        i = 0
        while i < 10:
            self.adminServW.grid_rowconfigure(i, minsize=40)
            i += 1
        i = 0
        while i < col_num:
            self.adminServW.grid_columnconfigure(i, minsize=100)
            i += 1
        BTNC = tkinter.Button(self.adminServW, text="Delete Account", width=15, command=self.deleteAccInit)
        BTNC.grid(row=1, column=1)
        BTNB = tkinter.Button(self.adminServW, text="Get User Data", width=15, command=self.getDataInit)
        BTNB.grid(row=2, column=1)
        BTNP = tkinter.Button(self.adminServW, text="Search With Name", width=15, command=self.searchNameInit)
        BTNP.grid(row=3, column=1)
        BTNL = tkinter.Button(self.adminServW, text="Logout", width=15, command=self.adminServW.destroy)
        BTNL.grid(row=5, column=1)
        BTNE = tkinter.Button(self.adminServW, text="Exit", width=15, command=exitBtn)
        BTNE.grid(row=6, column=1)

    # Delete Account
    def deleteAccInit(self):
        self.deleteAccW = tkinter.Toplevel()
        self.deleteAccW.geometry("250x150+670+200")
        self.deleteAccW.resizable(False, False)
        self.deleteAccW.title("Delete Account")
        i = 0
        while i < 6:
            self.deleteAccW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.deleteAccW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        Lbl = tkinter.Label(self.deleteAccW, text="ID ")
        Lbl.grid(row=1, column=1)
        # Button
        BTN = tkinter.Button(self.deleteAccW, text="Enter", width=10, command=self.deleteAccBtn)
        BTN.grid(row=5, column=2)
        # Entry
        self.deleteAcc_Entry = tkinter.Entry(self.deleteAccW)
        self.deleteAcc_Entry.grid(row=1, column=2)

    def deleteAccBtn(self):
        val = self.deleteAcc_Entry.get()
        if val in DB:
            os.system("rm -r " + str(val))
            DB.pop(val)
            w = open("Database/DB.txt", "w")
            w.write(str(DB))
            w.close()
            self.deleteAccW.destroy()
            ShowMSG("Account Deleted")

        else:
            # label
            LblCash = tkinter.Label(self.deleteAccW, text="ID doesnt exist")
            LblCash.grid(row=3, column=2)

    # Get Account Data
    def getDataInit(self):
        self.getDataW = tkinter.Toplevel()
        self.getDataW.geometry("250x150+670+200")
        self.getDataW.resizable(False, False)
        self.getDataW.title("Get Account Data")
        i = 0
        while i < 6:
            self.getDataW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.getDataW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        Lbl = tkinter.Label(self.getDataW, text="ID ")
        Lbl.grid(row=1, column=1)
        # Button
        BTN = tkinter.Button(self.getDataW, text="Enter", width=10, command=self.getDataBtn)
        BTN.grid(row=5, column=2)
        # Entry
        self.getData_Entry = tkinter.Entry(self.getDataW)
        self.getData_Entry.grid(row=1, column=2)

    def getDataBtn(self):
        val = self.getData_Entry.get()
        if val in DB:
            r = open(val + "/data.txt", "r")
            list = eval(r.read())
            r.close()
            self.printAccData(list, val)
            self.getDataW.destroy()
        else:
            # label
            lbl = tkinter.Label(self.getDataW, text="ID doesnt exist")
            lbl.grid(row=3, column=2)

    # Search With Name
    def searchNameInit(self):
        self.searchNameW = tkinter.Toplevel()
        self.searchNameW.geometry("250x150+670+200")
        self.searchNameW.resizable(False, False)
        self.searchNameW.title("Get Account Data")
        i = 0
        while i < 6:
            self.searchNameW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.searchNameW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        Lbl = tkinter.Label(self.searchNameW, text="Name ")
        Lbl.grid(row=1, column=1)
        # Button
        BTN = tkinter.Button(self.searchNameW, text="Enter", width=10, command=self.searchNameBtn)
        BTN.grid(row=5, column=2)
        # Entry
        self.searchName_Entry = tkinter.Entry(self.searchNameW)
        self.searchName_Entry.grid(row=1, column=2)

    def searchNameBtn(self):
        val = self.searchName_Entry.get()
        for (k, v) in DB.items():
            if v[0].loWer() == val.loWer():
                print(k)
                r = open(k + "/data.txt", "r")
                list = eval(r.read())
                r.close()
                self.printAccData(list, k)
                self.searchNameW.destroy()
                return
        # label
        lbl = tkinter.Label(self.searchNameW, text="Name doesnt exist")
        lbl.grid(row=3, column=2)


    def printAccData(self, list, id):
        self.printAccDataW = tkinter.Toplevel()
        self.printAccDataW.geometry("280x150+670+200")
        self.printAccDataW.resizable(False, False)
        self.printAccDataW.title("Account Data")
        i = 0
        while i < 6:
            self.printAccDataW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.printAccDataW.grid_columnconfigure(i, minsize=30)
            i += 1
        # label
        lbl = tkinter.Label(self.printAccDataW, text="ID:  " + id)
        lbl.grid(row=0, column=1)
        lbl = tkinter.Label(self.printAccDataW, text="Name: " + list[0])
        lbl.grid(row=1, column=1)
        lbl = tkinter.Label(self.printAccDataW, text="Password: " + list[1])
        lbl.grid(row=2, column=1)
        lbl = tkinter.Label(self.printAccDataW, text="Balance: " + list[2])
        lbl.grid(row=3, column=1)
        # Button
        BTN = tkinter.Button(self.printAccDataW, text="Close", width=10, command=self.printAccDataW.destroy)
        BTN.grid(row=5, column=1)


class New_User():

    def newUser(self):
        self.nUsrW = tkinter.Toplevel()
        self.nUsrW.geometry("300x140+400+200")
        self.nUsrW.title("New User")
        self.nUsrW.resizable(width=False, height=False)
        #Labels
        User_Label = tkinter.Label(self.nUsrW, text="ID")
        User_Label.grid(row=0, column=0)
        User_Label = tkinter.Label(self.nUsrW, text="Name")
        User_Label.grid(row=1, column=0)
        User_Label = tkinter.Label(self.nUsrW, text="Password")
        User_Label.grid(row=2, column=0)
        User_Label = tkinter.Label(self.nUsrW, text="Balance")
        User_Label.grid(row=3, column=0)
        #Entries
        self.Id_Entry = tkinter.Entry(self.nUsrW)
        self.Id_Entry.grid(row=0, column=1)
        self.Nm_Entry = tkinter.Entry(self.nUsrW)
        self.Nm_Entry.grid(row=1, column=1)
        self.Pw_Entry = tkinter.Entry(self.nUsrW)
        self.Pw_Entry.grid(row=2, column=1)
        self.Bc_Entry = tkinter.Entry(self.nUsrW)
        self.Bc_Entry.grid(row=3, column=1)

        Enter_Button = tkinter.Button(self.nUsrW, text="Enter", command=self.newUserBtn)
        Enter_Button.grid(row=4, column=1)

    def newUserBtn(self):
        userID = self.Id_Entry.get()
        global DB
        if userID in DB:
            ShowMSG("Account exist")
            return
        os.system("mkdir " + str(userID))
        os.system("touch " + str(userID) + "/" + "data.txt")

        lis = [self.Nm_Entry.get(), self.Pw_Entry.get(), self.Bc_Entry.get()]
        saveData(userID, lis)
        # updating Database
        DB[self.Id_Entry.get()] = [self.Nm_Entry.get(), "running"]
        w = open("Database/DB.txt", "w")
        w.write(str(DB))
        w.close()

        self.nUsrW.destroy()
        ShowMSG("Account Created Successfuly", x="300")


class Current_User():
    ID = ""
    trails = 1
    Data = []

    def curUser(self):
        self.curUsrW = tkinter.Toplevel()
        self.curUsrW.geometry("300x130+400+200")
        self.curUsrW.title("Current User")
        self.curUsrW.resizable(width=False, height=False)
        i = 0
        while i < row_num:
            self.curUsrW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < col_num:
            self.curUsrW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        LblLogin = tkinter.Label(self.curUsrW, text="Enter Account Number")
        LblLogin.grid(row=0, column=3)
        # Button
        BTNLogin = tkinter.Button(self.curUsrW, text="Enter", width=10, command=self.curUserBtn)
        BTNLogin.grid(row=3, column=3)
        # Entry
        self.curUser_Entry = tkinter.Entry(self.curUsrW)
        self.curUser_Entry.grid(row=1, column=3)


    def curUserBtn(self):
        self.ID = self.curUser_Entry.get()
        if self.ID in DB:
            if DB[self.ID][1] == "running":
                self.curUsrW.destroy()
    
                self.curUsrPsW = tkinter.Toplevel()
                self.curUsrPsW.geometry("300x130+400+200")
                self.curUsrPsW.resizable(False, False)
                self.curUsrPsW.title("Current User")
                i = 0
                while i < row_num:
                    self.curUsrPsW.grid_rowconfigure(i, minsize=20)
                    i += 1
                i = 0
                while i < col_num:
                    self.curUsrPsW.grid_columnconfigure(i, minsize=20)
                    i += 1
                # label
                LblCorr = tkinter.Label(self.curUsrPsW, text="Enter Password")
                LblCorr.grid(row=0, column=3)
                # Enter Button
                BTNCorr = tkinter.Button(self.curUsrPsW, text="Enter", width=10, command=self.curUsrPsBtn)
                BTNCorr.grid(row=5, column=3)
                # Entry
                self.curUsrPs_Entry = tkinter.Entry(self.curUsrPsW, show="*")
                self.curUsrPs_Entry.grid(row=1, column=3)
    
            else:
                ShowMSG("Account Locked, please go to the branch", x="350", title="Error")
    
        else:
            LblLogin = tkinter.Label(self.curUsrW, text="ID doesnt exist")
            LblLogin.grid(row=2, column=3)


    def curUsrPsBtn(self):
        r = open(str(self.ID) + "/" + "data.txt", "r")
        self.Data = eval(r.read())
        r.close()
        # Valid Password
        if self.curUsrPs_Entry.get() == self.Data[1]:
            self.trails = 1
            self.curUsrPsW.destroy()
            self.serv()
        # Wrong Password
        else:
            # label
            LblLogin = tkinter.Label(self.curUsrPsW, text="Wrong Password, Trail Number: " + str(self.trails))
            LblLogin.grid(row=2, column=3)
            self.trails += 1
            if self.trails == 4:
                DB[self.ID][1] = "locked"
                with open("Database/DB.txt", "w") as w:
                    w.write(str(DB))
                self.curUsrPsW.destroy()
                ShowMSG("Account Locked", title="Error")
                self.trails = 1


    def serv(self):
        self.servW = tkinter.Toplevel()
        self.servW.geometry("350x350+600+150")
        self.servW.resizable(False, False)
        self.servW.title("Services")
        i = 0
        while i < 10:
            self.servW.grid_rowconfigure(i, minsize=40)
            i += 1
        i = 0
        while i < col_num:
            self.servW.grid_columnconfigure(i, minsize=100)
            i += 1
        BTNC = tkinter.Button(self.servW, text="Cash Withdraw", width=15, command=self.cashInit)
        BTNC.grid(row=1, column=1)
        BTNB = tkinter.Button(self.servW, text="Balance Inquiry", width=15, command=self.balanceInit)
        BTNB.grid(row=2, column=1)
        BTNP = tkinter.Button(self.servW, text="Password Change", width=15, command=self.passInit)
        BTNP.grid(row=3, column=1)
        BTNF = tkinter.Button(self.servW, text="Mobile Recharge", width=15, command=self.fawryInit)
        BTNF.grid(row=4, column=1)
        BTNL = tkinter.Button(self.servW, text="Logout", width=15, command=self.servW.destroy)
        BTNL.grid(row=6, column=1)
        BTNE = tkinter.Button(self.servW, text="Exit", width=15, command=exitBtn)
        BTNE.grid(row=7, column=1)


    # Withdraw Balance
    def cashInit(self):
        self.cashW = tkinter.Toplevel()
        self.cashW.geometry("250x150+670+200")
        self.cashW.resizable(False, False)
        self.cashW.title("Cash Withdraw")
        i = 0
        while i < 6:
            self.cashW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.cashW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        LblCash = tkinter.Label(self.cashW, text="Amount")
        LblCash.grid(row=1, column=1)
        # Button
        BTNCash = tkinter.Button(self.cashW, text="Enter", width=10, command=self.cashBtn)
        BTNCash.grid(row=5, column=2)
        # Entry
        self.cash_Entry = tkinter.Entry(self.cashW)
        self.cash_Entry.grid(row=1, column=2)

    def cashBtn(self):
        val = self.cash_Entry.get()
        # Check if Numeric
        if val.isnumeric() == True:
            val = int(val)
    
        else:
            # label
            LblCash = tkinter.Label(self.cashW, text="     Numeric Only     ")
            LblCash.grid(row=3, column=2)
            return
        # Check if less than or equal the maximum
        if val <= 5000:
            pass
        else:
            # label
            LblCash = tkinter.Label(self.cashW, text="    5000 Maximum    ")
            LblCash.grid(row=3, column=2)
            return
        # Check if multiple of 100
        if val % 100 == 0:
            pass
        else:
            # label
            LblCash = tkinter.Label(self.cashW, text="Multiple of 100 only")
            LblCash.grid(row=3, column=2)
            return
        # Check if not 0 or -ve
        if val > 0:
            pass
        else:
            # label
            LblCash = tkinter.Label(self.cashW, text="     Wrong Number     ")
            LblCash.grid(row=3, column=2)
            return
        # Check if value is less or equal Balance
        if val <= int(self.Data[2]):
            # ATM_Actuator_Out(val)
            self.Data[2] = str(int(self.Data[2]) - val)
            saveData(self.ID, self.Data)
            self.cashW.destroy()
            ShowMSG("Thank you")
        else:
            self.cashW.destroy()
            ShowMSG("No sufficient balance", x="250")


    # Balance Inquiry
    def balanceInit(self):
        self.balanceW = tkinter.Toplevel()
        self.balanceW.geometry("300x150+600+150")
        self.balanceW.resizable(False, False)
        self.balanceW.title("Balance")
        i = 0
        while i < row_num:
            self.balanceW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < col_num:
            self.balanceW.grid_columnconfigure(i, minsize=50)
            i += 1
        # label For Name
        LblBal = tkinter.Label(self.balanceW, text=("Your Name: " + str(self.Data[0])))
        LblBal.grid(row=2, column=2)
        # label For Balance
        LblBal2 = tkinter.Label(self.balanceW, text=("Your Balance: " + str(self.Data[2])))
        LblBal2.grid(row=3, column=2)
        # Button
        BTNBal = tkinter.Button(self.balanceW, text="OK", width=10, command=self.balanceW.destroy)
        BTNBal.grid(row=5, column=2)


    # Change Password
    def passInit(self):
        self.chPasW = tkinter.Toplevel()
        self.chPasW.geometry("350x150+670+200")
        self.chPasW.resizable(False, False)
        self.chPasW.title("Password Change")
        i = 0
        while i < 6:
            self.chPasW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.chPasW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        LblP = tkinter.Label(self.chPasW, text="New Password")
        LblP.grid(row=1, column=0)
        # label
        LblPR = tkinter.Label(self.chPasW, text="Repeat Password")
        LblPR.grid(row=2, column=0)
        # Button
        BTNPC = tkinter.Button(self.chPasW, text="Change Password", width=20, command=self.chPasBtn)
        BTNPC.grid(row=5, column=1)
        # Entry
        global chPas_Entry
        chPas_Entry = tkinter.Entry(self.chPasW)
        chPas_Entry.grid(row=1, column=1)
        # Entry
        global chPas_Entry2
        chPas_Entry2 = tkinter.Entry(self.chPasW)
        chPas_Entry2.grid(row=2, column=1)

    def chPasBtn(self):
        val1 = chPas_Entry.get()
        val2 = chPas_Entry2.get()
        # Check if the two passwords match
        if val1 != val2:
            # label
            LblPass = tkinter.Label(self.chPasW, text="   passwords must match                  ")
            LblPass.grid(row=3, column=1)
            return
        # Check if password with length four
        elif len(val1) != 4 and len(val2) != 4:
            # label
            LblPass = tkinter.Label(self.chPasW, text="password must be with length four")
            LblPass.grid(row=3, column=1)
            return
        else:
            self.Data[1] = str(val1)
            saveData(self.ID, self.Data)
            self.chPasW.destroy()
            ShowMSG("Done")


    # Mobile Recharges
    def fawryInit(self):
        self.fawryW = tkinter.Toplevel()
        self.fawryW.geometry("350x325+600+150")
        self.fawryW.resizable(False, False)
        self.fawryW.title("Mobile Recharge")
        i = 0
        while i < 10:
            self.fawryW.grid_rowconfigure(i, minsize=40)
            i += 1
        i = 0
        while i < col_num:
            self.fawryW.grid_columnconfigure(i, minsize=110)
            i += 1
        BTNO = tkinter.Button(self.fawryW, text="Jio Recharge", width=15, command=self.fawryChargeBtn)
        BTNO.grid(row=1, column=1)
        BTNE = tkinter.Button(self.fawryW, text="Airtel Recharge", width=15, command=self.fawryChargeBtn)
        BTNE.grid(row=2, column=1)
        BTNV = tkinter.Button(self.fawryW, text="Vodafone Recharge", width=15, command=self.fawryChargeBtn)
        BTNV.grid(row=3, column=1)
        BTNW = tkinter.Button(self.fawryW, text="BSNL Recharge", width=15, command=self.fawryChargeBtn)
        BTNW.grid(row=4, column=1)
        BTNC = tkinter.Button(self.fawryW, text="Close", width=15, command=self.fawryW.destroy)
        BTNC.grid(row=6, column=1)

    def fawryChargeBtn(self):
        self.fawryChargeW = tkinter.Toplevel()
        self.fawryChargeW.geometry("250x150+670+200")
        self.fawryChargeW.resizable(False, False)
        self.fawryChargeW.title("Mobile Recharge")
        i = 0
        while i < 6:
            self.fawryChargeW.grid_rowconfigure(i, minsize=20)
            i += 1
        i = 0
        while i < 3:
            self.fawryChargeW.grid_columnconfigure(i, minsize=20)
            i += 1
        # label
        LblFB = tkinter.Label(self.fawryChargeW, text="Number")
        LblFB.grid(row=1, column=1)
        # label
        LblFB2 = tkinter.Label(self.fawryChargeW, text="Amount")
        LblFB2.grid(row=2, column=1)
        # Button
        BTNFB = tkinter.Button(self.fawryChargeW, text="Enter", width=10, command=self.rechargeBtn)
        BTNFB.grid(row=5, column=2)
        # Number Entry
        self.fawryNum_Entry = tkinter.Entry(self.fawryChargeW)
        self.fawryNum_Entry.grid(row=1, column=2)
        # Amount Entry
        self.fawryAmount_Entry = tkinter.Entry(self.fawryChargeW)
        self.fawryAmount_Entry.grid(row=2, column=2)

    def rechargeBtn(self):
        val = self.fawryAmount_Entry.get()

        # Check if Numeric
        if (val.isnumeric() == True) and (self.fawryNum_Entry.get().isnumeric() == True):
            val = int(val)
        else:
            # label
            LblCash = tkinter.Label(self.fawryChargeW, text="    Numeric Only    ")
            LblCash.grid(row=3, column=2)
            return
        # Check if value is less or equal Balance
        if val <= int(self.Data[2]):
            self.Data[2] = str(int(self.Data[2]) - val)
            saveData(self.ID, self.Data)
            self.fawryChargeW.destroy()
            ShowMSG("Thank you")
        else:
            self.fawryChargeW.destroy()
            ShowMSG("No sufficient balance", x="220")


def exitBtn():
    StartW.quit()

def ShowMSG(msg, x="200", title="Message", BtnText="Close"):
    winMSG = tkinter.Toplevel()
    winMSG.geometry(x + "x100+685+230")
    winMSG.resizable(False, False)
    winMSG.title(title)
    i = 0
    while i < 2:
        winMSG.grid_rowconfigure(i, minsize=25)
        i += 1
    i = 0
    while i < 2:
        winMSG.grid_columnconfigure(i, minsize=55)
        i += 1
    # label
    LblMSG = tkinter.Label(winMSG, text=(str(msg)))
    LblMSG.grid(row=1, column=1)
    # Button
    BTNMSG = tkinter.Button(winMSG, text=BtnText, width=10, command=winMSG.destroy)
    BTNMSG.grid(row=2, column=1)

def saveData(dir, list):
    w = open(str(dir) + "/" + "data.txt", "w")
    w.write(str(list))
    w.close()


