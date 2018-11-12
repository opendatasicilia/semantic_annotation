from annotator import annotate_act, check_dbpedia_resource, get_total_ddl, get_ddl_data


def test_annotate_act():
    file = open('prova.txt', 'r')
    text = file.read()

    for annotation in annotate_act(text):
        print(annotation)


def test_check_dbpedia_resource():
    resource = "https://en.wikipedia.org/wiki/Attributi_araldici_di_posizione"
    print(check_dbpedia_resource(resource))

limit = 100
offset = 0
total = get_total_ddl()
last_chunk_index = int(total/limit)+1

for i in range (0,last_chunk_index):
	chunk = get_ddl_data(limit,offset)
	offset += limit
	
	# do something with chunk
	print ('chunk no: %d \n\n' % i)
	for ddl in chunk:
		id = ddl['ddl']['value']
		print ('id: %s \n' % id)
		
		title = ddl['titolo']['value']
		print ('title: %s \n' % title)
		
		text = ddl['text']['value']
		print ('text:\n\n\n%s' % text)
	
		exit()
	