from tkinter import*
import cours_db
from tkinter import messagebox
win=Tk()
win.title('Form')
win.geometry('600x400')


#_______________Labable__________

lbl=Label(win,text='name',font='tahoma 13').place(x=50,y=20)
lbl=Label(win,text='lname',font='tahoma 13').place(x=300,y=20)
lbl=Label(win,text='name course',font='tahoma 13').place(x=30,y=50)
lbl=Label(win,text='password',font='tahoma 13').place(x=300,y=50)
lbl=Label(win,text=' : password login',font='tahoma 11').place(x=425,y=325)


#____________Function_________
ri1=cours_db.Register('D:/p_database/cours_db')

def select_record():
    listbox.delete(0,END)
    records=ri1.select()
    for record in records:
        listbox.insert(END,record)

def clear():
    entry_name.delete(0,END)
    entry_lname.delete(0,END)
    entry_cours.delete(0,END)
    entry_password.delete(0,END)

def select_insert():
    name=entry_name.get()
    lname=entry_lname.get()
    name_course=entry_cours.get()
    password=entry_password.get()
    ri1.insert(name,lname,name_course,password)
    clear()

def delete_record():
    result=messagebox.askquestion('WARNING','Dou you want it delete?')
    if result == 'yes':
        index=listbox.curselection()
        data=listbox.get(index)
        ri1.delete(data[0])
    select_record()

def exit():
    result=messagebox.askquestion('CLOSE','Dou you want exit?')
    if result=='yes':
        win.destroy()

def login():
    code= entry_login.get().strip()
    if not code :
        messagebox.showwarning("Input Error",'Password is required' )
        return
    user= ri1.validate_user(code)
    if user:
        messagebox.showinfo('sign in successful',f'HELLO{user[1]} {user[2]}!')
        clear()
        entry_login.delete(0,END)
    else:
        messagebox.showerror('Login Filed','Password is incorrect')

#___________Entry___________

entry_name=Entry(win,font='tahoma 10')
entry_name.place(x=134,y=21)

entry_lname=Entry(win,font='tahoma 10')
entry_lname.place(x=397,y=21)

entry_cours=Entry(win,font='tahoma 10')
entry_cours.place(x=134,y=53)

entry_password=Entry(win,font='tahoma 10')
entry_password.place(x=397,y=53)

entry_login=Entry(win,font='tahoma 10',width=50)
entry_login.place(x=30,y=330)

#__________Button___________

btn_select=Button(win,text='select',font='tahoma 11',width=11,command=select_record)
btn_select.place(x=430,y=90)


btn_insert=Button(win,text='insert',font='tahoma 11',width=11,command=select_insert)
btn_insert.place(x=430,y=130)


btn_clear=Button(win,text='clear',font='tahoma 11',width=11,command=clear)
btn_clear.place(x=430,y=165)


btn_delete=Button(win,text='delete',font='tahoma 11',width=11,command=delete_record)
btn_delete.place(x=430,y=200)

btn_exit=Button(win,text='exit',font='tahoma 11',width=11,command=exit)
btn_exit.place(x=430,y=235)

btn_login=Button(win,text='login',font='tahoma 11',width=11,command=login)
btn_login.place(x=430,y=270)


#____________LIstbox__________

listbox=Listbox(win,width=62,height=13)
listbox.place(x=30,y=94)












win.mainloop()