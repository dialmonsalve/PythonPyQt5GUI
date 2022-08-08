from pathlib import Path

""" Function to open QSS file path """
def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


""" Decorator to open forms """
def openDecorator():

	def superOpen(cls):

		class OpenTab(cls):

			def openTab(self, submenu, open_tab):

				self.submenu = submenu
				return self.submenu.triggered.connect(open_tab)

			def __str__(self) -> str:
				return  'Metod to open windows tab to create products'

		return OpenTab

	return superOpen