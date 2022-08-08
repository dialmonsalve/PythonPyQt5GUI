""" This is the module wich includes the main exec window """
# ###########################################################################
# 	Project: App for training												#
# 	Create by: Diego Alejandro Monsalve	E									# 
#	Start date: 29/04/2022													#
#	End date: 																#
# 	Copryght: 2022															#
# ###########################################################################

from GUI.main_window import MainWindow

import sys

from PyQt5.QtWidgets import QApplication


def main():
	app = QApplication(sys.argv)

	w = MainWindow()

	w.show()

	app.exec_()

if __name__ == '__main__':
    main()