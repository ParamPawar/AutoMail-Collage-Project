from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)

#####################################--------------------------------------------------

box_frame = Frame(window, relief="solid", bd=1, bg="#fff")
box_frame.grid(row=0, column=0, rowspan=2, padx=90, pady=30)

box_label = Label(box_frame, text="Box / Label", width=40, height=15, relief="solid", bg="#fff")
box_label.pack()


frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

# heading = Label(frame,text="Sign Up", fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',23,'bold'))
# heading.place(x=100,y=5)

text_frame_left = Frame(window, relief="solid", bd=1)
text_frame_left.grid(row=2, column=0, padx=20, pady=20)

text_box_left = Text(text_frame_left, height=10, width=50,font=('Microsoft Yahei UI Light',8))
text_box_left.pack()

####################---------------------------------------------------------------------

text = Text(frame,width=45,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
text.place(x=40,y=80)

Frame(frame,width=295,height=2,bg='black',relief="solid", bd=1).place(x=35,y=107)

text_1 = Text(frame,width=45,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
text_1.place(x=40,y=150)

Frame(frame,width=295,height=2,bg='black').place(x=35,y=177)

text_2 = Text(frame,width=45,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
text_2.place(x=40,y=200)

Frame(frame,width=295,height=2,bg='black').place(x=35,y=247)



###############----------------------------------------------------------------------

Button(frame,width=45,pady=10,text='Click me',bg='#57a1f8', fg='white', border=0,).place(x=35,y=280)


Button(frame,width=45,pady=10,text='Click me',bg='#57a1f8', fg='white', border=0).place(x=35,y=350)




window.mainloop()
