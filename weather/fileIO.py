import json


#Open and read from JSON file 
def read_from_file(filename):
	with open(filename, "r") as read_file:
		datafile = json.load(read_file)
		return datafile

def write_to_file(filename):
	with open(filename, "w") as write_file:
		json.dump(data, write_file, indent=4)
