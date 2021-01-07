import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Hello World"
        self.width=640
        self.height=480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0,0,self.width, self.height)

# Status bar
        status_bar = self.statusBar()
        status_bar.showMessage("Eirini")

# Menu bar
        self.build_menu()

        self.show()

    def build_menu(self):
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu("File")
        menu_bar.addMenu("Edit")
        menu_bar.addMenu("Help")

        exit_button = QAction(QIcon('exit24.png'), 'Quit', self)
        exit_button.setShortcut("Ctrl+Q")
        exit_button.setStatusTip("Exit application")
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())

        
