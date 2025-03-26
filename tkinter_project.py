from tkinter import *

master = Tk()
master.geometry("1200x1200")
master.title("title")
master.resizable(width=False,height=False)





def signup():

    username = username_entry.get()
    print(username)

    age = ageVar.get()
    print(age)

    password = password_entry.get()
    print(password)

    ageVar0.set(age)

    usernameVar.set(username)

    passwordVar.set(password)

username_label = Label(master, text="Username:")
username_label.pack(pady=10)

username_entry = Entry(master)
username_entry.pack()


password_label = Label(master, text="Password:")
password_label.pack(pady=10)

password_entry = Entry(master, show="*")
password_entry.pack()

age_label = Label(master, text="age")
age_label.pack(pady=10)

ageVar = IntVar()
age_scale = Scale(master, variable=ageVar, from_=0, to=100, orient=HORIZONTAL)
age_scale.pack()

register_button = Button(master, text="register", command=signup)
register_button.pack(pady=30)


username_label0 = Label(master, text="Username:")
username_label0.place(x=500, y=289)

usernameVar = StringVar()
LabelUsername = Label(master, textvariable=usernameVar)
LabelUsername.pack()

age_label0 = Label(master, text="age:")
age_label0.place(x=500, y=309)

ageVar0 = StringVar()
labelAge = Label(master, textvariable=ageVar0)
labelAge.pack()

password_label0 = Label(master, text="Password:")
password_label0.place(x=500, y=329)

passwordVar = StringVar()
labelpasswored = Label(master, textvariable=passwordVar)
labelpasswored.pack()


master.mainloop()