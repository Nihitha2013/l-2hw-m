from tkinter import *
from datetime import date

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years")
    except:
        result_label.config(text="Please enter valid numbers")

root = Tk()
root.title("Age Calculator")
root.geometry("300x250")

Label(root, text="Birthday:").pack()
entry_day = Entry(root)
entry_day.pack()

Label(root, text="Birth month:").pack()
entry_month = Entry(root)
entry_month.pack()

Label(root, text="Birth year:").pack()
entry_year = Entry(root)
entry_year.pack()

Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
