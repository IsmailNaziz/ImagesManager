from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import back_end

import os


class AppFrontEnd(QMainWindow):
	def __init__(self):
		super(AppFrontEnd, self).__init__()
		uic.loadUi(os.path.join(os.path.split(__file__)[0], "app_front_end.ui"), self)
		self.app_backend_object = back_end.AppBackEnd()
		self.connect_widgets()
		self.show()

	def connect_widgets(self):
		self.download_images.clicked.connect(self.start_loading)
		self.app_backend_object.loading.connect(self.update_progress_bar)

	def update_progress_bar(self, value):
		self.app_progress_bar.setValue(value)

	def start_loading(self):
		self.app_backend_object.start()

class AppFrontEnd(QMainWindow):
	def __init__(self):
		super(AppFrontEnd, self).__init__()
		uic.loadUi(os.path.join(os.path.split(__file__)[0], "app_front_end.ui"), self)
		self.app_backend_object = back_end.AppBackEnd()
		self.connect_widgets()
		self.show()

	def connect_widgets(self):
		self.download_images.clicked.connect(self.start_loading)
		self.app_backend_object.loading.connect(self.update_progress_bar)

	def update_progress_bar(self, value):
		self.app_progress_bar.setValue(value)

	def start_loading(self):
		self.app_backend_object.start()

def run_app_frontend():
	front_app = QApplication([])
	app_frontend_object = AppFrontEnd()
	front_app.exec_()
