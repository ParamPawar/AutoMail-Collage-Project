import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

## This is the main panel 
window = TkinterDnD.Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)

# Drag and drop label
drop_label = Label(window, text="Drag and drop your Excel file here", bg="#fff", fg="blue")
drop_label.pack(pady=20)

def on_drop(event):
    file_path = event.data
    if file_path.endswith('.xlsx'):
        try:
            # Load the Excel file
            df = pd.read_excel(file_path)
            messagebox.showinfo("Success", f"Loaded {len(df)} rows from {file_path}")
            # You can now use df for your operations
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")
    else:
        messagebox.showerror("Error", "Please drop a valid Excel file (.xlsx)")

drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', on_drop)

## Other parts of your GUI remain unchanged...

# Main loop
window.mainloop()
