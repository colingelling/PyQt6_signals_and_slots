"""

    Created by Colin Gelling on 26/04/2023
    Using Pycharm Professional

"""


class WindowController:

    active_window = None

    first_view_instance = None
    third_view_instance = None

    """
    
        Methods support loading multiple windows between switches triggered by the user
        
    """

    @staticmethod
    def show_first():
        if WindowController.first_view_instance is None:
            from views.FirstView import FirstView
            WindowController.first_view_instance = FirstView()

        if WindowController.active_window:
            WindowController.active_window.hide()

        WindowController.first_view_instance.show()
        WindowController.active_window = WindowController.first_view_instance

    @staticmethod
    def show_second():
        from views.SecondView import SecondView

        if WindowController.active_window:
            WindowController.active_window.hide()

        window = SecondView()
        window.show()

        WindowController.active_window = window

    @staticmethod
    def show_third():
        if WindowController.third_view_instance is None:
            from views.ThirdView import ThirdView
            WindowController.third_view_instance = ThirdView()

        if WindowController.active_window:
            WindowController.active_window.hide()

        WindowController.third_view_instance.show()
        WindowController.active_window = WindowController.third_view_instance
