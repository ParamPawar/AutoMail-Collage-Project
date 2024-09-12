import pandas as pd
import json
from tkinter import Tk, filedialog

def select_excel_file():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx;.xls")])
    return file_path

def main():
   
    excel_file = select_excel_file()

    if excel_file:
       
        excel_data = pd.read_excel(excel_file)


        low_attendance_students = {} 
        total_students = len(excel_data)
        attendance_threshold = 0.75
        
        for index, row in excel_data.iterrows():
          
            if attendance < attendance_threshold: # type: ignore
                student_id = row['Student_ID'] 
                phone_number = row['Phone_Number_Column_Name']
                low_attendance_students[student_id] = phone_number

        # Convert the dictionary to a JSON object
        json_data = json.dumps(low_attendance_students, indent=4)

       
        if low_attendance_students:
            print("Phone numbers of students with less than 75% attendance:")
            for phone_number in low_attendance_students.values():
                print(phone_number)
           
            with open('low_attendance_students.json', 'w') as json_file:
                json_file.write(json_data)
            print("Low attendance students' phone numbers saved to 'low_attendance_students.json'.")
        else:
            print("All students have 75% or higher attendance.")
    else:
        print("No file selected.")

if _name_ == "_main_": # type: ignore
    main()