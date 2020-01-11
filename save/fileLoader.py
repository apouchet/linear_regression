import pandas as pd

class FileLoader():
	def load(self, path):
		try :
			panda_data = pd.read_csv(path)
		except Exception:
			print("can't load :", path)
			exit()
		print("Loading dataset of dimensions {} x {})".format(panda_data.shape[0], panda_data.shape[1]))
		return panda_data

	def display(self, panda_data, size):
		print(panda_data[:size])