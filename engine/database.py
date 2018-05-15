import os
import json
import sys
import shutil
import engineConstants as ec

class Database:
	def __init__(self,name):
		self.name = name
		
	# Create new database
	def create(self):
		os.mkdir(name)
		db_cfg_json = {}
		db_config = open(name+"_cfg.bin",'w')
		db_config.write(db_cfg_json)
		db_config.close()

	# Get table names in curr. database
	def getTables(self):
		return os.listdir('./.')

	# Populate class variables if db exists
	def getIfExists(self):
		if self.name in os.listdir(ec.DATADIR):
			# Populate class variables
			return True
		else:
			return False

	# Delete database
	def delete(self):
		# Remove any references from master config if any.
		shutil.rmtree(ec.DATADIR+'/'+self.name)
		return True
