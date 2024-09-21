from tkinter import *
from tkinter import messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES  # Import DND module

## This is the main panel
window = TkinterDnD.Tk()  # drag and drop functionality
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)

# Callback function to handle dropped files
def handle_drop(event):
    file_path = event.data
    if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        messagebox.showinfo("File Accepted", f"Excel sheet '{file_path}' has been uploaded successfully.")
    else:
        messagebox.showwarning("Invalid File", "Only Excel files (.xls, .xlsx) are allowed.")

## this is the file panel that takes the excel file
box_frame = Frame(window, relief="solid", bd=1, bg="#fff", width=300, height=200)
box_frame.grid(row=0, column=0, rowspan=2, padx=90, pady=30)
box_label = Label(box_frame, text="Drag and Drop Excel Sheet Here", width=40, height=15, relief="solid", bg="#fff")
box_label.pack()

# bind the drag and drop event to the box_frame
box_frame.drop_target_register(DND_FILES)
box_frame.dnd_bind('<<Drop>>', handle_drop)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

## text frame for description
text_frame_left = Frame(window, relief="solid", bd=1)
text_frame_left.grid(row=2, column=0, padx=20, pady=20)

text_box_left = Text(text_frame_left, height=10, width=50, font=('Microsoft Yahei UI Light', 8))
text_box_left.pack()

# fun to manage placeholders
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

# text boxes with placeholders
text_1_placeholder = "Enter your name"
text_1 = Text(frame, width=45, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
text_1.place(x=40, y=10)
add_placeholder(text_1, text_1_placeholder)
text_1.bind("<FocusIn>", lambda e: clear_placeholder(e, text_1, text_1_placeholder))
text_1.bind("<FocusOut>", lambda e: restore_placeholder(e, text_1, text_1_placeholder))

Frame(frame, width=295, height=2, bg='black', relief="solid", bd=1).place(x=35, y=40)

# text box
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

# Button 1
Button(frame, width=45, pady=10, text='Click me', bg='#57a1f8', fg='white', border=0).place(x=35, y=280)

# Button 2
Button(frame, width=45, pady=10, text='Click me', bg='#57a1f8', fg='white', border=0).place(x=35, y=350)

window.mainloop()
