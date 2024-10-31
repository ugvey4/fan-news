import dbFan as db
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Listbox
from ui import *

def registr(root, login_entry, password_entry):
    global username
    username = login_entry.get()
    password = password_entry.get()
    if username and password:
        try:
            stored_password = db.check_password(username)
            if stored_password is not None:
                if password == stored_password:
                    messagebox.showinfo("Успех", "Вы вошли в свой аккаунт!")
                    app_run(root)
                else:
                    messagebox.showerror('Ошибка', 'Неверный пароль')
            else:
                if db.check_username(username):
                    messagebox.showerror('Ошибка', 'Пользователь с таким именем уже существует')
                else:
                    db.add_user(username, password)
                    messagebox.showinfo("Успех", "Регистрация прошла успешно!")
                    app_run(root)
        except Exception as e:
            messagebox.showerror('Ошибка', f'Ошибка регистрации{e}')
            print(e)
    else:
        messagebox.showwarning("Ошибка", "Заполните все поля!")

def app_run(root):
    for widget in root.winfo_children():
            widget.destroy()
            
    label = ttk.Label(text= 'Fan news', font= ('Arial', 35), background= '#2f2f2f', foreground= 'white')
    label.pack(expand= True)
    label.place(x = 300, y = 50)

    choice_sport(root)
    
def choice_sport(root):
    global leagues, selected_ligs

    button_choice = ttk.Button(root, text='Выбрать', command=lambda: choice_button(root))
    button_choice.place(x=320, y=360)
    
    button_skip = ttk.Button(root, text='Пропустить', command=lambda: menu_run(root))
    button_skip.place(x=410, y=360)

    leagues = {
        'АПЛ': ["Арсенал", "Челси", "Ливерпуль", "Манчестер Сити", "Манчестер Юнайтед"],
        'Ла лига': ["Барселона", "Реал Мадрид", "Атлетико Мадрид", "Севилья"],
        'Бундеслига': ["Бавария", "Боруссия Дортмунд", "Байер Леверкузен", "РБ Лейпциг"]}
    selected_ligs = StringVar()

    style = ttk.Style()
    style.configure('TRadiobutton', font=('Arial', 15), background='#2f2f2f', foreground= 'white')

    header = ttk.Label(text="Выберите любимую лигу", font=('Arial', 18), background='#2f2f2f', foreground='white')
    header.place(x=10, y=115)

    y_pos = 160
    for league in leagues:
        lig_btn = ttk.Radiobutton(root, text=league, variable=selected_ligs, value=league)
        lig_btn.place(x=10, y=y_pos)
        y_pos += 30

def choice_button(root):
    team_frame = ttk.Frame(root)
    team_frame.pack()

    league = selected_ligs.get()

    for widget in team_frame.winfo_children():
        widget.destroy()

    team_label = ttk.Label(team_frame, text="Команды {}".format(league))
    team_label.pack()

    team_listbox = Listbox(team_frame, font= ('Arial', 12),
     background= "#2f2f2f", foreground= 'white', width= 30)

    team_listbox.place(x = 350, y = 130)
    team_listbox.pack()

    for team in leagues[league]:
        team_listbox.insert(END, team)

    close_button = ttk.Button(team_frame, text="Закрыть", command=team_frame.destroy)
    close_button.pack(side=LEFT, padx=(5, 10), pady=10)

    select_button = ttk.Button(team_frame, text="Выбрать", command=lambda: select_team(root, team_listbox))
    select_button.pack(side=LEFT, padx=(5, 10), pady=10)

def select_team(root, team_listbox):
    selected_team = team_listbox.curselection()
    if selected_team:
        team_name = team_listbox.get(selected_team)
        db.add_teams(username, team_name)
        messagebox.showinfo("Выбор команды", f"Вы выбрали команду: {team_name}")
        menu_run(root)
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, выберите команду!")

def menu_run(root):
    for widget in root.winfo_children():
            widget.destroy()
    root.option_add("*tearOff", FALSE)
    main_menu = Menu(background='#2f2f2f', foreground= 'white', font= ('Arial', 10))
 
    file_menu = Menu(background='#2f2f2f', foreground= 'white', font= ('Arial', 10))
    file_menu.add_command(label="Профиль")
    file_menu.add_command(label="Команды")
    file_menu.add_separator()
    file_menu.add_command(label="Выйти")
    
    main_menu.add_cascade(label="Мой аккаунт", menu=file_menu)
    main_menu.add_cascade(label="Новости")
    main_menu.add_cascade(label="Турниры")
    
    root.config(menu=main_menu)

    import parsing
    parsing.main()
