import os

class Database:
	def __init__(self,name):
		self.name = name
		
	def create(self):
		os.mkdir(name)
		db_config = open(name+"_cfg.bin",'w')
		
		db_config.close()
