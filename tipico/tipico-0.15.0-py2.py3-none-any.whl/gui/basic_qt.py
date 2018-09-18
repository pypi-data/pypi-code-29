import sys
import Qt
from Qt import QtWidgets
from Qt.QtWidgets import QWidget
from Qt.QtWidgets import QApplication, QLabel, QPushButton



class SimpleGui(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Simple')
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label= QLabel("Hello World.\nUsing Qt binding %s" %
                           Qt.Qt.__binding__)
        self.verticalLayout.addWidget(self.label)
        self.pushButton= QPushButton('Button', self)
        self.verticalLayout.addWidget(self.pushButton)



def main():
    app = QApplication(sys.argv)
    gui = SimpleGui()
    gui.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
