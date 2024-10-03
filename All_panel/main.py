from tkinter import *
from tkinter import messagebox, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES  # Import DND module
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# This is the main panel
window = TkinterDnD.Tk()  # Drag and drop functionality
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)

# Callback function to handle dropped files
def handle_drop(event):
    file_path = event.data
    if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        messagebox.showinfo("File Accepted", f"Excel sheet '{file_path}' has been uploaded successfully.")
        
        # Load the Excel file and populate the comboboxes
        global df  # Make the dataframe accessible globally
        df = pd.read_excel(file_path)
        columns = df.columns.tolist()
        
        name_selection['values'] = columns
        attendance_selection['values'] = columns
        email_selection['values'] = columns
        
        # Clear previous selections
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
text_2.pack(pady=(10, 0))  # Added padding
text_2.insert("1.0", text_2_placeholder)
text_2.config(fg='gray')

# Function to send email
def send_email(to_email, subject, message_body):
    try:
        # Email configuration
        sender_email = ""  # Use your email
        sender_password = ""  # Use your app code 

        # Create MIME message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# Function to process the selections and send emails
def process_selection():
    name_col = name_selection.get()
    attendance_col = attendance_selection.get()
    email_col = email_selection.get()
    attendance_criteria = text_2.get("1.0", END).strip()
    additional_info = text_box_left.get("1.0", END).strip()

    if name_col and attendance_col and email_col and attendance_criteria:
        try:
            attendance_criteria = float(attendance_criteria)
            students_below_criteria = df[df[attendance_col] < attendance_criteria]
            if students_below_criteria.empty:
                messagebox.showinfo("Information", "All students meet the attendance criteria.")
            else:
                for _, row in students_below_criteria.iterrows():
                    student_name = row[name_col]
                    student_email = row[email_col]
                    email_body = f"Dear {student_name},\n\n{additional_info}"
                    
                    send_email(student_email, "Attendance Warning", email_body)
                messagebox.showinfo("Success", f"Emails sent to {len(students_below_criteria)} students.")
        except ValueError:
            messagebox.showerror("Error", "Invalid attendance criteria. Please enter a valid number.")
    else:
        messagebox.showwarning("Warning", "Please select all three columns and provide attendance criteria.")

# Button to submit the selection
Button(frame, width=45, pady=10, text='Submit', bg='#57a1f8', fg='white', border=0, command=process_selection).pack(pady=(20, 0))

# Additional button for any other action
Button(frame, width=45, pady=10, text='Another Action', bg='#57a1f8', fg='white', border=0).pack(pady=(10, 20))

# Text box for additional information or instructions
text_frame_left = Frame(window, relief="solid", bd=1)
text_frame_left.grid(row=2, column=0, padx=20, pady=20)

text_box_left = Text(text_frame_left, height=10, width=50, font=('Microsoft Yahei UI Light', 8))
text_box_left.pack()

window.mainloop()
