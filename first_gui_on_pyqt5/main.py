# pyuic5 hello.ui -o hello.py

import sys  # sys нужен для передачи argv в QApplication
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import hello

class HelloApp(QtWidgets.QMainWindow, hello.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам в файле hello.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации ранее созданного дизайна
        self.helloButton.clicked.connect(self.sayHello)
        self.browseButton.clicked.connect(self.browseFolder)
        self.listWidget.itemDoubleClicked.connect(self.handleDoubleClick)

    def sayHello(self):
        self.HelloHere.setText("HELLO - вот и результат")

    def browseFolder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы

        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):   # для каждого файла в директории
                self.listWidget.addItem(file_name)   # добавить файл в listWidget

    def handleDoubleClick(self, item):
            f = open(item.text(), 'r')
            with f:
                data = f.read()
                self.HelloHere.setText(data[0:10])


def main():
    app = QtWidgets.QApplication(sys.argv)   # Новый экземпляр QApplication
    window = HelloApp()                             # Создаём объект класса ExampleApp
    window.show()                                     # Показываем окно
    app.exec_()                                         # и запускаем приложение

if __name__ == '__main__':   # Если мы запускаем файл main.py
    main()                             # то выполняем функцию main()
