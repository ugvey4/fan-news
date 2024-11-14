from tkinter import *
from tkinter import ttk
from fun import register
from dbFan import create_data_base

root = Tk()

def window():
    root.geometry('800x500')
    root.title('Fan News')
    root.attributes("-alpha", 0.90)
    root.configure(bg="#2f2f2f")

def label_start():
    label = ttk.Label(text= 'Fan news', font= ('Arial', 35), background= '#2f2f2f', foreground= 'white')
    under_label_text = ttk.Label(text= 'Добро пожаловать! Придумайте логин и пароль или введите уже существующий', font= ('Arial', 13), background= '#2f2f2f', foreground= 'white')

    label.pack(expand= True)
    label.place(x = 300, y = 50)

    under_label_text.pack(expand= True)
    under_label_text.place(x = 120, y = 140)

def button_click():
    button = Button(root, text="Log in", font=('Arial', 12), background="#2f2f2f", foreground='white',
                    command=lambda: validate_input(login_entry, password_entry))
    button.pack()
    button.place(x=380, y=350)

def validate_input(login_entry, password_entry):
    login = login_entry.get()
    password = password_entry.get()
    
    if len(login) < 6 or len(password) < 6:
        error_label = ttk.Label(text='Логин и пароль должны содержать не менее 6 символов.', 
                                 font=('Arial', 12), background="#2f2f2f", foreground='red')
        error_label.place(x=200, y=320)
        return error_label
    else:
        registr(root, login_entry, password_entry)

def enty_log():
    global login_entry, password_entry
    label_login = ttk.Label(text='Логин', font= ('Arial', 12), background= "#2f2f2f", foreground= 'white')
    label_login.place(x = 240, y = 230)

    label_password = ttk.Label(text='Пароль', font= ('Arial', 12), background= "#2f2f2f", foreground= 'white')
    label_password.place(x = 210, y = 280)

    login_entry = ttk.Entry(root, width=20, font=('Arial', 15))
    login_entry.pack()
    login_entry.place(x=300, y=230)

    password_entry = ttk.Entry(root, width= 20, font=('Arial', 15), show= '*')
    password_entry.pack()
    password_entry.place(x=300, y=280)


def main_ui():
     create_data_base()
     window()
     label_start()
     button_click()
     enty_log()
     root.mainloop()
