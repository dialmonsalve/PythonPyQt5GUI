from PyQt5.QtWidgets import (QTabWidget,)
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QCursor, QPixmap

from GUI.stacke_windows import UsersTab, CustomersTab, ProvidersTab,ProductsTab
from GUI.app_variables import WordVariables

""" Class that creates a QTabWidgets wich contains a form for users, customers, providers and products  
"""
class TabWindow(QTabWidget):
	def __init__(self, ):
		super().__init__()

		#-------------------------- Variables instance --------------------------
		self.words = WordVariables()

		#----------------------- Properties of QtabWidget -----------------------
		self.tabCloseRequested.connect(self.delete)
		self.setTabsClosable(True)
		self.setMovable(True)

	def open_user(self):

		#-------------------------- Users tabs instance -------------------------
		wid = UsersTab()

		# Add users tab to the QtabWidget
		self.addTab(wid, self.words.users)
		
		i = self.count() - 1
		self.setCurrentIndex(i)

	def open_customers(self):

		#------------------------ Customers tab instance ------------------------
		wid = CustomersTab()

		#------------------ Add customers tab to the QtabWidget -----------------
		self.addTab(wid, self.words.customers)

		i = self.count() - 1
		self.setCurrentIndex(i)

	def open_providers(self):

		#------------------------ Providers tab instance ------------------------
		wid = ProvidersTab()

		self.addTab(wid,self.words.providers)

		i = self.count() - 1
		self.setCurrentIndex(i)

		#------------------ Add providers tab to the QtabWidget -----------------

	def open_products(self):

		#------------------------- Products tab instance ------------------------
		wid = ProductsTab()

		#------------------ Add products tab to the QtabWidget ------------------
		self.addTab(wid, self.words.food)

		i = self.count() - 1
		self.setCurrentIndex(i)

	def delete(self, i):

		#------------------------------- Close tab ------------------------------
		self.removeTab(i)
