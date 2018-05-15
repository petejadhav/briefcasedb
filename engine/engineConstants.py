import os

data_directory_name = 'data'

ENGINEDIR = os.path.dirname(os.path.abspath(__file__))
ROOTDIR = os.sep.join(ENGINEDIR.split(os.sep)[:-1])
DATADIR = ROOTDIR + os.sep + data_directory_name
