from dandelion import DataTXT
from config import tokens

currToken = 0

def dandelion(s1, s2, type):

	global currToken
	global tokens
	
	while True:
		
		try:
			datatxt = DataTXT(app_id = tokens[currToken], app_key = tokens[currToken])
						
			if type == 'sim':
				val = datatxt.sim(s1, s2, lang='it').similarity
				return val
			if type == 'nex':
				list = datatxt.nex(s1, lang='it').annotations
				return list
	
		except:
			currToken += 1
			if len(tokens) != currToken:
				if currToken == len(tokens)-1:
					print("!!!!! LAST token left! !!!!!")
			else:
				print("!!!!! NO tokens left! !!!!!")
				exit()

file = open('prova.txt', 'r') 
text = file.read()

output = []

for annotation in dandelion(text,0,'nex'):
	print(annotation.spot)
	print(annotation.start)
	print(annotation.end)
	print('http://it.dbpedia.org/resource/' + annotation.uri.split('wiki/')[1])
	print()