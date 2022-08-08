""" This module includes the main window and its main widgets """

from email import message
from PyQt5.QtWidgets import (
	QAction, QFrame, QHBoxLayout,
	QMainWindow, QMenuBar, QStatusBar,QVBoxLayout, QPushButton
	)

from GUI.windows_tab import TabWindow
from GUI.app_variables import WordVariables
from GUI.app_functions import openDecorator, absPath


class MainWindow(QMainWindow):
	""" 
	The constructor creates the window title, minimun size 1000x600, a menu bar called menu which have submenus  
	"""
	def __init__(self):
		super().__init__()

		#-------------------------- Variables instance --------------------------		
		words = WordVariables()

		#----------------------------- Window title -----------------------------
		self.setWindowTitle(words.title)

		#------------------------------ Window Size -----------------------------
		self.setMinimumSize(1000, 600)

		#------------------------------- Main frame -----------------------------
		self.frame_main = QFrame()

		#------ Vertical layout inside frame_main wich contains four frames -----
		# frame Bar will contain a windows bar
		# frame menu will contain a windows menu
		# central frame will contain forms
		# foot frame will contain status windows bar
		box_vertical_layout = QVBoxLayout()
		box_vertical_layout.setContentsMargins(0, 0, 0, 0)
		box_vertical_layout.setSpacing(0)

		#--- Horizontal layout inside central frame  wich contains three frames--
		# central left frame wich will contain a left bar
		# central mid frame wich will contain Qtabs
		# central right frame wich will contain right bar
		box_horizontal_layout = QHBoxLayout()
		box_horizontal_layout.setContentsMargins(0, 0, 0, 0)

		#--------------- Layout central wich contains a tab widget --------------
		central_vertical_layout = QVBoxLayout()
		central_vertical_layout.setContentsMargins(0, 3, 0, 0)

		# Horizontal layout wich contain a staus bar and more widgets
		foot_horizontal_layout = QHBoxLayout()

		#------------------- Frame will contains a widgets bar ------------------
		frame_bar = QFrame()
		frame_bar.setFixedHeight(40)

		#-------------------- Frame menu to put on a menu bar -------------------
		frame_menu = QFrame()
		frame_menu.setFixedHeight(30)

		# Central layout will contain a menu box_horizontal_layout
		central_frame = QFrame()

		#------------- Foot frame will contain a box_vertical_layout ------------
		foot_frame = QFrame()
		foot_frame.setFixedHeight(80)

		#---------------- Central left frame will contain widgtes ---------------
		central_left_frame = QFrame()
		central_left_frame.setFixedWidth(100)

		#---------------- Central mid frame will contain widgtes ----------------
		central_mid_frame = QFrame()

		#---------------- Central right frame will contain widgtes --------------
		central_right_frame = QFrame()
		central_right_frame.setFixedWidth(200)

		central_frame.setLayout(box_horizontal_layout)

		#---- Box horizontal layout to build a left, center and right widgets ---
		box_horizontal_layout.addWidget(central_left_frame)
		box_horizontal_layout.addWidget(central_mid_frame)
		box_horizontal_layout.addWidget(central_right_frame)

		#------ Vertical layout inside frame_main wich contains four frames -----
		box_vertical_layout.addWidget(frame_bar)
		box_vertical_layout.addWidget(frame_menu)
		box_vertical_layout.addWidget(central_frame)
		box_vertical_layout.addWidget(foot_frame)

		#----------------- Main frame contains a vertical layout ----------------
		self.frame_main.setLayout(box_vertical_layout)

		#-------------------------- TabWindow instance --------------------------
		tab = TabWindow()

		central_vertical_layout.addWidget(tab)
		central_mid_frame.setLayout(central_vertical_layout)

		#---------------------------- Menu bar Master ---------------------------
		menu = MenuBar(frame_menu)
		menu.openTab(menu.submenu_users, tab.open_user)
		menu.openTab(menu.submenu_customers, tab.open_customers)
		menu.openTab(menu.submenu_providers, tab.open_providers)
		menu.openTab(menu.subitem_products, tab.open_products)

		#-------------------------- Status windows bar --------------------------
		status_bar = StatusBar()
		self.setStatusBar(status_bar)
		# -----------------------------load QSS file ----------------------------
		self.loadQSS("qss/Aqua.qss")

		#---------------- Defines a frame main how central widget ---------------
		self.setCentralWidget(self.frame_main)
	
	def __str__(self) -> str:
		super().__str__()
		message_class = """ Create a class encharges of carry all widgtes """
		return message_class

	def loadQSS(self, file):
        #---------------------- Save the file absolute path ---------------------
		path = absPath(file)
        #------------------- Try to open and dump the content -------------------
		try:
			with open(path) as styles:
				self.setStyleSheet(styles.read())
		#------------- If there is a fail we capture with a exception------------
		except:
			print("Error abriendo estilos", path)

@openDecorator()
class MenuBar(QMenuBar):

	def __init__(self, parent: None):
		super().__init__(parent)

		words = WordVariables()

		self.setFixedHeight(30)

		#--------------- First element of the menu called Masters ---------------
		self.file_menu = self.addMenu(words.masters)
		self.file_menu.setFixedWidth(150)

		#-------------------- Submenu in Masters called Users -------------------
		self.submenu_users = self.file_menu.addAction(words.users)
		self.submenu_users.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.users
			)
		)

		#------------------ Submenu in Masters called Customers -----------------
		self.submenu_customers =  self.file_menu.addAction(words.customers)
		self.submenu_customers.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.customers
			)
		)

		self.submenu_providers = self.file_menu.addAction(words.providers)
		self.submenu_providers.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.providers
			)
		)
		#----------------------------- End Providers ----------------------------

		#------------------ Submenu in Masters called Products -----------------
		submenu_products = self.file_menu.addMenu(words.products)

		#------------------------ Sub-items into products -----------------------

		#----------------------------- Sub-item Food ----------------------------
		self.subitem_products = submenu_products.addAction(words.food)
		self.subitem_products.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.food
			)
		)
		self.subitem_products.setShortcut('Ctrl+F')

		#---------------------------- Sub-item Books ----------------------------

		self.subitem_books = submenu_products.addAction(words.books)
		self.subitem_books.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.books
			)
		)

		#--------------------------- Sub-item Clothes ---------------------------
		self.subitem_clothing = submenu_products.addAction(words.clothing)
		self.subitem_clothing.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.clothing
			)
		)

		#---------------------------- Sub-item Shoes ----------------------------
		self.subitem_shoes = submenu_products.addAction(words.shoes)
		self.subitem_shoes.setStatusTip('{}: {}'.format(
			words.message_tips,
			words.shoes
			)
		)

	""" def openTab(self, submenu, open_tab):
		#----------- Metod to open windows tab to create food products ----------
		self.submenu = submenu
		self.submenu.triggered.connect(open_tab) """

class StatusBar(QStatusBar):

	def __init__(self):
		super().__init__()

		self.setFixedHeight(20)





