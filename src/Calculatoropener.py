from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt6.QtWidgets import QLineEdit


class MiniCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle('MiniCalculator')

        self.first_num = QLabel('Первое число:', self)
        self.second_num = QLabel('Второе число:', self)
        self.lbl3 = QLabel('Подсчитать целое выражение:', self)

        self.number_1 = QLineEdit(self)
        self.number_2 = QLineEdit(self)
        self.expression = QLineEdit(self)

        self.calculate_button = QPushButton('->', self)
        self.expression_button = QPushButton('=', self)

        self.lblsum = QLabel('Сумма:', self)
        self.lblsum.resize(self.lblsum.sizeHint())
        self.lblsum.move(200, 10)
        self.lblrazn = QLabel('Разность:', self)
        self.lblrazn.resize(self.lblrazn.sizeHint())
        self.lblrazn.move(200, 30)
        self.lblymn = QLabel('Произведение:', self)
        self.lblymn.resize(self.lblymn.sizeHint())
        self.lblymn.move(200, 50)
        self.lbldel = QLabel('Частное:', self)
        self.lbldel.resize(self.lbldel.sizeHint())
        self.lbldel.move(200, 70)

        self.result_sum = QLineEdit(self)
        self.result_sum.resize(50, 20)
        self.result_sum.move(300, 10)
        self.result_sub = QLineEdit(self)
        self.result_sub.resize(50, 20)
        self.result_sub.move(300, 30)
        self.result_mul = QLineEdit(self)
        self.result_mul.resize(50, 20)
        self.result_mul.move(300, 50)
        self.result_div = QLineEdit(self)
        self.result_div.resize(50, 20)
        self.result_div.move(300, 70)
        self.result_expression = QLineEdit(self)
        self.result_expression.resize(50, 20)
        self.result_expression.move(160, 150)

        self.first_num.resize(self.first_num.sizeHint())
        self.number_1.resize(50, 30)
        self.first_num.move(10, 10)
        self.number_1.move(10, 30)

        self.second_num.resize(self.second_num.sizeHint())
        self.number_2.resize(50, 30)
        self.second_num.move(10, 70)
        self.number_2.move(10, 90)

        self.lbl3.resize(self.lbl3.sizeHint())
        self.lbl3.move(10, 120)
        self.expression.resize(100, 20)
        self.expression.move(10, 150)

        self.calculate_button.resize(30, 20)
        self.calculate_button.move(150, 50)
        self.expression_button.resize(30, 20)
        self.expression_button.move(120, 150)

        self.calculate_button.clicked.connect(self.click)
        self.expression_button.clicked.connect(self.expression_making)

    def click(self):
        a = self.number_1.text()
        b = self.number_2.text()
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            self.result_sum.setText(str(a + b))
            self.result_sub.setText(str(a - b))
            self.result_mul.setText(str(a * b))
            if b != 0:
                self.result_div.setText(str(round(a / b, 3)))
            else:
                self.result_div.setText('Error')

    def expression_making(self):
        try:
            self.result_expression.setText(str(eval(self.expression.text())))
        except Exception:
            self.result_expression.setText('Error')
