from tkinter import *
from tkinter import messagebox
import sys
import os
import mysql.connector
from mysql.connector import Error

py = sys.executable


#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.iconbitmap(r'libico.ico')
        self.maxsize(1920, 1080)
        self.minsize(1200, 700)
        self.configure(bg="pale green")
        self.title("BI-KAT LIBRARY MANAGEMENT SYSTEM")



#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='librarymn',
                                         user='root',
                                         password='Admin_123_4')
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `admin` where user= %s AND password = %s ',(user,password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'options.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

        def check():


                    self.label = Label(self, text="LOGIN", bg = 'pale green', fg = 'sea green', font=("Times New Roman", 24,'bold'))
                    self.label.place(x=600, y=130)
                    self.label1 = Label(self, text="USER ID:" , bg = 'pale green' , fg = 'sea green', font=("courier-new", 15, 'bold'))
                    self.label1.place(x=340, y=210)
                    self.user_text = Entry(self, textvariable=self.a, width=45)
                    self.user_text.place(x=520, y=210)
                    self.label2 = Label(self, text="PASSWORD:" , bg = 'pale green' , fg = 'sea green', font=("courier-new", 15, 'bold'))
                    self.label2.place(x=340, y=260)
                    self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
                    self.pass_text.place(x=520, y=260)
                    self.butt = Button(self, text="Login",bg ='sea green',fg='white', font=10, width=8, command=chex).place(x=620, y=300)
                    self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='pale green', fg='sea green', font=("Times New Roman", 24, 'bold'))
                    self.label3.place(x=350, y=30)


        check()

Lib().mainloop()