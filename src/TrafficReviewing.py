import sys
import matplotlib.pyplot as plt
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QTableWidgetItem, QTableWidget
from PyQt6.QtWidgets import QInputDialog, QLineEdit
from Mapopener import Mapping
from Calculatoropener import MiniCalculator
from Tableopener import NewTabl


class Traffic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Traffic Review')
        self.setFixedSize(500, 500)

        self.lbl1 = QLabel(self)
        self.lbl1.setText('Добро пожаловать в программу "Обзор трафика". Здесь вы можете удобно визуализи-\n'
                          'ровать зависимости между временем суток и баллами пробок на дороге.')
        self.lbl1.resize(500, 30)
        self.lbl1.move(10, 10)

        self.lbl2 = QLabel(self)
        self.lbl2.resize(500, 20)
        self.lbl2.move(10, 110)
        self.lbl2.hide()

        self.lbl3 = QLabel(self)
        self.lbl3.resize(500, 20)
        self.lbl3.move(10, 140)
        self.lbl3.hide()

        self.lbl4 = QLabel(self)
        self.lbl4.resize(500, 20)
        self.lbl4.move(10, 180)
        self.lbl4.hide()

        self.lbl5 = QLabel(self)
        self.lbl5.resize(500, 20)
        self.lbl5.move(10, 210)
        self.lbl5.hide()

        self.btn1 = QPushButton('Выбрать таблицу', self)
        self.btn1.clicked.connect(self.choose)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(200, 100)

        self.addition = QPushButton('Добавить строку', self)
        self.addition.clicked.connect(self.adding)
        self.addition.resize(self.addition.sizeHint())
        self.addition.move(350, 130)
        self.addition.hide()

        self.num = QLineEdit(self)
        self.num.resize(20, 20)
        self.num.move(350, 210)
        self.num.hide()

        self.delett = QPushButton('Удалить строку', self)
        self.delett.clicked.connect(self.deleting)
        self.delett.resize(self.addition.sizeHint())
        self.delett.move(350, 160)
        self.delett.hide()

        self.variant1 = QPushButton('1 Визуализация', self)
        self.variant1.clicked.connect(self.var1)
        self.variant1.resize(self.variant1.sizeHint())
        self.variant1.move(10, 300)
        self.variant1.hide()

        self.variant2 = QPushButton('2 Визуализация', self)
        self.variant2.clicked.connect(self.var2)
        self.variant2.resize(self.variant2.sizeHint())
        self.variant2.move(10, 330)
        self.variant2.hide()

        self.variant3 = QPushButton('3 Визуализация', self)
        self.variant3.clicked.connect(self.var3)
        self.variant3.resize(self.variant3.sizeHint())
        self.variant3.move(10, 360)
        self.variant3.hide()

        self.sortt = QPushButton('Отсортированная таблица', self)
        self.sortt.clicked.connect(self.otsort)
        self.sortt.resize(self.sortt.sizeHint())
        self.sortt.move(15, 390)
        self.sortt.hide()

        self.opencalc = QPushButton('Открыть калькулятор', self)
        self.opencalc.clicked.connect(self.calcopenning)
        self.opencalc.resize(self.opencalc.sizeHint())
        self.opencalc.move(350, 100)

        self.btn2 = QPushButton('Сохранить изменения', self)
        self.btn2.clicked.connect(self.saving)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(300, 460)
        self.btn2.hide()

        self.btnmap = QPushButton('Открыть карту', self)
        self.btnmap.clicked.connect(self.openmap)
        self.btnmap.resize(self.btnmap.sizeHint())
        self.btnmap.move(250, 50)

    def choose(self):
        self.dialog = QFileDialog.getOpenFileName(self, 'Выбрать таблицу', '', 'Таблица (*.csv)')[0]
        try:
            with open(self.dialog, encoding='utf-8') as f:
                self.dialogsave = self.dialog
                self.t = list(csv.reader(f, delimiter=';', quotechar='"'))
            self.variant1.show()
            self.variant2.show()
            self.variant3.show()
            self.table()
        except Exception:
            self.dialog = self.dialogsave

    def var1(self):
        road, ok_pressed = QInputDialog.getItem(
            self, "Выберите дорогу", "Дорога?",
            set(i[0] for i in self.t[1:]), 0, False)
        if ok_pressed:
            x = list(set(i[1] for i in self.t[1:] if i[0] == road))
            x = sorted(x, key=lambda j: (int(j.split(':')[0]), int(j.split(':')[1])))
            x1 = [0] * len(x)
            y = [0] * len(x)
            for i in self.t[1:]:
                if i[1] in x and i[0] == road:
                    x1[x.index(i[1])] += 1
                    y[x.index(i[1])] += int(i[2])
            for i in range(len(y)):
                y[i] = round(y[i] // x1[i], 2)
            plt.figure(figsize=(10, 10))
            plt.bar(x, y, label='Баллы пробок')
            plt.title(f'Средний балл пробок на дороге: {road}')
            plt.xticks(rotation=90)
            plt.legend()
            plt.show()

    def var2(self):
        road, ok_pressed = QInputDialog.getItem(
            self, "Выберите дорогу", "Дорога?",
            set(i[0] for i in self.t[1:]), 0, False)
        if ok_pressed:
            x = list(set(i[1] for i in self.t[1:] if i[0] == road))
            x = sorted(x, key=lambda j: (int(j.split(':')[0]), int(j.split(':')[1])))
            x1 = [0] * len(x)
            y = [0] * len(x)
            for i in self.t[1:]:
                if i[1] in x and i[0] == road:
                    x1[x.index(i[1])] += 1
                    y[x.index(i[1])] += int(i[2])
            for i in range(len(y)):
                y[i] = round(y[i] // x1[i], 2)
            plt.figure(figsize=(10, 10))
            plt.plot(x, y, label='Баллы пробок', color='black', marker='o', markersize=7)
            plt.title(f'Средний балл пробок на дороге: {road}')
            plt.xticks(rotation=90)
            plt.legend()
            plt.show()

    def var3(self):
        st = list(set([i[0] for i in self.t[1:]]))
        lt = [0] * len(st)
        lt1 = [0] * len(st)
        for road in st:
            for i in self.t[1:]:
                if i[0] == road:
                    lt[st.index(road)] += int(i[2])
                    lt1[st.index(road)] += 1
        for i in range(len(lt)):
            lt[i] = round(lt[i] / lt1[i], 2)
        plt.figure(figsize=(10, 10))
        plt.bar(st, lt, width=0.5)
        plt.tick_params(labelsize=6, axis='x')
        plt.xticks(rotation=90)
        plt.title('Среднее значение занятости дороги')
        plt.show()

    def saving(self):
        with open(self.dialog, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(
                [self.tabl.horizontalHeaderItem(i).text()
                 for i in range(self.tabl.columnCount())])
            for i in range(1, self.tabl.rowCount()):
                row = []
                for j in range(self.tabl.columnCount()):
                    item = str(self.tabl.item(i, j).text())
                    if i > 0 and j == 1:
                        if item.isalpha() or ':' not in item:
                            item = '00:00'
                        if not item.split(':')[0].isdigit() or not item.split(':')[1].isdigit():
                            item = '00:00'
                        if int(item.split(':')[0]) >= 24:
                            item = '00:' + item.split(':')[1]
                        if int(item.split(':')[1]) >= 60:
                            item = item.split(':')[0] + ':00'
                    elif i > 0 and j == 2:
                        if not item.isdigit() or int(i) < 0:
                            item = '0'
                    if item is not None:
                        row.append(item)
                    else:
                        row.append('')
                writer.writerow(row)
        with open(self.dialog, encoding='utf-8') as f:
            self.dialogsave = self.dialog
            self.t = list(csv.reader(f, delimiter=';', quotechar='"'))
        self.table()

    def table(self):
        self.tabl = QTableWidget(self)
        self.tabl.setColumnCount(len(self.t[0]))
        self.tabl.setHorizontalHeaderLabels(self.t[0])
        self.tabl.setRowCount(0)
        for i, row in enumerate(self.t):
            self.tabl.setRowCount(
                self.tabl.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tabl.setItem(
                    i, j, QTableWidgetItem(elem))

        self.tabl.resize(200, 200)
        self.tabl.move(200, 250)
        self.tabl.show()
        self.btn2.show()
        self.sortt.show()
        self.delett.show()
        self.addition.show()
        self.num.show()

        self.lbl2.setText(f'Количество записей: {len(self.t[1:])}')
        self.lbl2.show()

        self.lbl3.setText(f'Количество уникальных дорог: {len(set([i[0] for i in self.t[1:]]))}')
        self.lbl3.show()

        self.lbl4.setText('Самое затруднённое движение: ' + " ".join(sorted([i for i in self.t[1:]],
                                                                            key=lambda x: -int(x[2]))[0]))
        self.lbl4.show()

        self.lbl5.setText(f'Есть времена без пробок у дорог: {"да" if 0 in [int(i[2]) for i in self.t[1:]] else "нет"}')
        self.lbl5.show()

    def adding(self):
        self.tabl.setRowCount(
            self.tabl.rowCount() + 1)
        for i in range(3):
            self.tabl.setItem(
                self.tabl.rowCount() - 1, i, QTableWidgetItem('Nothing'))

    def deleting(self):
        try:
            self.tabl.removeRow(int(self.num.text()) - 1)
        except Exception:
            pass

    def otsort(self):
        self.examp = NewTabl(self.t)
        self.examp.show()

    def calcopenning(self):
        self.calc = MiniCalculator()
        self.calc.show()

    def openmap(self):
        self.map = Mapping()
        self.map.show()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    ex = Traffic()
    ex.show()
    sys.exit(a.exec())
