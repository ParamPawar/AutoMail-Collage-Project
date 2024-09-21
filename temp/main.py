from tkinter import *
from tkinter import messagebox
from db import get_db  # Assuming you have a database connection utility

# Initialize the main window
root = Tk()
root.title("Login & Sign Up")
root.geometry("950x500+300+200")
root.configure(background="#fff")
root.resizable(False, False)


# Authentication Functions
def signin():
    username = user.get()
    password = code.get()

    db = get_db()
    user_record = db.find_one({"username": username})

    if user_record and user_record.get('password') == password:
        show_main_content()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')


def signup():
    username = user.get()
    password = code.get()
    conform_password = conform_code.get()

    if password == conform_password:
        try:
            db = get_db()
            existing_user = db.find_one({"username": username})

            if existing_user:
                messagebox.showerror('Invalid', 'Username already exists')
            else:
                db.insert_one({"username": username, "password": password})
                messagebox.showinfo('Signup', 'Successfully signed up')
                show_login_frame()
        except Exception as e:
            messagebox.showerror('Error', str(e))
    else:
        messagebox.showerror('Invalid', "Passwords do not match")


def show_signup_frame():
    for widget in root.winfo_children():
        widget.destroy()

    signup_frame = Frame(root, width=950, height=500, bg='#fff')
    signup_frame.pack(fill='both', expand=True)

    def on_enter(e, entry, placeholder):
        entry.delete(0, 'end')

    def on_leave(e, entry, placeholder):
        if entry.get() == '':
            entry.insert(0, placeholder)

    Label(signup_frame, image=img_signup, border=0, bg='white').place(x=5, y=90)

    frame = Frame(signup_frame, width=350, height=390, bg='#fff')
    frame.place(x=300, y=50)

    global user, code, conform_code
    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
    user.bind("<FocusOut>", lambda e: on_leave(e, user, 'Username'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
    code.bind("<FocusOut>", lambda e: on_leave(e, code, 'Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    conform_code.place(x=30, y=220)
    conform_code.insert(0, 'Confirm Password')
    conform_code.bind("<FocusIn>", lambda e: on_enter(e, conform_code, 'Confirm Password'))
    conform_code.bind("<FocusOut>", lambda e: on_leave(e, conform_code, 'Confirm Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    Label(frame, text='I have an account!', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9)).place(x=90, y=340)
    Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_login_frame).place(x=200, y=340)


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

    global user, code
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

    Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
    Label(frame, text='Don’t have an account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)
    Button(frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_signup_frame).place(x=215, y=270)


def on_enter(e, entry, placeholder):
    entry.delete(0, 'end')


def on_leave(e, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)


# Main Content (Code 2) after Authentication
def show_main_content():
    for widget in root.winfo_children():
        widget.destroy()

    # The new panel layout (from second.py)
    box_frame = Frame(root, relief="solid", bd=1, bg="#fff")
    box_frame.grid(row=0, column=0, rowspan=2, padx=90, pady=30)

    box_label = Label(box_frame, text="Box / Label", width=40, height=15, relief="solid", bg="#fff")
    box_label.pack()

    frame = Frame(root, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    # Text frame for description (from second.py)
    text_frame_left = Frame(root, relief="solid", bd=1)
    text_frame_left.grid(row=2, column=0, padx=20, pady=20)

    text_box_left = Text(text_frame_left, height=10, width=50, font=('Microsoft Yahei UI Light', 8))
    text_box_left.pack()

    # Function to manage placeholders
    def add_placeholder(text_widget, placeholder):
        text_widget.insert("1.0", placeholder)
        text_widget.config(fg='gray')

    def clear_placeholder(event, text_widget, placeholder):
        if text_widget.get("1.0", END).strip() == placeholder:
            text_widget.delete("1.0", END)
            text_widget.config(fg='black')

    def restore_placeholder(event, text_widget, placeholder):
        if text_widget.get("1.0", END).strip() == "":
            add_placeholder(text_widget, placeholder)

    # Create text boxes with placeholders (copied from second.py)
    text_1_placeholder = "Enter your name"
    text_1 = Text(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    text_1.place(x=40, y=10)
    add_placeholder(text_1, text_1_placeholder)
    text_1.bind("<FocusIn>", lambda e: clear_placeholder(e, text_1, text_1_placeholder))
    text_1.bind("<FocusOut>", lambda e: restore_placeholder(e, text_1, text_1_placeholder))

    Frame(frame, width=295, height=2, bg='black', relief="solid", bd=1).place(x=35, y=40)

    # New surname text box
    text_2_placeholder = "Enter your surname"
    text_2 = Text(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    text_2.place(x=40, y=80)  # Adjusted y position for the new box
    add_placeholder(text_2, text_2_placeholder)
    text_2.bind("<FocusIn>", lambda e: clear_placeholder(e, text_2, text_2_placeholder))
    text_2.bind("<FocusOut>", lambda e: restore_placeholder(e, text_2, text_2_placeholder))

    Frame(frame, width=295, height=2, bg='black').place(x=35, y=107)

    text_3_placeholder = "Enter your email"
    text_3 = Text(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    text_3.place(x=40, y=150)
    add_placeholder(text_3, text_3_placeholder)
    text_3.bind("<FocusIn>", lambda e: clear_placeholder(e, text_3, text_3_placeholder))
    text_3.bind("<FocusOut>", lambda e: restore_placeholder(e, text_3, text_3_placeholder))

    Frame(frame, width=295, height=2, bg='black').place(x=35, y=177)

    text_4_placeholder = "Enter your message"
    text_4 = Text(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    text_4.place(x=40, y=220)
    add_placeholder(text_4, text_4_placeholder)
    text_4.bind("<FocusIn>", lambda e: clear_placeholder(e, text_4, text_4_placeholder))
    text_4.bind("<FocusOut>", lambda e: restore_placeholder(e, text_4, text_4_placeholder))

    Frame(frame, width=295, height=2, bg='black').place(x=35, y=250)

    # Buttons
    Button(frame, width=45, pady=10, text='Click me', bg='#57a1f8', fg='white', border=0).place(x=35, y=280)
    Button(frame, width=45, pady=10, text='Click me', bg='#57a1f8', fg='white', border=0).place(x=35, y=350)


# Load Images for Login and Signup
img_login = PhotoImage(file='D:\code\AutoMail-Collage-Project\images\login_img.png')
img_signup = PhotoImage(file='D:\code\AutoMail-Collage-Project\images\signup_img.png')

# Start with the login frame
show_login_frame()

root.mainloop()
