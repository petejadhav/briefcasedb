# BriefCase DB
* fast read, slow write v2

## On-Disk Structure
* Every database is a folder on disk
* Database is a collection of tables
* Every table is a folder inside database folder
* Tables are collection of columns
* Every column is a file on disk
* Every column file is a mapping of 'row_id to value' of record for that column
* Every table will have defined no. of columns with exact definition of datatype
* Ex- table customers, has 3 columns- name->string(100), address->string(500), specialty->string(50)
* Here, even if a record has 'name' with say, 40 character length, the record will still allocate full 100 bytes.
* This will help in fast reads, since we can directly go to a certain part of the file without reading the full contents of file.
* Indexing will require an additional file, 'column'.index.
* THINK OF ENCODING - bin, compression, etc.

### On-Disk CRUD & Indexing
* Create Table - create directory with tablename in db folder, create 3 additional files -> name.bdb, address.bdb, specialty.bdb
* Create additional file -> config.bin (binary encoded config file) containing - 
	* schema details
	* byte multiplication factor for specific record access in column file 
	* max row_id or perhaps next row_id
* Create - get max row_id, calculate each column file_position using multiplication factor in config, write column value to file
* Read - Ex-> get address of customer whose name is 'asd' 
	* Iterate only through 'name' file and search for 'asd', get row_id for record (Possible Optimization - Indexing)
	* Calculate file position of record in 'address' file using row_id, read file content at position and return
	* If multiple filters, calculate intersection of row_ids from all column files where condition is true
* Update - Same as read, get row_id, then overwrite
* Delete - Calculate row_id, flag record/row_id in config.bin, next write will be at this flagged position (& then remove flag from cfg)

## In-Memory Structure
