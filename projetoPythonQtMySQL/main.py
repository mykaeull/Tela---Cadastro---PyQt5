from PyQt5 import uic, QtWidgets
import pymysql
import time

try:
    connect = pymysql.connect(host="localhost",
                              user="root",
                              password="32142970",
                              database="cadastros_produtos")
    print("Conectando ao banco de dados...")
    time.sleep(2)
    print("Conetado ao banco de dados com sucesso!")
except:
    print("Não foi possível conectar com o banco de dados...")

def main_function():
    cod = main_window.lineEdit.text()
    descricao = main_window.lineEdit_2.text()
    preco = main_window.lineEdit_3.text()

    if main_window.radioButton.isChecked():
        cat = "informatica"
    elif main_window.radioButton_2.isChecked():
        cat = "alimentos"
    elif main_window.radioButton_3.isChecked():
        cat = "eletronicos"

    try:
        cursor = connect.cursor()
        cursor.execute("INSERT INTO produtos(codigo, descricao, preco, categoria) VALUES ('{}', '{}', '{}', '{}')".format(cod,
                                                                                                                          descricao,
                                                                                                                          preco,
                                                                                                                          cat))
        connect.commit()
        connect.close()
        print("Cadastro realizado com sucesso!")
    except:
        print("ERRO ao cadastrar...")
    main_window.lineEdit.setText("")
    main_window.lineEdit_2.setText("")
    main_window.lineEdit_3.setText("")

def trocaTela():
    main_window.hide()
    lista_window.show()

    cursor = connect.cursor()
    cursor.execute("SELECT * FROM produtos")
    lista_produtos = cursor.fetchall()

    lista_window.tableWidget.setRowCount(len(lista_produtos))
    lista_window.tableWidget.setColumnCount(5)

    for i in range(0, len(lista_produtos)):
        for j in range(0, 5):
            lista_window.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista_produtos[i][j])))

def voltarTela():
    lista_window.hide()
    main_window.show()

app = QtWidgets.QApplication([])
main_window = uic.loadUi("main_window.ui")
lista_window = uic.loadUi("lista_window.ui")
main_window.pushButton.clicked.connect(main_function)
main_window.pushButton_2.clicked.connect(trocaTela)
lista_window.pushButton.clicked.connect(voltarTela)

main_window.show()
app.exec()