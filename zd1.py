import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Таймер")

        self.time_elapsed = 0
        self.running = False

        self.label = tk.Label(root, text="00:00", font=("Arial", 40))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Старт", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = tk.Button(root, text="Пауза", command=self.pause_timer)
        self.pause_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Сброс", command=self.reset_timer)
        self.reset_button.pack(side="left", padx=10)

    def update_timer(self):
        if self.running:
            self.time_elapsed += 1
            minutes = self.time_elapsed // 60
            seconds = self.time_elapsed % 60
            self.label.config(text=f"{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

