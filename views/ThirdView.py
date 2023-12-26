"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QHBoxLayout, QWidget, QPushButton, QLabel

from core.Controllers.WindowController import WindowController


class ThirdView(QMainWindow, WindowController):

    item_signal = QtCore.pyqtSignal(str)

    items_list = []
    widgets = []

    def __init__(self):
        super().__init__()

        self.ui = self.load_ui()

        self.setWindowTitle(f"ThirdWindow")
        self.setFixedSize(1047, 834)

        self.input_obj = None

        self.show_content()

    def load_ui(self):
        from ui.ThirdWindow import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(self)

        return ui

    def show_content(self):
        """
        Bind the Ui that was loaded, define ViewComponents and load them individually
        :return:
        """

        ui = self.ui

        horizontal_layout = QHBoxLayout()
        create_button = QPushButton()
        clear_button = QPushButton()
        back_button = QPushButton()
        form_widget = QWidget()
        input_field = QLineEdit()

        self.input_obj = input_field

        create_button.clicked.connect(self.create_button)
        clear_button.clicked.connect(self.clear_button)
        back_button.clicked.connect(self.show_first)

        create_button.setText("Create item")
        clear_button.setText("Clear list")
        back_button.setText("First window")

        form_widget.setLayout(horizontal_layout)

        horizontal_layout.addWidget(input_field)
        horizontal_layout.addWidget(create_button)
        horizontal_layout.addWidget(clear_button)
        horizontal_layout.addWidget(back_button)

        form_widget.setStyleSheet("padding: 8px 6px;")

        ui.verticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Add the programmatically created elements to the existing layout in your UI file
        ui.verticalLayout.addWidget(form_widget)

        # Create a QWidget to hold the verticalLayout
        container_widget = QWidget()
        container_widget.setLayout(ui.verticalLayout)

        # Set the container_widget as the central widget of the main window
        self.setCentralWidget(container_widget)

    def create_button(self):
        input_text = self.input_obj.text()

        ui = self.ui

        horizontal_layout = QHBoxLayout()

        list_widget = QWidget()

        label = QLabel()
        label.setText(input_text)

        list_widget.setLayout(horizontal_layout)

        horizontal_layout.addWidget(label)

        self.widgets.append(list_widget)

        ui.verticalLayout.addWidget(list_widget)

        # Emit the signal with the created widget
        self.item_signal.emit(input_text)

        if WindowController.first_view_instance:
            WindowController.first_view_instance.handle_signal(input_text)

    def clear_button(self):
        ui = self.ui
        items = self.items_list

        if WindowController.first_view_instance:
            obj = WindowController.first_view_instance
            obj_ui = obj.ui
            obj_widgets = obj.widgets
            for widget in obj_widgets:
                obj_ui.verticalLayout.removeWidget(widget)
                widget.deleteLater()

            obj_widgets.clear()

        for widget in self.widgets:
            ui.verticalLayout.removeWidget(widget)
            widget.deleteLater()

        self.widgets.clear()
        items.clear()
