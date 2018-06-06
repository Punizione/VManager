import json

def loadJsonFile(path):
	with open(path, 'r', encoding='utf-8') as load_f:
		json_dict = json.load(load_f)
		return json_dict


