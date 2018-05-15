import os
import sys
import shutil
import engineConstants as ec
from database import Database
import json

class DBTable:
	def __init__(self,name,db_name):
		self.name = name
		self.database = Database(db_name)
		if(!self.database.getIfExists()):
			print("Error: Database "+ db_name +" not found")
			return False
		self.absTablePath = ec.DATADIR + os.sep + self.database.name + os.sep + self.name
		os.mkdir(self.absTablePath)
		return True

	# Define table's Schema loaded from JSON str
	# Json format -> {'columns':[{'name':'customer_name','datatype':'string','maxlength':50},{},...], 'config':[...]}
	#
	def defineSchema(self,jsonStr):
		schemaDict = json.loads(jsonStr)
		columnsObj = schemaDict['columns']
		#miscCfgObj = schemaDict['config']
		cfgFile = open(self.absTablePath+os.sep+'config.bin','wb')
		# write schema to config file binary
		cfgFile.close()
		for col in columnsObj:
			c = open(self.absTablePath+os.sep+col['name'],'wb')
			# write headers
			c.close()
		