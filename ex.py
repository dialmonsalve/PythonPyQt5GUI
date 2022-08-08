import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
	def __init__(self, parent = None):
		super(Window, self).__init__(parent)

		bar = self.menuBar()
		file = bar.addMenu("File")
		file.addAction("show")
		file.addAction("add")
		file.addAction("remove")
		file.triggered[QAction].connect(self.processtrigger)
		self.setCentralWidget(QTextEdit())

		self.statusBar = QStatusBar()
		self.b = QPushButton("click here")
		self.setWindowTitle("QStatusBar Example")
		self.setStatusBar(self.statusBar)
		
	def processtrigger(self,q):
	
		if (q.text() == "show"):
			self.statusBar.showMessage(q.text()+" is clicked",2000 )
			
		if q.text() == "add":
			self.statusBar.addWidget(self.b)
				
		if q.text() == "remove":
			self.statusBar.removeWidget(self.b)
		self.statusBar.show()

def main():
	app = QApplication(sys.argv)

	w = Window()

	w.show()

	app.exec_()

if __name__ == '__main__':
    main()



def dos(num_uno, num_2):
	def function_uno(num_uno, num_2):
		return num_uno>0 and num_2 > 0

	if function_uno(num_uno, num_2):
		return num_uno/num_2

r = dos(2,5)
print(r)

# a(b) => c

def function_a(function_b):

	def function_c():
		result = function_b()
		return result

	return function_c

def my_custome_decorator(funct):

	def wapper(*args, **kwargs):
		result = funct(*args, **kwargs)
		return result

	return wapper



