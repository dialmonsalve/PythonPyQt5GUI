
from PyQt5.QtWidgets import (
	QFrame,
	QHBoxLayout,
	QPushButton,
	QStackedWidget,
	QTabWidget,
	QVBoxLayout,
	QWidget,
)

from GUI.form_products import FormGeneralFood, FormPurchaseFood, FormLogisticFood
from GUI.app_variables import WordVariables
from GUI.templates  import ButtonTemplate



class UsersTab(QWidget):
	def __init__(self):
		super().__init__()
		self.setAutoFillBackground(True)


class CustomersTab(QWidget):
	def __init__(self):
		super().__init__()
		self.setAutoFillBackground(True)

		#-------------------------- Variables instance --------------------------
		words = WordVariables()


class ProvidersTab(QWidget):
	def __init__(self):
		super().__init__()

		#self.setStyleSheet('background-color:yellow; margin:30')

""" Class where will insert a products form """
class ProductsTab(QFrame):
	
	def __init__(self):
		""" The Constructor creates a main widget that will contain a vertical layout. The vertical layout will have a horizontal layout and tabs wich inside will contain a Form General Products """
		super().__init__()

		#-------------------------- Variables instance --------------------------
		words = WordVariables()

		#------------------------------ Tab wigdget -----------------------------
		tab = QTabWidget()

		#---------------------------- Vertical layout ---------------------------
		boxv_layout = QVBoxLayout()
		boxv_layout.setContentsMargins(0,0,0,3)

		#--------------------------- Horizontal layout --------------------------
		boxh_layout = QHBoxLayout()

		#-------------------------------- Buttons -------------------------------
		btn_ok = ButtonTemplate(words.btn_ok)

		btn_cancel = ButtonTemplate(words.btn_cancel)

		#-------------------- General Products Form Instance --------------------
		general_food = FormGeneralFood()
		purcharse_food = FormPurchaseFood()
		logistic_food = FormLogisticFood()

		#------------------------------- Add tabs -------------------------------
		tab.addTab(general_food, words.general)
		tab.addTab(purcharse_food, words.Purcharse)
		tab.addTab(logistic_food, words.logistic)

		#----------------- Add buttons to the horizontal Layout -----------------
		boxh_layout.addStretch(1)
		boxh_layout.setSpacing(10)
		boxh_layout.addWidget(btn_ok)
		boxh_layout.addWidget(btn_cancel)
		boxh_layout.addSpacing(10)

		#------------------ Add elements to the vertical Layout -----------------
		boxv_layout.addWidget(tab)
		boxv_layout.addLayout(boxh_layout)

		#----------------- Add verical layout to the main widget ----------------
		self.setLayout(boxv_layout)



