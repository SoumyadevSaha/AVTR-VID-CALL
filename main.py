from PyQt5.QtWidgets import QApplication
from gui.app_interface import AvatarApp

if __name__ == "__main__":
    app = QApplication([])
    window = AvatarApp()
    window.show()
    app.exec_()
