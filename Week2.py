import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QGroupBox, QRadioButton, QComboBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)

        main_layout = QVBoxLayout()

        # Identitas Section
        identitas_group = QGroupBox("Identitas (vertical box layout)")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : Arnetha Nirwana Putri"))
        identitas_layout.addWidget(QLabel("NIM : F1D022113"))
        identitas_layout.addWidget(QLabel("Kelas : Pemrograman Visual_C"))
        identitas_group.setLayout(identitas_layout)
        main_layout.addWidget(identitas_group)

        # Navigation Section
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)

        # User Registration Section
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select", "Paris", "UK", "Swedia", "Indonesia", "Norwegia", "Germany"])
        
        form_layout.addRow("Full Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Phone:", self.phone_input)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country_combo)
        
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Actions Section
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())