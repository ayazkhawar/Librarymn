from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove User")
        self.canvas = Canvas(width=1366, height=768, bg='pale green')
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='librarymn',
                                         user='root',
                                         password='Admin_123_4')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")


        Label(self, text = "ENTER USER ID ",bg='pale green',fg='sea green',font=('Courier new', 15, 'bold')).place(x = 130,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 100,y = 90)
        Button(self, text='Remove', width=15,bg='sea green',fg='white', font=('arial', 10),command = ent).place(x=145, y = 130)



Rem().mainloop()