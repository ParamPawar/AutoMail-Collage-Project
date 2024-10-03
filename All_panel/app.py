from tkinter import *
from tkinter import messagebox, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES  # Import DND module
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        show_main_content()  # Transition to the main application
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

    frame = Frame(signup_frame, width=500, height=390, bg='#fff')
    frame.place(x=400, y=50)

    global user, code, conform_code
    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=130, y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", lambda e: on_enter(e, user, 'Username'))
    user.bind("<FocusOut>", lambda e: on_leave(e, user, 'Username'))

    Frame(frame, width=295, height=2, bg='black').place(x=130, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=130, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", lambda e: on_enter(e, code, 'Password'))
    code.bind("<FocusOut>", lambda e: on_leave(e, code, 'Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=130, y=177)

    conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    conform_code.place(x=130, y=220)
    conform_code.insert(0, 'Confirm Password')
    conform_code.bind("<FocusIn>", lambda e: on_enter(e, conform_code, 'Confirm Password'))
    conform_code.bind("<FocusOut>", lambda e: on_leave(e, conform_code, 'Confirm Password'))

    Frame(frame, width=295, height=2, bg='black').place(x=130, y=247)

    Button(frame,width=39,pady=5,text='Sign up',bg='#57a1f8', fg='white', border=0,command=signup).place(x=130,y=280)


    # Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=130, y=280)
    Label(frame, text='I have an account!', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9)).place(x=150, y=340)
    Button(frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=show_login_frame).place(x=250, y=340)

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

# Load Images for Login and Signup
img_login = PhotoImage(file='D:/code/AutoMail-Collage-Project/images/login_img.png')
img_signup = PhotoImage(file='D:/code/AutoMail-Collage-Project/images/signup_img.png')

# Main Application Panel
def show_main_content():
    for widget in root.winfo_children():
        widget.destroy()

    # Initialize the main panel with drag-and-drop functionality
    window = TkinterDnD.Tk()
    window.title("Main Application")
    window.geometry('925x500+300+200')
    window.configure(bg="#fff")
    window.resizable(False, False)

    # Callback function to handle dropped files
    def handle_drop(event):
        file_path = event.data
        if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
            messagebox.showinfo("File Accepted", f"Excel sheet '{file_path}' has been uploaded successfully.")
            global df  # Make the dataframe accessible globally
            df = pd.read_excel(file_path)
            columns = df.columns.tolist()
            name_selection['values'] = columns
            attendance_selection['values'] = columns
            email_selection['values'] = columns
            name_selection.set('')
            attendance_selection.set('')
            email_selection.set('')
        else:
            messagebox.showwarning("Invalid File", "Only Excel files (.xls, .xlsx) are allowed.")

    # This is the file panel that takes the Excel file
    box_frame = Frame(window, relief="solid", bd=1, bg="#fff", width=300, height=200)
    box_frame.grid(row=0, column=0, rowspan=2, padx=90, pady=30)
    box_label = Label(box_frame, text="Drag and Drop Excel Sheet Here", width=40, height=15, relief="solid", bg="#fff")
    box_label.pack()

    # Bind the drag and drop event to the box_frame
    box_frame.drop_target_register(DND_FILES)
    box_frame.dnd_bind('<<Drop>>', handle_drop)

    frame = Frame(window, bg='#fff')
    frame.place(x=480, y=50, width=350, height=390)

    # Labels and Comboboxes for column selection
    name_label = Label(frame, text="Select the name column:")
    name_label.pack(pady=(10, 0))
    name_selection = ttk.Combobox(frame, width=50)
    name_selection.pack(pady=(0, 10))

    attendance_label = Label(frame, text="Select the attendance column:")
    attendance_label.pack(pady=(10, 0))
    attendance_selection = ttk.Combobox(frame, width=50)
    attendance_selection.pack(pady=(0, 10))

    email_label = Label(frame, text="Select the email column:")
    email_label.pack(pady=(10, 0))
    email_selection = ttk.Combobox(frame, width=50)
    email_selection.pack(pady=(0, 10))

    # Text box for attendance criteria
    text_2_placeholder = "Enter the attendance criteria"
    text_2 = Text(frame, height=3, width=45, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    text_2.pack(pady=(10, 0))
    text_2.insert("1.0", text_2_placeholder)
    text_2.config(fg='gray')

    # Function to send email
    def send_email(to_email, subject, message_body):
        try:
            sender_email = ""  # Replace with your email
            sender_password = ""  # Replace with your App Password

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message_body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            server.quit()
            print(f"Email sent to {to_email}")

        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate. Check your email and password.")
        except smtplib.SMTPException as e:
            print(f"Error sending email to {to_email}: {e}")

    def process_selection():
        name_col = name_selection.get()
        attendance_col = attendance_selection.get()
        email_col = email_selection.get()
        attendance_criteria = text_2.get("1.0", END).strip()

        if name_col and attendance_col and email_col and attendance_criteria:
            try:
                attendance_criteria = float(attendance_criteria)
                students_below_criteria = df[df[attendance_col] < attendance_criteria]

                print("Students below criteria:")
                print(students_below_criteria)  

                if students_below_criteria.empty:
                    messagebox.showinfo("Information", "All students meet the attendance criteria.")
                else:
                    for _, row in students_below_criteria.iterrows():
                        student_name = row[name_col]
                        student_email = row[email_col]
                        email_body = f"Dear {student_name},\n\nYou are below the attendance criteria."
                        send_email(student_email, "Attendance Warning", email_body)
                    messagebox.showinfo("Success", f"Emails sent to {len(students_below_criteria)} students.")
            except ValueError:
                messagebox.showerror("Error", "Invalid attendance criteria. Please enter a valid number.")
        else:
            messagebox.showwarning("Warning", "Please select all three columns and provide attendance criteria.")

    # Button to submit the selection
    Button(frame, width=45, pady=10, text='Submit', bg='#57a1f8', fg='white', border=0, command=process_selection).pack(pady=(20, 0))

    # Text box for additional information or instructions
    text_frame_left = Frame(window, relief="solid", bd=1)
    text_frame_left.grid(row=2, column=0, padx=20, pady=20)

    text_box_left = Text(text_frame_left, height=10, width=50, font=('Microsoft Yahei UI Light', 8))
    text_box_left.pack()

    window.mainloop()

# Start the application with the login frame
show_login_frame()
root.mainloop()
