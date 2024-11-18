from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QColor


class NewTabl(QMainWindow):
    def __init__(self, a):
        super().__init__()
        self.setGeometry(600, 600, 500, 500)
        self.setWindowTitle('Table Review')

        t = 0
        for i in a[1:]:
            t += int(i[2])
        t //= len(a[1:])

        a1 = sorted(a[1:], key=lambda x: int(x[2]))

        self.tabll = QTableWidget(self)
        self.tabll.setColumnCount(len(a[0]))
        self.tabll.setHorizontalHeaderLabels(a[0])
        self.tabll.setRowCount(0)
        for i, row in enumerate(a1):
            self.tabll.setRowCount(
                self.tabll.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tabll.setItem(
                    i, j, QTableWidgetItem(elem))
            if int(row[2]) < t / 3:
                self.good_num(i)
            elif int(row[2]) > t * 2 / 3:
                self.bad_num(i)
            else:
                self.sredn_num(i)

        self.tabll.resize(500, 500)

    def bad_num(self, row):
        for i in range(self.tabll.columnCount()):
            self.tabll.item(row, i).setBackground(QColor(200, 0, 0))

    def sredn_num(self, row):
        for i in range(self.tabll.columnCount()):
            self.tabll.item(row, i).setBackground(QColor(100, 100, 0))

    def good_num(self, row):
        for i in range(self.tabll.columnCount()):
            self.tabll.item(row, i).setBackground(QColor(0, 200, 0))
