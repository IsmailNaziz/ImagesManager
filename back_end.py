from PyQt5.QtCore import QThread, pyqtSignal
import time


class AppBackEnd(QThread):
	loading = pyqtSignal(int)

	def __init__(self):
		super(AppBackEnd, self).__init__()

	def run(self):
		for index in range(0, 101):
			self.loading.emit(index)
			time.sleep(0.1)

class Downloader(QThread):

	def __init__(self):
		super(Downloader, self).__init__()

	def download(self):
		return


