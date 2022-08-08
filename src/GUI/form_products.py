from msilib.schema import ComboBox
from PyQt5.QtWidgets import (
	QComboBox,
	QCheckBox,
	QFrame,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QPlainTextEdit,
	QSpinBox,
)
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QCursor, QPixmap, QIcon

from GUI.app_variables import WordVariables
from GUI.templates import WidgetTemplate, ButtonTemplate


class FormGeneralFood(WidgetTemplate):
	"""
	Class Widget which contains a Form to create products. Only have widget for the general information.
	"""

	def __init__(self):
		""" Constructor where there is a layout, inside there is a Form which contain Labels and LineEdits. """
		super().__init__()

		#-------------------------- Variables instance --------------------------
		words = WordVariables()

		#--- Frae which contains horizontal layout for ComboBox and SpingBox --
		frame_combo_sping = QFrame()
		frame_combo_sping.setFixedWidth(180)

		#----- Horizontal layout (contain spingBox and combobox inside Form) ----
		boxh_combo_sping_layout = QHBoxLayout()

		#------------------------------- Form Label------------------------------
		lbl_id = QLabel(words.id)
		lbl_short_code = QLabel(words.short_code)		
		lbl_ean = QLabel(words.ean)		
		lbl_description = QLabel(words.description)
		lbl_presentation = QLabel(words.presentation)
		lbl_trademark = QLabel(words.trademark)
		lbl_observations = QLabel(words.observation)

		#---------------------------- Form Line Edits ---------------------------
		txt_id = QLineEdit()
		txt_id.setEnabled(False)
		txt_id.setFixedWidth(150)
		txt_id.setProperty("cssClass", "gray" )

		txt_short_code = QLineEdit()
		txt_short_code.setFixedWidth(150)

		txt_ean = QLineEdit()
		txt_ean.setFixedWidth(150)

		txt_description = QLineEdit()
		txt_description.setMaxLength(100)
		txt_description.setFixedWidth(350)

		txt_trademark = QLineEdit()
		txt_trademark.setFixedWidth(150)

		#------------------------------ Form SpinBox ----------------------------
		spbox_presentation = QSpinBox()
		spbox_presentation.setMaximum(10000)
		spbox_presentation.setFixedWidth(80)

		#----------------------------- Form ComboBox ----------------------------
		cmbbox_presentation = QComboBox()
		cmbbox_presentation.setFixedWidth(100)

		#-------------------------- Form Plain text box -------------------------
		txt_observations = QPlainTextEdit()
		txt_observations.setFixedSize(480,150)

		#--------------------------------- image --------------------------------
		image = QPixmap('./src/GUI/image/Discard.png')

		photo = QLabel()
		photo.setFixedSize(200,200)
		photo.setPixmap(image.scaled(200,200, Qt.KeepAspectRatio))

		#-------------------------- Button upload image -------------------------
		btn_upload = ButtonTemplate(words.btn_upload)

		#--------------- horizontal layout for SpingBox + ComboBox --------------
		boxh_combo_sping_layout.setContentsMargins(0,0,0,0)
		boxh_combo_sping_layout.setSpacing(0)
		boxh_combo_sping_layout.addStretch(1)

		#------- Adding Spingbox and ComboBox to the Horizontal layout --------
		boxh_combo_sping_layout.addWidget(spbox_presentation)
		boxh_combo_sping_layout.addWidget(cmbbox_presentation)

		#---- Adding Frame comboBox and spinbox to another Horizontal layout ---
		frame_combo_sping.setLayout(boxh_combo_sping_layout)

		#------------------------ Add elemens to the Form -----------------------
		self.left_form.addRow(lbl_id, txt_id)
		self.left_form.addRow(lbl_short_code, txt_short_code)
		self.left_form.addRow(lbl_ean, txt_ean)
		self.left_form.addRow(lbl_description, txt_description)
		self.left_form.addRow(lbl_presentation, frame_combo_sping)
		self.left_form.addRow(lbl_trademark, txt_trademark)

		#------------------- Add elements to one vertical layout ------------------
		self.boxv_one_layout.addLayout(self.left_form)
		self.boxv_one_layout.addWidget(lbl_observations)
		self.boxv_one_layout.addWidget(txt_observations)
		self.boxv_one_layout.addStretch(1)
		self.boxv_one_layout.setSpacing(10)

		#------------------- Add elements to two vertical layout ------------------
		self.boxv_two_layout.addWidget(photo)
		self.boxv_two_layout.addWidget(btn_upload)		
		self.boxv_two_layout.addStretch(1)
		self.boxv_two_layout.setSpacing(10)


class FormPurchaseFood(WidgetTemplate):
	"""
	Class Widget which contains a Form to create products. Only have widget for the purchase information.
	"""
	def __init__(self):
		""" Constructor where there are two layouts, inside each one there is a Form which contains widgets. """
		super().__init__()

		#-------------------------- Variables instance --------------------------
		words = WordVariables()

		#---------------------------- left Form Labels --------------------------
		lbl_supplier = QLabel(words.supplier)
		lbl_imported = QLabel(words.imported)
		lbl_category = QLabel(words.category)
		lbl_subcategory = QLabel(words.subcategory)

		#-------------------------- left Form CheckBox --------------------------
		chk_imported = QCheckBox()

		#------------------------- left Form Line Edit --------------------------
		txt_supplier = QLineEdit()
		txt_supplier.setFixedWidth(280)
		txt_supplier.setMaxLength(70)

		#-------------------------- left Form ComboBox --------------------------
		cmb_category = QComboBox()
		cmb_category.setFixedWidth(100)

		cmb_subcategory = QComboBox()
		cmb_subcategory.setFixedWidth(100)

		#------------------------- layout properties one-------------------------
		self.boxv_one_layout.setSpacing(40)
		self.boxv_one_layout.setContentsMargins(0,0,0,0)
		
		#------------------------- layout properties two ------------------------
		self.boxv_two_layout.setSpacing(40)
		self.boxv_two_layout.setContentsMargins(0,0,0,0)

		#---------------------- Add elemens to the left Form --------------------
		self.left_form.addRow(lbl_imported, chk_imported)
		self.left_form.addRow(lbl_supplier, txt_supplier)
		self.left_form.addRow(lbl_category, cmb_category)
		self.left_form.addRow(lbl_subcategory, cmb_subcategory)

		#--------------------------- right Form Labels --------------------------
		lbl_cost = QLabel(words.cost)
		lbl_iva = QLabel(words.iva)
		lbl_cost_iva = QLabel(words.cost_iva)
		lbl_cost_effectiveness = QLabel(words.cost_effectiveness)
		lbl_pvp = QLabel(words.pvp)

		#--------------------------- right Form Spinbox --------------------------
		spn_cost = QSpinBox()
		spn_cost.setFixedWidth(50)

		cmb_iva = QComboBox()
		cmb_iva.setFixedWidth(50)

		txt_cost_iva = QLineEdit()
		txt_cost_iva.setFixedWidth(50)
		txt_cost_iva.setEnabled(False)

		spn_cost_effectiveness = QSpinBox()
		spn_cost_effectiveness.setFixedWidth(50)

		spn_pvp = QSpinBox()
		spn_pvp.setFixedWidth(50)

		#---------------------- Add elemens to the right Form --------------------
		self.right_form.addRow(lbl_cost, spn_cost)
		self.right_form.addRow(lbl_iva, cmb_iva)
		self.right_form.addRow(lbl_cost_iva, txt_cost_iva)
		self.right_form.addRow(lbl_cost_effectiveness, spn_cost_effectiveness)
		self.right_form.addRow(lbl_pvp, spn_pvp)

		#------------------ Adding forms to one and two layouts -----------------
		self.boxv_one_layout.addLayout(self.left_form)
		self.boxv_two_layout.addLayout(self.right_form)


class FormLogisticFood(WidgetTemplate):
	"""
	Class Widget which contains a Form to create products. Only have widget for the logistic information.
	"""
	def __init__(self):
		""" Constructor where there is a layout, inside a Form which contains widgets. """
		super().__init__()

		#-------------------------- Variables instance --------------------------
		words = WordVariables()

		frame_width = QFrame()
		frame_width.setFixedWidth(180)
		frame_height = QFrame()
		frame_height.setFixedWidth(180)
		frame_large = QFrame()
		frame_large.setFixedWidth(180)
		frame_weight = QFrame()
		frame_weight.setFixedWidth(180)

		hbox_width_layout = QHBoxLayout()
		hbox_height_layout = QHBoxLayout()
		hbox_large_layout = QHBoxLayout()
		hbox_weight_layout = QHBoxLayout()

		lbl_width = QLabel(words.width )
		lbl_height = QLabel(words.height)
		lbl_large = QLabel(words.large)
		lbl_weight = QLabel(words.weight)

		spnb_width = QSpinBox()
		spnb_width.setMaximum(10000)
		spnb_height = QSpinBox()
		spnb_height.setMaximum(10000)
		spnb_large = QSpinBox()
		spnb_large.setMaximum(10000)
		spnb_weight = QSpinBox()
		spnb_weight.setMaximum(10000)

		cmbb_width = QComboBox()
		cmbb_height = QComboBox()
		cmbb_large = QComboBox()
		cmbb_weight = QComboBox()

		hbox_width_layout.addWidget(spnb_width)
		hbox_width_layout.addWidget(cmbb_width)

		hbox_height_layout.addWidget(spnb_height)
		hbox_height_layout.addWidget(cmbb_height)

		hbox_large_layout.addWidget(spnb_large)
		hbox_large_layout.addWidget(cmbb_large)

		hbox_weight_layout.addWidget(spnb_weight)
		hbox_weight_layout.addWidget(cmbb_weight)

		frame_width.setLayout(hbox_width_layout)
		frame_height.setLayout(hbox_height_layout)
		frame_large.setLayout(hbox_large_layout)
		frame_weight.setLayout(hbox_weight_layout)

		self.left_form.addRow(lbl_width, frame_width)
		self.left_form.addRow(lbl_height, frame_height)
		self.left_form.addRow(lbl_large, frame_large)
		self.left_form.addRow(lbl_weight, frame_weight)

		self.boxv_one_layout.addLayout(self.left_form)
