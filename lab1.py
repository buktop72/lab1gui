from lab1ui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindo = QtWidgets.QMainWindow()
ui = Ui_MainWindo()
ui.setupUi(MainWindo)
MainWindo.show()

### my cod

def on_click():
    h_n = [int(i) for i in ui.lineEdit_2.text().split()]
    x_n = [int(i) for i in ui.lineEdit_3.text().split()]
    n = int(ui.lineEdit_4.text())
    y_n = calc(h_n, x_n, n)
    s = ""
    for i in y_n:
        s += " "
        s += str(i)
    ui.lineEdit_5.setText(s)
    graph(h_n, x_n, y_n)

ui.pushButton.clicked.connect(on_click)



"""
Задание: Для своего варианта вычислить реакцию ЛДС в виде 20 отсчетов при нулевых начальных условиях в
режиме калькулятора и с использованием программы. Построить графики импульсной характеристики, воздействия и реакции.
h(n) - Импульсная характеристика
x(n) - дискретный сигнал (воздействие)
y(n) - реакция
n - количество отсчетов
"""
import matplotlib.pyplot as plt
import pandas as pd


def calc(h_n, x_n, n):
    y_n = []
    # если длина h(n) и x(n) меньше n, до дополним нулями:
    if len(h_n) < n:
        for i in range(n - len(h_n)):
            h_n.append(0)
            x_n.append(0)

    # находим y(n):
    for i in range(n):
        for j in range(i + 1):
            ls1 = h_n[:j + 1]
            ls2 = x_n[:j + 1]
            ls2.reverse()
            y = 0
            for h, x in zip(ls1, ls2):
                y += h * x
        y_n.append(y)

    print('Реакция системы: ')
    print(y_n)
    return y_n

# # Построение графиков:
def graph(h_n, x_n, y_n):
    data = {'импульсная характеристика h(n)': h_n}
    df = pd.DataFrame(data)
    df.plot(kind='bar', color='g')
    plt.grid()
    plt.show()

    data = {'дискретный сигнал x(n)': x_n}
    df = pd.DataFrame(data)
    df.plot(kind='bar', color='b')
    plt.grid()
    plt.show()

    data = {'реакция y(n)': y_n}
    df = pd.DataFrame(data)
    df.plot(kind='bar', color='r')
    plt.grid()
    plt.show()

sys.exit(app.exec_())
