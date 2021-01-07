import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

import stock_ingester_tradier as si

class StockGui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "Stock Tracker"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.ticker_symbol_entry = None
        self.ticker_list_widget = None
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #------------
        # Create ticker information area
        self.ticker_list_widget = QListWidget()
        self.ticker_list_widget.addItem("MSFT")
        graph_widget = QWidget()
        graph_widget.setMinimumSize(600, 400)
        ticker_info_layout = QHBoxLayout()
        ticker_info_layout.addWidget(self.ticker_list_widget)
        ticker_info_layout.addWidget(graph_widget)
        # -----------
        # Create add ticker area
        add_ticker_button = QPushButton("Add Ticker Symbol")
        add_ticker_button.pressed.connect(self.add_ticker)
        self.ticker_symbol_entry = QLineEdit()
        # add_ticker_frame = QFrame()
        # add_ticker_frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        add_ticker_layout = QHBoxLayout()
        add_ticker_layout.addWidget(add_ticker_button)
        add_ticker_layout.addWidget(self.ticker_symbol_entry)
        # -----------
        # Create the outer layout
        central_layout = QVBoxLayout()
        central_layout.addLayout(ticker_info_layout)
        central_layout.addLayout(add_ticker_layout)

        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def add_ticker(self):
        # Get text from text box and insert in ticker list
        new_ticker_text = self.ticker_symbol_entry.text()
        ingester = si.StockIngester()
        ticker_list = ingester.find_symbol(new_ticker_text)
        self.ticker_list_widget.addItem(new_ticker_text)
        print(f"Button Pressed: {new_ticker_text}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StockGui()
    sys.exit(app.exec_())
