import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


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
        self.show()
3p

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())

        
