import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Initialize the user interface elements
        self.length_slider = QSlider(self)
        self.length_slider.setMaximum(30)
        self.length_slider.setMinimum(12)
        self.length_slider.setOrientation(1)  # Vertical slider
        self.length_slider.setTickPosition(QSlider.TicksBothSides)
        self.length_slider.setTickInterval(1)
        self.length_label = QLabel('Password Length: {}'.format(self.length_slider.value()))
        self.length_slider.valueChanged.connect(lambda value: self.length_label.setText('Password Length: {}'.format(self.length_slider.value())))

        self.uppercase_checkbox = QCheckBox('Uppercase Letters')
        self.uppercase_checkbox.setChecked(True)
        self.lowercase_checkbox = QCheckBox('Lowercase Letters')
        self.lowercase_checkbox.setChecked(True)
        self.digits_checkbox = QCheckBox('Digits')
        self.special_chars_checkbox = QCheckBox('Special Characters')

        self.generated_password_label = QLabel('Generated Password:')
        self.generated_password_display = QLabel(self)
        self.generated_password_display.setAlignment(Qt.AlignCenter)
        # Set the generated password to be bold
        font = QFont()
        font.setBold(True)
        font.setPixelSize(18)
        self.generated_password_display.setFont(font)

        generate_button = QPushButton('Generate Password', self)
        generate_button.clicked.connect(self.generate_password)

        # Create a horizontal layout for the label and the slider
        length_layout = QHBoxLayout()
        length_layout.addWidget(self.length_label)
        length_layout.addWidget(self.length_slider)

        # Create a vertical layout for the entire content
        layout = QVBoxLayout()
        layout.addLayout(length_layout)
        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.lowercase_checkbox)
        layout.addWidget(self.digits_checkbox)
        layout.addWidget(self.special_chars_checkbox)
        layout.addWidget(generate_button)
        layout.addWidget(self.generated_password_label)
        layout.addWidget(self.generated_password_display)

        self.setLayout(layout)

        self.setGeometry(300, 300, 400, 300)  # Set the window size
        self.setWindowTitle('Password Generator')

        self.show()

    def generate_password(self):
        # Get the user-selected options
        length = self.length_slider.value()
        uppercase = self.uppercase_checkbox.isChecked()
        lowercase = self.lowercase_checkbox.isChecked()
        digits = self.digits_checkbox.isChecked()
        special_chars = self.special_chars_checkbox.isChecked()

        characters = ""
        # Define character sets based on user options
        if uppercase:
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if lowercase:
            characters += "abcdefghijklmnopqrstuvwxyz"
        if digits:
            characters += "0123456789"
        if special_chars:
            characters += "!@#$%^&*()_-+=<>?/{}[]"

        if not characters:
            return

        # Generate the password
        generated_password = ''.join(random.choice(characters) for _ in range(length))

        # Set the generated password
        self.generated_password_display.setText(generated_password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    sys.exit(app.exec_())
