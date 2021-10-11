from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

from .lexic import analizator
from .sintact import grammar


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        # config app
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(720, 480)
        Dialog.setMinimumSize(QtCore.QSize(720, 480))
        Dialog.setMaximumSize(QtCore.QSize(720, 480))
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/favicon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAccessibleName("")
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(False)
        # boton compilar
        self.button_compile = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.click_compile())
        self.button_compile.setEnabled(False)
        self.button_compile.setGeometry(QtCore.QRect(200, 380, 75, 23))
        self.button_compile.setObjectName("button_compile")
        # ventana de codigo
        self.text_code = QtWidgets.QTextEdit(Dialog)
        self.text_code.setEnabled(False)
        self.text_code.setGeometry(QtCore.QRect(10, 80, 241, 291))
        self.text_code.setObjectName("text_code")
        # tabla token lexema
        self.table_token = QtWidgets.QTableWidget(Dialog)
        self.table_token.setEnabled(False)
        self.table_token.setGeometry(QtCore.QRect(260, 50, 211, 321))
        self.table_token.setObjectName("table_token")
        self.table_token.setColumnCount(2)
        self.table_token.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_token.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_token.setHorizontalHeaderItem(1, item)
        # boton about
        self.button_about = QtWidgets.QPushButton(Dialog, clicked=lambda: webbrowser.open(
            'https://github.com/ohmono/analizador-lexico'))
        self.button_about.setGeometry(QtCore.QRect(10, 450, 91, 23))
        self.button_about.setObjectName("button_about")
        # boton limpiar ventana
        self.button_clear = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.click_clear())
        self.button_clear.setEnabled(False)
        self.button_clear.setGeometry(QtCore.QRect(640, 450, 75, 23))
        self.button_clear.setObjectName("button_clear")
        # boton adjuntar archivo
        self.button_upload = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.click_upload())
        self.button_upload.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.button_upload.setObjectName("button_upload")
        # boton escribir codigo
        self.button_write = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.click_draw())
        self.button_write.setGeometry(QtCore.QRect(120, 50, 91, 23))
        self.button_write.setObjectName("button_write")
        # ventana de resultados
        self.text_code_2 = QtWidgets.QTextEdit(Dialog)
        self.text_code_2.setEnabled(False)
        self.text_code_2.setGeometry(QtCore.QRect(480, 80, 231, 291))
        self.text_code_2.setObjectName("text_code_2")
        # texto resultado
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 60, 47, 13))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Analizador Léxico"))
        self.button_compile.setText(_translate("Dialog", "Compilar"))
        item = self.table_token.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Lexema"))
        item = self.table_token.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Token"))
        self.button_about.setText(_translate("Dialog", "Documentación"))
        self.button_clear.setText(_translate("Dialog", "Limpiar"))
        self.button_upload.setText(_translate("Dialog", "Adjuntar archivo"))
        self.button_write.setText(_translate("Dialog", "Escribir código"))

    def click_draw(self):
        self.text_code.setEnabled(True)
        self.button_upload.setEnabled(False)
        self.button_compile.setEnabled(True)
        self.button_write.setEnabled(False)

    def click_compile(self):
        self.text_code.setEnabled(False)
        self.table_token.setEnabled(True)
        self.button_clear.setEnabled(True)
        self.button_compile.setEnabled(False)
        self.table_token.insertRow(0)
        global sol
        txt = self.text_code.toPlainText()
        sol = analizator().token_list(txt.replace('\n', ' '))
        self.table_token.setRowCount(len(sol))
        for i in range(len(sol)):
            self.table_token.setItem(
                i, 0, QtWidgets.QTableWidgetItem(sol[i][1]))
            self.table_token.setItem(
                i, 1, QtWidgets.QTableWidgetItem(sol[i][0]))

    def click_clear(self):
        self.text_code.setText('')
        for _ in range(len(sol)):
            self.table_token.removeRow(0)
        self.table_token.setEnabled(False)
        self.button_upload.setEnabled(True)
        self.button_write.setEnabled(True)
        self.button_clear.setEnabled(False)

    def click_upload(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open file', '.\\', "Txt files (*.txt)")
        if fname[0] != '':
            txt = str(open(fname[0], 'r').read()).replace('\n', ' ')
            self.text_code.setText((txt))
            self.button_upload.setEnabled(False)
            self.button_write.setEnabled(False)
            self.button_compile.setEnabled(True)
            self.text_code.setEnabled(True)
