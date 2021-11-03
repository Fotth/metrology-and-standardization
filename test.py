import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
#from PyQt5.QtCore import pyqtSignal, QObject
from grafiki import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import dastfun as df
from PyQt5.QtWidgets import QListWidgetItem,QMessageBox
from PyQt5.QtGui import QFont
import time
#from reader.__main__ import main


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clot=df.Hisoblash
        self.grafdata={}
        self.ui.pushButton.clicked.connect(self.agty)
        self.ui.pushButton_2.clicked.connect(self.dataclear)
        self.ui.pushButton_3.clicked.connect(self.grafiki)
        self.ui.commandLinkButton.clicked.connect(self.linkferuz)
        self.ui.listWidget.setFont(QFont('Times',16,weight=1))
        #
        # QListWidgetItem("salom ", self.ui.listWidget)
        # self.ui.listWidget.addItem(aitem=a)


    def linkferuz(self):
        msg = QMessageBox()
        msg.setWindowTitle("Bog'lanish uchun")
        msg.setText("Dastur muallifi : fottihsultan@gmail.com")
        x = msg.exec_()

    def grafiki(self):
        self.agty()
        xpoint=list()
        ypoint=list()
        for x , y in self.grafdata.values():
            xpoint.append(x)
            ypoint.append(y)
        font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
        font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

        plt.title("O'lchov qiymatlarini qayta ishlash Grafik shakili", fontdict=font1)
        plt.xlabel("    Kiritlgan qiymatlar  ", fontdict=font2)
        plt.ylabel("    Chiqayotgan qiymatlar ", fontdict=font2)

        plt.plot(xpoint,ypoint)
        plt.show()







    def agty(self):
        # QListWidgetItem("salom", self.ui.listWidget)
        fff=True
        a=list()
        try:
            a.append(float(self.ui.lineEdit.text()))
            a.append(float(self.ui.lineEdit_2.text()))
            a.append(float(self.ui.lineEdit_3.text()))
            a.append(float(self.ui.lineEdit_4.text()))
            a.append(float(self.ui.lineEdit_5.text()))
            a.append(float(self.ui.lineEdit_6.text()))
            a.append(float(self.ui.lineEdit_7.text()))
            a.append(float(self.ui.lineEdit_8.text()))
            a.append(float(self.ui.lineEdit_9.text()))
            a.append(float(self.ui.lineEdit_10.text()))
            a.append(float(self.ui.lineEdit_11.text()))
            a.append(float(self.ui.lineEdit_12.text()))
            a.append(float(self.ui.lineEdit_13.text()))
            a.append(float(self.ui.lineEdit_14.text()))
            a.append(float(self.ui.lineEdit_15.text()))
            a.append(float(self.ui.lineEdit_16.text()))
            a.append(float(self.ui.lineEdit_18.text()))
            a.append(float(self.ui.lineEdit_19.text()))
            a.append(float(self.ui.lineEdit_17.text()))
            a.append(float(self.ui.lineEdit_20.text()))
        except:
            QListWidgetItem('Xatolika yo\'li qo\'ydiz ',self.ui.listWidget)
            fff=False
        if fff:
            self.ui.listWidget.clear()
            hisob=df.Hisoblash(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19])
            time.sleep(1)
            massiv={}
            massiv=hisob.wow()
            guf=0
            datahisob=hisob.algo7()
            for i in massiv.values():  #manashu joyida xatolik bor  aloxida ozgaruvchi yaratib ishlab ko'r
                QListWidgetItem(i,self.ui.listWidget)
                self.grafdata[guf]=a[guf],datahisob[guf]
                guf+=1
                # d=f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                # QListWidgetItem(d, self.ui.listWidget)
                # time.sleep(0.1)
            #     print(i)
        else:
            QListWidgetItem("qaytib urunib koring ",self.ui.listWidget)




            # else:
            #     self.clot(self.a[i])
            #     if i == 19:
            #         mass = self.clot.wow().copy()
            #         for ma in mass:
            #             self.ui.listWidget.addItem(
            #                 f'{ma[0]} {ma[1]} {ma[2]} {ma[3]} {ma[4]} {ma[5]} {ma[6]} {ma[7]}'.format(ma[0], ma[1],
            #                                                                                           ma[2], ma[3],
            #                                                                                           ma[4], ma[5],
            #                                                                                           ma[6], ma[7]))

    def dataclear(self):
        self.ui.listWidget.clear()




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())