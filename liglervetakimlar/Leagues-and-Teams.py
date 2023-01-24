## liroza
import sys
from PyQt5.QtWidgets import *
from ui_liglerArayuz import *
from ui_hakkında import *

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

HakkindaUygulama = QApplication(sys.argv)
penHak = QMainWindow()
uiHak = Ui_hakkindaWindow()
uiHak.setupUi(penHak)

with open("hakkındaText.txt","a",encoding="utf-8") as file:
    pass

def ileriGit():
    aktifIndex=ui.tabWidget.currentIndex()
    if aktifIndex==5:
        aktifIndex=-1
    ui.tabWidget.setCurrentIndex(aktifIndex+1)


def geriGit():
    aktifIndex=ui.tabWidget.currentIndex()
    if aktifIndex==0:
        aktifIndex=6
    ui.tabWidget.setCurrentIndex(aktifIndex-1)


def sayfaDegistir(index):
    ui.tabWidget.setCurrentIndex(index)


def hakkında():
    try:
        with open("hakkındaText.txt","r",encoding="utf-8") as file:
            text=file.read()
        uiHak.hakkinda_textEdit.setText(text)
        penHak.show()
    except:
        with open("hakkındaText.txt","r") as file:
            pass


def kaydet():
    text=uiHak.hakkinda_textEdit.toPlainText()
    with open("hakkındaText.txt","w",encoding="utf-8")  as file:
        file.write(text)  


ui.TurkiyeButon.clicked.connect(lambda : sayfaDegistir(1))
ui.AlmanyaButon.clicked.connect(lambda : sayfaDegistir(2))
ui.ItalyaButon.clicked.connect(lambda : sayfaDegistir(3))
ui.IngiltereButon.clicked.connect(lambda : sayfaDegistir(4))
ui.IspanyaButon.clicked.connect(lambda : sayfaDegistir(5))

ui.HakkindaButon.clicked.connect(lambda : hakkında())
uiHak.KaydetButon.clicked.connect(lambda : kaydet())

ui.ileriButon.clicked.connect(lambda : ileriGit())
ui.geriButon.clicked.connect(lambda : geriGit())
ui.tabWidget.setCurrentIndex(0)
sys.exit(Uygulama.exec_())

## liroza
