from tkinter import *
from tkinter import messagebox
from db import get_db

# Initialize the main window
root = Tk()
root.title("Login")
root.geometry("950x500+300+200")
root.configure(background="#fff")
root.resizable(False, False)


# Functions for handling user input
def on_enter(e, entry, placeholder):
    entry.delete(0, 'end')

def on_leave(e, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)

# Function to clear widgets and show main content
def show_main_content():
    for widget in root.winfo_children():
        widget.destroy()
    content_frame = Frame(root, width=950, height=500, bg='white')
    content_frame.pack(fill='both', expand=True)
    Label(content_frame, text='Hello Everyone!', bg='#fff', font=('Calibri', 50, 'bold')).pack(expand=True)

# Function to handle login process
def signin():
    username = user.get()
    password = code.get()
    db = get_db()
    user_record = db.find_one({"username": username})
    if user_record and user_record.get('password') == password:
        show_main_content()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

# Function to show signup frame
def show_signup_frame():
    for widget in root.winfo_children():
        widget.destroy()
    signup_frame = Frame(root, width=950, height=500, bg='#fff')
    signup_frame.pack(fill='both', expand=True)
    ...
    # All code for signup frame remains here

# Function to show login frame
def show_login_frame():
    for widget in root.winfo_children():
        widget.destroy()
    login_frame = Frame(root, width=950, height=500, bg='white')
    login_frame.pack(fill='both', expand=True)
    ...
    # All code for login frame remains here

# Load images for login and signup
img_login = PhotoImage(file='D:/code/AutoMail-Collage-Project/images/login_img.png')
img_signup = PhotoImage(file='D:/code/AutoMail-Collage-Project/images/signup_img.png')

# Function to clear widgets and show main content
def show_main_content():
    for widget in root.winfo_children():
        widget.destroy()

    content_frame = Frame(root, width=950, height=500, bg='white')
    content_frame.pack(fill='both', expand=True)

    Label(content_frame, text='Hello Everyone!', bg='#fff', font=('Calibri', 50, 'bold')).pack(expand=True)

# Function to handle login process
def signin():
    username = user.get()
    password = code.get()

    db = get_db()
    user_record = db.find_one({"username": username})

    if user_record and user_record.get('password') == password:
        show_main_content()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

# Function to show signup frame
def show_signup_frame():
    for widget in root.winfo_children():
        widget.destroy()

    signup_frame = Frame(root, width=950, height=500, bg='#fff')
    signup_frame.pack(fill='both', expand=True)

    def signup():
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()

        if password == conform_password:
            db = get_db()
            if db.find_one({"username": username}):
                messagebox.showerror('Invalid', 'Username already exists')
            else:
                db.insert_one({"username": username, "password": password})
                messagebox.showinfo('Signup', 'Successfully signed up')
                show_login_frame()
        else:
            messagebox.showerror('Invalid', "Both Passwords should match")

    def on_enter(e, entry, placeholder):
        entry.delete(0, 'end')

    def on_leave(e, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)

    Label(signup_frame, image=img_signup, border=0, bg='white').place(x=5, y=90)

    frame = Frame(signup_frame, width=350, height=390, bg='#fff')
    frame.place(x=300, y=50)

    heading = Label(frame, text="Sign Up", fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    global user, code, conform_code  # Declare as global to be used in signup
    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
    user.bind("FocusOut", lambda e: on_leave(e, user, 'Username'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
    code.bind("FocusOut", lambda e: on_leave(e, code, 'Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    conform_code.place(x=30, y=220)
    conform_code.insert(0, 'Confirm Password')
    conform_code.bind("<FocusIn>", lambda e: on_enter(e, conform_code, 'Confirm Password'))
    conform_code.bind("FocusOut", lambda e: on_leave(e, conform_code, 'Confirm Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    Label(frame, text='I have an account!', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9)).place(x=90, y=340)
    Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_login_frame).place(x=200, y=340)

# Function to show login frame
def show_login_frame():
    for widget in root.winfo_children():
        widget.destroy()

    login_frame = Frame(root, width=950, height=500, bg='white')
    login_frame.pack(fill='both', expand=True)

    Label(login_frame, image=img_login, bg='white').place(x=50, y=50)

    frame = Frame(login_frame, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    global user, code  # Declare as global to be used in signin
    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=40, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', lambda e: on_enter(e, user, 'Username'))
    user.bind('<FocusOut>', lambda e: on_leave(e, user, 'Username'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=40, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', lambda e: on_enter(e, code, 'Password'))
    code.bind('<FocusOut>', lambda e: on_leave(e, code, 'Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
    Label(frame, text='Don’t have an account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)
    Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_signup_frame).place(x=215, y=270)

# Load images for login and signup
img_login = PhotoImage(file='D:\code\AutoMail-Collage-Project\images\login_img.png')
img_signup = PhotoImage(file='D:\code\AutoMail-Collage-Project\images\signup_img.png')

# Show the login frame initially
show_login_frame()

# Run the main loop of the Tkinter application
root.mainloop()
