from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pywhatkit
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

#creating window
class issue(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title('Library Admisintration')
        self.maxsize(500, 417)
        self.minsize(500,417)

        self.canvas = Canvas(width=1366, height=768, bg='pale green')
        self.canvas.pack()

        c = StringVar()
        d = StringVar()



#verifying input
        def isb():
            if (len(c.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            elif (len(d.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            else:
             try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='librarymn',
                                                        user='root',
                                                        password='Admin_123_4')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select availability from book where availability = 'YES' and book_id = %s", [c.get()])
                    self.pc = self.mycursor.fetchall()
                    try:
                     if self.pc:
                        print("success")
                        book = c.get()
                        stud = d.get()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("Insert into issue_book(book_id,stud_id,issue_date,return_date) values (%s,%s,%s,%s)",
                                              [book, stud, idate,''])
                        self.conn.commit()
                        self.mycursor.execute("Update book set availability = 'NO' where book_id = %s", [book])
                        self.conn.commit()
                        messagebox.showinfo("Success", "Successfully Issue!")
                        ask = messagebox.askyesno("Confirm", "Do you want to add another?")
                        if ask:
                            self.destroy()
                            os.system('%s %s' % (py, 'issueTable.py'))
                        else:
                            self.destroy()
                     else:
                        messagebox.showinfo("Oop's", "Book id "+c.get()+" is not available")
                    except Error:
                        messagebox.showerror("Error", "Check The Details")
             except Error:
                    messagebox.showerror("Error", "Something goes wrong")

        msg = StringVar()
        mobile = StringVar()

        def Send():
            message = msg.get()
            mobiles = mobile.get()

            pywhatkit.sendwhatmsg_instantly(mobiles,message)
#label and input box
        Label(self, text='BOOK ISSUING',fg='sea green', bg = 'pale green', font=('times new roman', 24,'bold')).place(x=135, y=40)
        Label(self, text='BOOK ID:',fg='sea green', bg = 'pale green', font=('Courier new', 10,'bold')).place(x=20, y=120)
        Entry(self, textvariable=c, width=30).place(x=185, y=120)
        Label(self, text='STUDENT ID:',fg='sea green', bg = 'pale green', font=('Courier new', 10,'bold')).place(x=20, y=160)
        Entry(self, textvariable=d, width=30).place(x=185, y=160)
        Label(self, text='ENTER MOBILE NUMBER:',fg='sea green', bg='pale green', font=('Courier new', 10,'bold')).place(x=20, y=200)
        Entry(self, textvariable=mobile, width=30).place(x=185, y=200)
        Label(self, text='ENTER THE MESSAGE:',fg='sea green', bg='pale green', font=('Courier new', 10,'bold')).place(x=20, y=240)
        Entry(self, textvariable=msg, width=30).place(x=185, y=240)

        Button(self, text="Issue", width=15,fg='white', bg='sea green', command=isb).place(x=220, y=280)
        Button(self, text="Send Message", width=15,fg='white', bg='sea green', command=Send).place(x=220, y=320)
issue().mainloop()
