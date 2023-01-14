from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QApplication

app = QApplication([])

dlg = QDialog()
lay = QVBoxLayout()
dlg.setLayout(lay)

label = QLabel("Hit izs")
