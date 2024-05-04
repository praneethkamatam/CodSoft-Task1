import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title('TO-DO-LIST')
app.geometry('350x450')
app.config(bg='skyblue')
font2 = ("Arial", 18, 'bold')
font3 = ("Arial", 10, "bold")

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showerror("Error", "Enter a task")

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror("Error", "Choose a task to delete")

def save_tasks():
    with open('tasks.txt', 'w') as f:
        tasks = tasks_list.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

title_label = tk.Label(app, font=("Arial", 30, 'bold'), text="To-do-list", bg='skyblue', height=2)
title_label.place(x=70, y=10)

add_button = tk.Button(app, command=add_task, font=font2, text="Add Task", width=10, bg='yellow', fg='black', relief=tk.RAISED, borderwidth=2)
add_button.place(x=20, y=100)

remove_button = tk.Button(app, command=remove_task, font=font2, text="Remove Task", width=10, bg='red', fg='black', relief=tk.RAISED, borderwidth=2)
remove_button.place(x=210, y=100)

task_entry = tk.Entry(app, font=font2, width=20)
task_entry.place(x=20, y=160)

tasks_list = tk.Listbox(app, width=39, height=15, font=font3)
tasks_list.place(x=20, y=210)
load_tasks()
app.mainloop()
