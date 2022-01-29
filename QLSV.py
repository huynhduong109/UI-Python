from sqlite3.dbapi2 import DatabaseError

import tkinter as tk

from tkinter import Button, Entry, Label, Message, StringVar, ttk

from tkinter import messagebox

import sqlite3

from tkinter import font



# return a list from sql statement 

def returnlist(s):

    con = sqlite3.connect('QLSV(2).db')

    cur = con.cursor()

    cur = cur.execute(s)

    return cur.fetchall()


# commit sql

def commitsql(s):

    con = sqlite3.connect('QLSV(2).db')

    cur = con.cursor()

    try:

        cur = cur.execute(s)

        con.commit()

        ok(0)

    except sqlite3.Error as e:

        messagebox.showerror("Error",e)

# create a string

def chuoi(id, name, address, clas):

    s = ""

    if (id!=""):

        s = s + " StudentID='%s'" %(id)

    if (name!=""):

        if (s!=""):

            s = s + " AND StudentName='%s'" %(name)

        else:

            s = s + " StudentName='%s'" %name

    if (address!=""):

        if (s!=""):

            s = s + " AND StudentAddress='%s'" %(address)

        else:

            s = s + " StudentAddress='%s'" %(address)

    if (clas!=""):

        if (s!=""):

            s = s + " AND ClassID='%s'" %(clas)

        else:

            s = s + " ClassID='%s'" %(clas)

    return s

#class
def chuoic(idc, namec, clasy):

    c = ""

    if (idc!=""):

        c = c + " ClassID='%s'" %(idc)

    if (namec!=""):

        if (c!=""):

            c = c + " AND ClassName='%s'" %(namec)

        else:

            c = c + " ClassName='%s'" %(namec)


    if (clasy!=""):

        if (c!=""):

            c = c + " AND ClassYear='%s'" %(clasy)

        else:

            c = c + " ClassYear='%s'" %(clasy)

    return c

#Subject
def chuois(ids, names, unit):

    m = ""

    if (ids!=""):

        m = m + " SubjectID='%s'" %(ids)

    if (names!=""):

        if (m!=""):

            m = m + " AND SubjectName='%s'" %(names)

        else:

            m = m + " SubjectName='%s'" %names

    if (unit!=""):

        if (m!=""):

            m = m + " AND Units='%s'" %(unit)

        else:

            m = m + " Units='%s'" %(unit)

    return m

#grades

def chuoig(id, ids, grade):

    g = ""

    if (id!=""):

        g = g + " StudentID='%s'" %(id)

    if (ids!=""):

        if (g!=""):

            g = g + " AND SubjectID='%s'" %(ids)

        else:

            g = g + " SubjectID='%s'" %ids

    if (grade!=""):

        if (g!=""):

            g = g + " AND Grades='%s'" %(grade)

        else:

            g = g + " Grades='%s'" %(grade)

    return g

def settree(list):

    for i in tree.get_children():

        tree.delete(i)

    for i in list:

        tree.insert('',tk.END,values=i)
        
#class



def ok(f):

    s = "SELECT * FROM Student "

    if (data.get()!='All'):

        s = s + "WHERE" + chuoi("","","",data.get())

    settree(returnlist(s))

#class
def okc(c):

    s = "SELECT * FROM Class "

    if (data.get()!='All'):

        s = s + "WHERE" + chuoic("","",data.get())
    settree(returnlist(s))
    
#subject
def oks(s):

    s = "SELECT * FROM Subject "

    if (data.get()!='All'):

        s = s + "WHERE" + chuois("","",data.get())

    settree(returnlist(s))

#grade
def okg(g):

    s = "SELECT * FROM StudentGrades "

    if (data.get()!='All'):

        s = s + "WHERE" + chuoig("","",data.get())

    settree(returnlist(s))

def okinsert():

    s = "INSERT INTO Student VALUES('%s','%s','%s','%s');" %(id.get(), name.get(), address.get(), clas.get())

    print(s)

    commitsql(s)
    
#class
def okinsertc():

    s = "INSERT INTO Class VALUES('%s','%s','%s');" %(idc.get(), namec.get(), clasy.get())

    print(s)

    commitsql(s)
    
#subject
def okinserts():

    s = "INSERT INTO Subject VALUES('%s','%s','%s');" %(ids.get(), names.get(), unit.get())

    print(s)

    commitsql(s)

#grade
def okinsertg():

    s = "INSERT INTO StudentGrades VALUES('%s','%s','%s');" %(id.get(), ids.get(), grade.get())

    print(s)

    commitsql(s)

def okdelete():

    s = "DELETE FROM Student WHERE" + chuoi(id.get(), name.get(), address.get(), clas.get())

    print(s)

    commitsql(s)
    
#class
def okdeletec():

    s = "DELETE FROM Class WHERE" + chuoic(idc.get(), namec.get(), clasy.get())

    print(s)

    commitsql(s)
    
#subject
def okdeletes():

    s = "DELETE FROM Subject WHERE" + chuois(ids.get(), names.get(), unit.get())

    print(s)

    commitsql(s)

#grade
def okdeleteg():

    s = "DELETE FROM StudentGrades WHERE" + chuoig(id.get(), ids.get(), grade.get())

    print(s)

    commitsql(s)
        

    

def okupdate():

    s = "UPDATE Student SET" + chuoi("",name.get(), address.get(), clas.get()) + " WHERE" + chuoi(id.get(),"","","")

    s = s.replace("AND", ",")

    print(s)

    commitsql(s)
    
#class
def okupdatec():

    s = "UPDATE Class SET" + chuoic("",namec.get(), clasy.get()) + " WHERE" + chuoic(idc.get(),"","")

    s = s.replace("AND", ",")

    print(s)

    commitsql(s)
#subject
def okupdates():

    s = "UPDATE Subject SET" + chuois("",names.get(), unit.get()) + " WHERE" + chuois(ids.get(),"","")

    s = s.replace("AND", ",")

    print(s)

    commitsql(s)
    
#grade
def okupdateg():

    s = "UPDATE StudentGrades SET" + chuoig("",ids.get(), grade.get()) + " WHERE" + chuoig(id.get(),"","")

    s = s.replace("AND", ",")

    print(s)

    commitsql(s)
    

def oksearch():

    s = "SELECT * FROM Student WHERE" + chuoi(id.get(), name.get(), address.get(), clas.get())    

    print(s)

    settree(returnlist(s))
    
#class
def oksearchc():

    s = "SELECT * FROM Class WHERE" + chuoic(idc.get(), namec.get(), clasy.get())    

    print(s)

    settree(returnlist(s))
    
#subject
def oksearchs():

    s = "SELECT * FROM Subject WHERE" + chuois(ids.get(), names.get(), unit.get())    

    print(s)

    settree(returnlist(s))
    
#grade
def oksearchg():

    s = "SELECT * FROM StudentGrades WHERE" + chuoig(id.get(), ids.get(), grade.get())    

    print(s)

    settree(returnlist(s))
    

def insert():

    id.set("")

    name.set("")

    clas.set("")

    address.set("")

    ap = app2("insert", okinsert)

    clas.set(data.get())

    ap.mainloop()
    
#class
def insertc():

    idc.set("")

    namec.set("")

    clasy.set("")

    ap = app2c("Insert", okinsertc)

    idc.set(data.get())

    ap.mainloop()
    
#subject
def inserts():

    ids.set("")

    names.set("")

    unit.set("")

    ap = app2s("Insert", okinserts)

    ids.set(data.get())

    ap.mainloop()
    
#grade
def insertg():

    id.set("")

    ids.set("")

    grade.set("")

    ap = app2g("Insert", okinsertg)

    grade.set(data.get())

    ap.mainloop()
    

def delete():

    ap = app3(okdelete)

    ap.mainloop()
    
#class
def deletec():

    ap = app3(okdeletec)

    ap.mainloop()

#subject
def deletes():

    ap = app3(okdeletes)

    ap.mainloop()
    
#grade
def deleteg():

    ap = app3(okdeleteg)

    ap.mainloop()
        

def update():

    ap = app2("update", okupdate)

    clas.set(data.get())

    ap.mainloop()
    
#class
def updatec():

    ap = app2c("update", okupdatec)

    idc.set(data.get())

    ap.mainloop()

#subject
def updates():

    ap = app2s("update", okupdates)

    ids.set(data.get())

    ap.mainloop()
    
#grade
def updateg():

    ap = app2g("update", okupdateg)

    id.set(data.get())

    ap.mainloop()

def search():

    id.set("")

    name.set("")

    clas.set("")

    address.set("")

    ap = app2("search", oksearch)

    ap.mainloop()
    
#class
def searchc():

    idc.set("")

    namec.set("")

    clasy.set("")

    ap = app2c("search", oksearchc)

    ap.mainloop()
    
#subject
def searchs():

    ids.set("")

    names.set("")

    unit.set("")

    ap = app2s("search", oksearchs)

    ap.mainloop()
    
#grade
def searchg():

    id.set("")

    ids.set("")

    grade.set("")

    ap = app2g("search", oksearchg)

    ap.mainloop()

def xuat():

    print(id.get())
    
#class
def xuatc():

    print(idc.get())
    
#subject
def xuats():

    print(ids.get())
    
#grade
def xuatg():

    print(grade.get())
    

class app3(tk.Toplevel):

    def __init__(self,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        Label(self,text="This line will be permanently deleted. Do you still want to delete?", font="20").pack()

        Button(self, text="0K", command=dk, width=15).pack()
        Button(self, text="Cancel", command=self.destroy, width=15).pack()

class app2(tk.Toplevel):

    def __init__(self,st,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        

        

        

        self.title(st)

        Label(self, text="StudentID", width=15).grid(row=0, column=0)

        Entry(self, textvariable=id).grid(row=0, column=1, sticky=tk.E + tk.W)

        Label(self, text="StudentName", width=15).grid(row=1, column=0)

        Entry(self, textvariable=name).grid(row=1, column=1, sticky=tk.E + tk.W)

        Label(self, text="StudentAddress", width=15).grid(row=2, column=0)

        Entry(self, textvariable=address).grid(row=2, column=1, sticky=tk.E + tk.W)

        Label(self, text="ClassID", width=15).grid(row=4, column=0)

        lst2 = ("C01", "C02", "C03", "C04", "C05", "C06")

        combox2 = ttk.Combobox(self, textvariable=clas)

        combox2['value'] = lst2

        combox2['state'] = 'readonly'

        combox2.grid(row=4, column=1)

        Button(self, text="OK", command=dk, width=5).grid(row=5, column=0)

        Button(self, text="Quit", command=self.destroy, width=5).grid(row=5, column=1)
        
#class
class app2c(tk.Toplevel):

    def __init__(self,st,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        

        

        

        self.title(st)

        Label(self, text="ClassID", width=15).grid(row=0, column=0)

        Entry(self, textvariable=idc).grid(row=0, column=1, sticky=tk.E + tk.W)

        Label(self, text="ClassName", width=15).grid(row=1, column=0)

        Entry(self, textvariable=namec).grid(row=1, column=1, sticky=tk.E + tk.W)

        Label(self, text="ClassYear", width=15).grid(row=2, column=0)

        Entry(self, textvariable=clasy).grid(row=2, column=1, sticky=tk.E + tk.W)

        Button(self, text="OK", command=dk, width=5).grid(row=5, column=0)

        Button(self, text="Quit", command=self.destroy, width=5).grid(row=5, column=1)
        
#subject
class app2s(tk.Toplevel):

    def __init__(self,st,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        

        

        

        self.title(st)

        Label(self, text="SubjectID", width=15).grid(row=0, column=0)

        Entry(self, textvariable=ids).grid(row=0, column=1, sticky=tk.E + tk.W)

        Label(self, text="SubjectName", width=15).grid(row=1, column=0)

        Entry(self, textvariable=names).grid(row=1, column=1, sticky=tk.E + tk.W)

        Label(self, text="Units", width=15).grid(row=2, column=0)

        Entry(self, textvariable=unit).grid(row=2, column=1, sticky=tk.E + tk.W)

        Button(self, text="OK", command=dk, width=5).grid(row=5, column=0)

        Button(self, text="Quit", command=self.destroy, width=5).grid(row=5, column=1)
        
#grade
class app2g(tk.Toplevel):

    def __init__(self,st,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        

        

        

        self.title(st)

        Label(self, text="StudentID", width=15).grid(row=0, column=0)

        Entry(self, textvariable=id).grid(row=0, column=1, sticky=tk.E + tk.W)

        Label(self, text="SubjectID", width=15).grid(row=1, column=0)

        Entry(self, textvariable=ids).grid(row=1, column=1, sticky=tk.E + tk.W)

        Label(self, text="StudentGrades", width=15).grid(row=2, column=0)

        Entry(self, textvariable=grade).grid(row=2, column=1, sticky=tk.E + tk.W)

        Button(self, text="OK", command=dk, width=5).grid(row=5, column=0)

        Button(self, text="Quit", command=self.destroy, width=5).grid(row=5, column=1)

class frame1(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        ttk.Label(self, text="STUDENT", font="20", relief='raised').grid(row=0)

        lst = ("All", "C01", "C02", "C03", "C04", "C05", "C06")

        

        global combox, data

        data = StringVar()

        combox = ttk.Combobox(self, textvariable=data)

        combox['value'] = lst 

        combox['state'] = 'readonly'

        combox.grid(row=1)

        combox.bind('<<ComboboxSelected>>', ok)
        
#class
class frame1c(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        ttk.Label(self, text="CLASS", font="20", relief='raised').grid(row=0)

        lstc = ("All")

        

        global combox, data

        data = StringVar()

        combox = ttk.Combobox(self, textvariable=data)

        combox['value'] = lstc

        combox['state'] = 'readonly'

        combox.grid(row=1)

        combox.bind('<<ComboboxSelected>>', okc)
        
#subject
class frame1s(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        ttk.Label(self, text="SUBJECT", font="20", relief='raised').grid(row=0)

        lsts = ("All")

        

        global combox, data

        data = StringVar()

        combox = ttk.Combobox(self, textvariable=data)

        combox['value'] = lsts 

        combox['state'] = 'readonly'

        combox.grid(row=1)

        combox.bind('<<ComboboxSelected>>', oks)
        
#grade

class frame1g(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        ttk.Label(self, text="STUDENT GRADES", font="20", relief='raised').grid(row=0)

        lstg = ("All")

        

        global combox, data

        data = StringVar()

        combox = ttk.Combobox(self, textvariable=data)

        combox['value'] = lstg 

        combox['state'] = 'readonly'

        combox.grid(row=1)

        combox.bind('<<ComboboxSelected>>', okg)


def item_selected(f):

    for selected_item in tree.selection():

        # dictionary

        item = tree.item(selected_item)

        # list

        record = item['values']

        print(record)

        id.set(record[0])

        name.set(record[1])

        address.set(record[2])

        clas.set(record[3])

#class
def item_selectedc(c):

    for selected_item in tree.selection():

        # dictionary

        item = tree.item(selected_item)

        # list

        record = item['values']

        print(record)

        idc.set(record[0])

        namec.set(record[1])

        clasy.set(record[2])
        
#subject

def item_selecteds(s):

    for selected_item in tree.selection():

        # dictionary

        item = tree.item(selected_item)

        # list

        record = item['values']

        print(record)

        ids.set(record[0])

        names.set(record[1])

        unit.set(record[2])
        
#grade

def item_selectedg(g):

    for selected_item in tree.selection():

        # dictionary

        item = tree.item(selected_item)

        # list

        record = item['values']

        print(record)

        id.set(record[0])

        ids.set(record[1])

        grade.set(record[2])


class frame2(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        global tree

        colums = ('#1', '#2', '#3', '#4')

        tree = ttk.Treeview(self, columns=colums, show='headings')

        # define heading

        tree.heading('#1', text="StudentID")

        tree.heading('#2', text="StudentName")

        tree.heading('#3', text="StudentAddress")

        tree.heading('#4', text="ClassID")

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)

        tree.config(yscroll=scrollbar.set)

        tree.bind('<<TreeviewSelect>>', item_selected)

        scrollbar.grid(row=0, column=1, sticky='ns')
        
#class

class frame2c(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        global tree

        colums = ('#1', '#2', '#3')

        tree = ttk.Treeview(self, columns=colums, show='headings')

        # define heading

        tree.heading('#1', text="ClassID")

        tree.heading('#2', text="ClassName")

        tree.heading('#3', text="ClassYear")

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)

        tree.config(yscroll=scrollbar.set)

        tree.bind('<<TreeviewSelect>>', item_selectedc)

        scrollbar.grid(row=0, column=1, sticky='ns')
        
#subject

class frame2s(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        global tree

        colums = ('#1', '#2', '#3')

        tree = ttk.Treeview(self, columns=colums, show='headings')

        # define heading

        tree.heading('#1', text="SubjectID")

        tree.heading('#2', text="SubjectName")

        tree.heading('#3', text="Units")

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)

        tree.config(yscroll=scrollbar.set)

        tree.bind('<<TreeviewSelect>>', item_selecteds)

        scrollbar.grid(row=0, column=1, sticky='ns')
        
        
#grade

class frame2g(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        global tree

        colums = ('#1', '#2', '#3')

        tree = ttk.Treeview(self, columns=colums, show='headings')

        # define heading

        tree.heading('#1', text="StudentID")

        tree.heading('#2', text="SubjectID")

        tree.heading('#3', text="Grades")

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)

        tree.config(yscroll=scrollbar.set)

        tree.bind('<<TreeviewSelect>>', item_selectedg)

        scrollbar.grid(row=0, column=1, sticky='ns')
        
        
        

class frame3(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        Button(self, text="Insert", width=15, command=insert).grid(row=0, column=0)

        Button(self, text="Delete", width=15, command=delete).grid(row=0, column=1)

        Button(self, text="Update", width=15, command=update).grid(row=0, column=2)

        Button(self, text="Search", width=15, command=search).grid(row=0, column=3)

        Button(self, text="Quit", width=15, command=parent.destroy).grid(row=0, column=4)
        
#class

class frame3c(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        Button(self, text="Insert", width=15, command=insertc).grid(row=0, column=0)

        Button(self, text="Delete", width=15, command=deletec).grid(row=0, column=1)

        Button(self, text="Update", width=15, command=updatec).grid(row=0, column=2)

        Button(self, text="Search", width=15, command=searchc).grid(row=0, column=3)

        Button(self, text="Quit", width=15, command=parent.destroy).grid(row=0, column=4)
        
        
#subject

class frame3s(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        Button(self, text="Insert", width=15, command=inserts).grid(row=0, column=0)

        Button(self, text="Delete", width=15, command=deletes).grid(row=0, column=1)

        Button(self, text="Update", width=15, command=updates).grid(row=0, column=2)

        Button(self, text="Search", width=15, command=searchs).grid(row=0, column=3)

        Button(self, text="Quit", width=15, command=parent.destroy).grid(row=0, column=4)
        
        
#grade

class frame3g(tk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent, *args, **kwargs)

        Button(self, text="Insert", width=15, command=insertg).grid(row=0, column=0)

        Button(self, text="Delete", width=15, command=deleteg).grid(row=0, column=1)

        Button(self, text="Update", width=15, command=updateg).grid(row=0, column=2)

        Button(self, text="Search", width=15, command=searchg).grid(row=0, column=3)

        Button(self, text="Quit", width=15, command=parent.destroy).grid(row=0, column=4)
        
        

class app(tk.Toplevel):

    def __init__(self,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        global id, name, address, clas, combox2

        id=tk.StringVar() 

        name=tk.StringVar()

        address=tk.StringVar()  

        clas= tk.StringVar()

        frame1(self).pack()

        frame2(self).pack()

        frame3(self).pack()

        self.geometry("1024x500")

        self.title("Student")
        
#class
class appc(tk.Toplevel):

    def __init__(self,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        global idc, namec, clasy, combox2

        idc=tk.StringVar() 

        namec=tk.StringVar()

        clasy= tk.StringVar()
        
        frame1c(self).pack()

        frame2c(self).pack()

        frame3c(self).pack()
        
        self.geometry("1024x500")

        self.title("Class")
    
#subject
class apps(tk.Toplevel):

    def __init__(self,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        global ids, names, unit, combox2

        ids=tk.StringVar() 

        names=tk.StringVar()

        unit= tk.StringVar()
        
        frame1s(self).pack()

        frame2s(self).pack()

        frame3s(self).pack()
        
        self.geometry("1024x500")

        self.title("Subject")

#grade
class appg(tk.Toplevel):

    def __init__(self,dk, *args, **kwargs):

        super().__init__(*args, **kwargs)

        global id, ids, grade, combox2

        id=tk.StringVar() 

        ids=tk.StringVar()

        grade= tk.StringVar()
        
        frame1g(self).pack()

        frame2g(self).pack()

        frame3g(self).pack()
        
        self.geometry("1024x500")

        self.title("StudentGrades")


#student


def student():

    ap = app(ok)

    ap.mainloop()
    
    
#class


def classc():
    ap=appc(okc)
    ap.mainloop()
    
    
#subject


def subject():
    ap=apps(oks)
    ap.mainloop()
    
    
#grade


def grade():
    ap=appg(okg)
    ap.mainloop()


class window(tk.Tk):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        Label(self,text="STUDENT  MANAGEMENT", font="Arial 20 bold", fg= "white", bg="blue").pack()
        Label(self,text="MENU", font="Arial 20 bold", fg= "red", bg="blue").place(x=250,y=70)
        
        Button(self,text="Student",font="Arial 9 bold", width=28, height=5, command =student, bg="pink").place(x=80,y=150)
        Button(self,text="Class",font="Arial 9 bold",width=28, height=5, command =classc, bg="green").place(x=310,y=150)
        Button(self,text="Subject",font="Arial 9 bold",width=28, height=5, command =subject, bg="red").place(x=80,y=260)
        Button(self,text="StudentGrades",font="Arial 9 bold",width=28, height=5, command =grade, bg="white").place(x=310,y=260)
        
        self.geometry("600x400")

        self.title("QuanLiSinhVien")
        
        self.configure(background="blue")

ap = window()

ap.mainloop()
