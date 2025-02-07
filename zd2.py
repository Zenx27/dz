import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список задач")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=50, height=15)
        self.task_list.pack(pady=10)

        self.delete_button = tk.Button(root, text="Удалить задачу", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task.strip():
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка", "Задача не может быть пустой!")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
