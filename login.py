from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from PIL import ImageTk

def clear():
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    

def login_user():
    Username=usernameEntry.get();
    Password=passwordEntry.get();

    if Username=='' or Password=='':
        messagebox.showerror('Error','All fields are required')

    else:
        try:
            con=mysql.connect(host='localhost',user='root',password='paru',port='3306',database='project1')
            cursor=con.cursor()
            print('Connected to Database successfully!!!')
           
        except:
            messagebox.showerror('Error','Database is not connected')
            return

        command='use project1'
        cursor.execute(command)

        command='select * from datas where Username=%s and Password=%s'
        cursor.execute(command,(Username,Password))
        myresult=cursor.fetchone()
        #print(myresult)

        if myresult==None:
            messagebox.showinfo('Invalid','Invalid Username or Password')
        else:
            messagebox.showinfo('Login','Succesfully Login!!!')
        clear()
        
       
        
def sign_up():
    login.destroy()
    import signup
    

def user_enter(a):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def user_leave(a):
    if usernameEntry.get()=='':
        usernameEntry.insert(0,'Username')

def pass_enter(a):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def pass_leave(a):
    if passwordEntry.get()=='':
        passwordEntry.insert(0,'Password')

def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


login=Tk()
login.resizable(0,0)
login.title('Login Page')


bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login,image=bgImage)
bgLabel.grid()

heading=Label(login,text='USER LOGIN',font=('Times New Roman',21,'bold'),bg='white',fg='SlateBlue4')
heading.place(x=140,y=100)

#username
usernameEntry=Entry(login,width=25,font=('Times New Roman',11,'bold'),bd=0,fg='SlateBlue4')
usernameEntry.place(x=100,y=160)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
usernameEntry.bind('<FocusOut>',user_leave)

frame1=Frame(login,width=250,height=2,bg='SlateBlue4')
frame1.place(x=100,y=180)

#password
passwordEntry=Entry(login,width=25,font=('Times New Roman',11,'bold'),bd=0,fg='SlateBlue4')
passwordEntry.place(x=100,y=210)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',pass_enter)
passwordEntry.bind('<FocusOut>',pass_leave)

frame2=Frame(login,width=250,height=2,bg='SlateBlue4')
frame2.place(x=100,y=230)

#eyebutton
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',
                 command=hide)
eyeButton.place(x=320,y=210)

#forgot button
forgotButton=Button(login,text='Forgot Password?',bd=0,bg='white',font=('Times New Roman',9,'bold'),
                    fg='SlateBlue4',activebackground='white',activeforeground='SlateBlue4',
                    cursor='hand2')
forgotButton.place(x=250,y=250)

#login button
loginButton=Button(login,width=20,text='LOGIN',font=('Times New Roman',13,'bold'),fg='white',
                   bg='SlateBlue4',activeforeground='white',activebackground='SlateBlue4',
                   command=login_user)
loginButton.place(x=120,y=290)

#or label
orLabel=Label(login,text='----------------OR----------------',font=('Times New Roman',17,'bold'),
              bg='white',fg='SlateBlue4')
orLabel.place(x=80,y=350)

alabel=Label(login,text="Don't have an account?",font=('Times New Roman',15,'bold'),bg='white',
             fg='SlateBlue4')
alabel.place(x=80,y=400)

#signin label
newButton=Button(login,text='Create',font=('Times New Roman',13,'bold underline'),bd=0,
                 fg='firebrick1',bg='white',activeforeground='firebrick1',activebackground='white',
                 cursor='hand2',command=sign_up)
newButton.place(x=290,y=400)


login.mainloop()
