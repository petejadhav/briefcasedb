import os
import sys
import shutil
import engineConstants as ec
from database import Database
import json

class DBTable:
	def __init__(self,name,db_name):
		self.name = name
		# Check if databse exists
		self.database = Database(db_name)
		if(!self.database.getIfExists()):
			print("Error: Database "+ db_name +" not found")
			return False
		else:
			return True
	
	def createTable(self):
		# Create table directory
		if self.name in os.listdir(ec.DATADIR + os.sep + self.database.name):
			print("Table already exists")
			return False
		self.absTablePath = ec.DATADIR + os.sep + self.database.name + os.sep + self.name
		os.mkdir(self.absTablePath)
		return True

	# Define table's Schema loaded from JSON str
	# Json format -> {'columns':[{'name':'customer_name','datatype':'string','maxlength':50},{},...], 'config':[...]}
	#
	def createColumns(self,jsonStr):
		schemaDict = json.loads(jsonStr)
		columnsObj = schemaDict['columns']
		#miscCfgObj = schemaDict['config']
		cfgFile = open(self.absTablePath+os.sep+'config.bin','wb')
		# Validate Json	and create column bin files	
		for col in columnsObj:
			c = open(self.absTablePath+os.sep+col['name'],'wb')
			# calculate byte_multiplication_factor and write to config dict
			record_byte_length = ec.MAX_COLUMN_KEY_LENGTH + 1 + col['maxlength']
			columnsObj[col]['record_byte_length'] = record_byte_length
			c.close()
		# write first max_record_id, first 10 bytes reserved
		cfgfile.write('0000000000')
		# write schema to config file binary
		cfgFile.write(json.dumps(columnsObj))
		#cfgFile.write(json.dumps(miscCfgObj))
		cfgFile.close()		
