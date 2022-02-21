from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Student')
        self.canvas = Canvas(width=500, height=417, bg='pale green')
        self.canvas.pack()
        i = StringVar()
        n = StringVar()
        p = StringVar()
        a = StringVar()
#verifying input
        def asi():
            if len(i.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Student id")
            elif len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Phone Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Address")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='librarymn',
                                                        user='root',
                                                        password='Admin_123_4')
                    self.myCursor = self.conn.cursor()
                    si1 = i.get()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    self.myCursor.execute("Insert into student(stud_id,name,phone_number,address) values (%s,%s,%s,%s)",[si1,name1,pn1,add1])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add_Student.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='STUDENT DETAILS',bg='pale green', fg='sea green', font=('Times New Roman', 25, 'bold')).place(x=90, y=50)
        Label(self, text='STUDENT ID:', bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=70, y=140)
        Entry(self, textvariable=i, width=30).place(x=200, y=140)
        Label(self, text='NAME:',bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=n, width=30).place(x=200, y=180)
        Label(self, text='PHONE NUMBER:',bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=70, y=220)
        Entry(self, textvariable=p, width=30).place(x=200, y=220)
        Label(self, text='ADDRESS:',bg='pale green',fg='sea green', font=('Courier new', 10, 'bold')).place(x=70, y=260)
        Entry(self, textvariable=a, width=30).place(x=200, y=260)
        Button(self, text="Submit",bg='sea green',fg='white',width = 15,command=asi).place(x=230, y=300)

Add().mainloop()
