from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from PIL import ImageTk

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    conpassEntry.delete(0,END)
    check.set(0)
    

def connect_database():
    Email=emailEntry.get();
    Username=usernameEntry.get();
    Password=passwordEntry.get();
    
    if Email=='' or Username=='' or Password=='' or conpassEntry.get()=='':
        messagebox.showinfo('Error','All fields are required')
    elif passwordEntry.get() != conpassEntry.get():
        messagebox.showinfo('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showinfo('Error','Please accept Terms & Conditions')
    else:
        con=mysql.connect(host='localhost',user='root',password='paru',port='3306',database='project1')
        cursor=con.cursor()
        cursor.execute("insert into datas values('"+Email+"','"+Username+"','"+Password+"')")
        cursor.execute("commit")
        con.close()
        messagebox.showinfo("Success","Registration is successful")
        clear()

        
def login_page():
    signup.destroy()
    import login
    

signup=Tk()
signup.title('SignUp')
signup.resizable(0,0)

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup,image=bgImage)
bgLabel.grid()

#frame
frame=Frame(signup,width=50,height=20,bg='white')
frame.place(x=100,y=90)

#heading label
heading=Label(frame,text='CREATE NEW ACCOUNT',font=('Times New Roman',18,'bold'),bg='white',
              fg='SlateBlue4')
heading.grid(row=0,column=0,padx=10,pady=10)

#email label
Email=Label(frame,text='Email',font=('Times New Roman',11,'bold'),bg='white',
              fg='SlateBlue4')
Email.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=37,font=('Times New Roman',10,'bold'),bg='SlateBlue4',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

#username label
Username=Label(frame,text='Username',font=('Times New Roman',11,'bold'),bg='white',
              fg='SlateBlue4')
Username.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=37,font=('Times New Roman',10,'bold'),bg='SlateBlue4',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

#password label
Password=Label(frame,text='Password',font=('Times New Roman',11,'bold'),bg='white',
              fg='SlateBlue4')
Password.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=37,font=('Times New Roman',10,'bold'),bg='SlateBlue4',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

#confirm password label
conpassLabel=Label(frame,text='Confirm Password',font=('Times New Roman',11,'bold'),bg='white',
              fg='SlateBlue4')
conpassLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
conpassEntry=Entry(frame,width=37,font=('Times New Roman',10,'bold'),bg='SlateBlue4',fg='white')
conpassEntry.grid(row=8,column=0,sticky='w',padx=25)

#agree button
check=IntVar()
terms=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Times New Roman',11,'bold'),
                  bd=0,bg='white',fg='SlateBlue4',activeforeground='SlateBlue4',
                  activebackground='white',cursor='hand2',variable=check)
terms.grid(row=10,column=0,padx=15 ,pady=10)

#signup button
signupButton=Button(frame,width=15,text='Sign Up',font=('Times New Roman',17,'bold'),bg='SlateBlue4',
                    fg='white',activebackground='SlateBlue4',activeforeground='white',cursor='hand2',
                    command=connect_database)
signupButton.grid(row=12,column=0,padx=25,pady=10)

#login button
bLabel=Label(frame,text='Already have an account?',font=('Times New Roman',11,'bold'),bg='white',
             fg='SlateBlue4')
bLabel.grid(row=13,column=0,sticky='w',padx=(45,0),pady=10)

oldButton=Button(signup,text='LogIn',font=('Times New Roman',10,'bold underline'),bd=0,bg='white',
                 fg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',
                 command=login_page)
oldButton.place(x=327,y=467)


signup.mainloop()
