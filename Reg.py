from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
        self.canvas = Canvas(width=500, height=417, bg='pale green')
        self.canvas.pack()
#creating variables Please chech carefully
        x = StringVar()
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='librarymn',
                                         user='root',
                                         password='Admin_123_4')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(id,user,name,password) values (%s,%s,%s,%s)",[x.get(), u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
#label and input
        Label(self, text='USER DETAILS', bg='pale green', fg='sea green', font=('Times New Roman', 20, 'bold')).place(x=150, y=70)
        Label(self, text='USER ID:', bg='pale green', fg='sea green', font=('Courier new', 10, 'bold')).place(x=60,y=140)
        Entry(self, textvariable=x, width=30).place(x=170, y=140)
        Label(self, text='USERNAME:', bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=60, y=170)
        Entry(self, textvariable=u, width=30).place(x=170, y=170)
        Label(self, text='NAME:', bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=60, y=200)
        Entry(self, textvariable=n, width=30).place(x=170, y=200)
        Label(self, text='PASSWORD:', bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=p, width=30).place(x=170, y=232)
        Button(self, text="Submit", width=15, bg='sea green',fg='white', command=insert).place(x=205, y=280)
reg().mainloop()