import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор с историей")


        self.entry = tk.Entry(root, width=30, font=("Arial", 20))
        self.entry.pack(pady=10)

       
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.result_button = tk.Button(self.buttons_frame, text="=", command=self.calculate, width=10)
        self.result_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(self.buttons_frame, text="Очистить", command=self.clear_entry, width=10)
        self.clear_button.grid(row=0, column=1, padx=5)


        self.history_label = tk.Label(root, text="История вычислений:", font=("Arial", 12))
        self.history_label.pack(pady=5)

        self.history_list = tk.Listbox(root, width=50, height=10)
        self.history_list.pack(pady=10)

        self.clear_history_button = tk.Button(root, text="Очистить историю", command=self.clear_history)
        self.clear_history_button.pack(pady=5)

    def calculate(self):

        expression = self.entry.get()

        try:

            result = eval(expression)


            history_entry = f"{expression} = {result}"
            self.history_list.insert(tk.END, history_entry)


            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception:

            messagebox.showerror("Ошибка", "Некорректное выражение! Попробуйте снова.")

    def clear_entry(self):

        self.entry.delete(0, tk.END)

    def clear_history(self):

        self.history_list.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
