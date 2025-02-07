import sys
import requests
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel

class JsonPlaceholderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("JSONPlaceholder Client")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()

        self.label = QLabel("Введите ресурс (posts, users, comments):")
        self.layout.addWidget(self.label)

        self.input = QLineEdit("posts")
        self.layout.addWidget(self.input)

        self.btn_fetch = QPushButton("Запросить данные")
        self.btn_fetch.clicked.connect(self.fetch_data)
        self.layout.addWidget(self.btn_fetch)

        self.result = QTextEdit()
        self.layout.addWidget(self.result)

        self.btn_save = QPushButton("Сохранить данные")
        self.btn_save.clicked.connect(self.save_data)
        self.layout.addWidget(self.btn_save)

        self.setLayout(self.layout)

    def fetch_data(self):

        resource = self.input.text()
        url = f"https://jsonplaceholder.typicode.com/{resource}"
        response = requests.get(url)

        if response.status_code == 200:
            self.data = response.json()
            self.result.setText(json.dumps(self.data, indent=4, ensure_ascii=False))
        else:
            self.result.setText(f"Ошибка {response.status_code}")

    def save_data(self):
        """Сохранение данных в файл"""
        if hasattr(self, 'data'):
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
            self.result.append("\nДанные сохранены в data.json")
        else:
            self.result.append("\nНет данных для сохранения")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JsonPlaceholderApp()
    window.show()
    sys.exit(app.exec())  
