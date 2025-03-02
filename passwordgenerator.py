from tkinter import *
import random
import string
from tkinter import messagebox
import json
#import pylance
def generate():
    s=[]
    1
    for i in range (0,5):
        s.append(str(random.randint(0,9)))
    

    m=["!","@","$","%","^","&","*"]
    for i in range(0,2):
        s.append(random.choice(m))
    
    for i in range(0,3):
        s.append(random.choice(string.ascii_lowercase))
    random.shuffle(s)

    # Join the list into a string and print the final password
    password = ''.join(s)
    entry.insert(0,password)
def find_password():
    website=en.get()
    
   
    try:
        with open("data.json") as file:
            data =json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="error",message="No data file found")
    else:    
        if en.get() in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"email: {email}\npassword: {password}" )
        else:
            messagebox.showinfo(title="error",message=f"{website} is not available ")



def data():
    website=en.get()
    email=ent.get()
    password=entry.get()
    new_data={website:{
        "email":email,
        "password":password
        }
    }
    if(len(website)==0 or len(password)==0):
        messagebox.showinfo(title="OOPs",message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json","r") as file:
                # json.dump(new_data,file,indent=4)
                data=json.load(file)
                data.update(new_data)
            with open("data.json","w")as file:
                json.dump(data,file,indent=4)
        except :
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
                file.close()


    en.delete(0,END)
    ent.delete(0,END)
    entry.delete(0,END)
    
    en.focus()
w=Tk()
w.config(padx=20,pady=20)
p=PhotoImage(file="logo.png")
c=Canvas(width=200,height=200)
c.create_image(100,100,image=p)
c.grid(column=1,row=0)
l=Label(text="Website:")
l.grid(column=0,row=1)
en=Entry(width=35)
en.grid(column=1,row=1,sticky="w")
en.focus()
sn=Button(text="Search",width=30,command=find_password)
sn.grid(row=6,column=1)
la=Label(text="Email Addresss")
la.grid(column=0,row=2)
ent=Entry(width=35)
ent.grid(column=1,row=2,columnspan=2,sticky="w")
pas=Label(text="Password")
pas.grid(column=0,row=3)
entry=Entry(width=35)
entry.grid(column=1,row=3,sticky="w")
B=Button(text="Generate Password",width=30,command=generate)
B.grid(column=1,row=4)
b=Button(text="ADD",width=30,command=data)
b.grid(column=1,row=5)

w.mainloop()