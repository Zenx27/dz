from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример программы на PyQt6")
        self.setGeometry(100, 100, 400, 200)


        self.label = QLabel("Нажмите на кнопку", self)
        self.label.setStyleSheet("font-size: 16px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton("Нажми меня", self)
        self.button.setStyleSheet("font-size: 14px;")
        self.button.clicked.connect(self.on_button_click)


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_click(self):
        self.label.setText("Кнопка нажата!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
