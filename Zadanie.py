import sys
import requests
import json
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox, QLabel

API_URL = "https://jsonplaceholder.typicode.com"


class JSONPlaceholderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JSONPlaceholder Client")
        self.setGeometry(100, 100, 500, 400)


        layout = QVBoxLayout()


        self.label = QLabel("Выберите категорию запроса:")
        self.combo_box = QComboBox()
        self.combo_box.addItems(["posts", "comments", "users", "albums", "photos", "todos"])


        self.get_data_button = QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.fetch_data)


        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)


        self.save_button = QPushButton("Сохранить в файл")
        self.save_button.clicked.connect(self.save_data)


        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.get_data_button)
        layout.addWidget(self.text_area)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.data = ""

    def fetch_data(self):

        category = self.combo_box.currentText()
        response = requests.get(f"{API_URL}/{category}")

        if response.status_code == 200:
            self.data = response.json()
            formatted_data = json.dumps(self.data, indent=4, ensure_ascii=False)
            self.text_area.setText(formatted_data)
        else:
            self.text_area.setText(f"Ошибка запроса: {response.status_code}")

    def save_data(self):
        """ Сохранение данных в файл """
        if not self.data:
            self.text_area.setText("Нет данных для сохранения!")
            return

        folder_name = "json_data"
        os.makedirs(folder_name, exist_ok=True)

        category = self.combo_box.currentText()
        file_path = os.path.join(folder_name, f"{category}.json")

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

        self.text_area.setText(f"Данные сохранены в {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JSONPlaceholderApp()
    window.show()
    sys.exit(app.exec())
