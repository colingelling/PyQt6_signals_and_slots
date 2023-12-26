"""

    Created by Colin Gelling on 30/01/2023
    Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QWidget

from core.Controllers.WindowController import WindowController


class SecondView(QMainWindow, WindowController):

    def __init__(self):
        super().__init__()

        self.ui = self.load_ui()

        self.setWindowTitle(f"SecondWindow")
        self.setFixedSize(1047, 834)

        self.show_content()

    def load_ui(self):
        from ui.SecondWindow import Ui_MainWindow
        ui = Ui_MainWindow()
        ui.setupUi(self)

        return ui

    def show_content(self):
        """
        Bind the Ui that was loaded, define ViewComponents and load them individually
        :return:
        """

        ui = self.ui

        main_layout = ui.verticalLayout
        widget_layout = QHBoxLayout()

        open_window_btn = QPushButton()

        second_window_btn = open_window_btn
        second_window_btn.setText("Open third window")
        second_window_btn.adjustSize()

        widget = QWidget()
        widget.setLayout(widget_layout)

        widget_layout.addWidget(second_window_btn)

        main_layout.addWidget(widget)

        # Create a QWidget to hold the verticalLayout
        container_widget = QWidget()
        container_widget.setLayout(main_layout)

        from PyQt6.QtCore import Qt
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Set the container_widget as the central widget of the main window
        self.setCentralWidget(container_widget)

        obj = WindowController()
        second_window_btn.clicked.connect(obj.show_third)
