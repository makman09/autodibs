import json

'''
	@return {array} - list of all the times with 3 hours between that the rooms are available at
'''
def time_table(time_list_length):

	return []

def barcodes():
	with open('barcodes.json') as data_file:
		data = json.load(data_file)

		return data
