""" This module is a template create how QStackedWidget that will be the incharge of carry all widgets inside the forms """

from PyQt5.QtWidgets import (
	QFormLayout, QHBoxLayout, QLabel, QLayout, QPushButton,
	QSizePolicy,  QVBoxLayout ,QWidget,
	)
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class WidgetTemplate(QWidget):
	""" Class QStackedWidget with a wiget, QHBoxLayouts and QVBoxLayouts """

	def __init__(self, *args, **kwargs):
		""" Constructor that contains a widget, a horizontal layout and three vertical layout """
		super().__init__(*args, **kwargs)

		#-------------------------------- Layouts -------------------------------
		self.boxh_layout = QHBoxLayout()
		self.boxh_layout.setSizeConstraint(QLayout.SetMinimumSize)
		self.boxh_layout.setContentsMargins(100,50,100,100)
		
		self.boxv_one_layout = QVBoxLayout()
		#self.boxv_one_layout.setContentsMargins(30,30,0,0)

		self.boxv_two_layout = QVBoxLayout()
		#self.boxv_two_layout.setContentsMargins(0,30,30,0)

		self.boxv_three_layout = QVBoxLayout()
		self.left_form= QFormLayout()
		self.right_form = QFormLayout()

		#------------- Add vertical layouts to the horizontal layout ------------
		self.boxh_layout.addLayout(self.boxv_one_layout)
		self.boxh_layout.addLayout(self.boxv_two_layout)
		self.boxh_layout.addLayout(self.boxv_three_layout)

		#------------------ Add horizontal layout to the widget -----------------
		self.setLayout(self.boxh_layout)

		self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding,)

		#self.setObjectName("diego")
		#self.setProperty("cssClass", "large" )
		#self.setStyleSheet('background-color:yellow')


class ButtonTemplate(QPushButton):

	def __init__(self, title, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
		self.setFixedSize(150,30)
		self.setText(title)



