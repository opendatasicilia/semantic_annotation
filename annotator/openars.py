from SPARQLWrapper import SPARQLWrapper, JSON


def get_total_acts():
    query = """
		PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
		PREFIX ars: <http://www.openars.org/core#>
		PREFIX ars_16_ddl: <http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/>

		SELECT count(*)
		FROM <http://www.openars.org/9/>
		WHERE {
			   ?ddl a        ars:DisegnoDiLegge;   
								ars:testo ?text;
								ars:titolo ?titolo.
						
		   }
    """

    sparql = SPARQLWrapper("http://virtuosa.pa2.itd.cnr.it:8890/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    json_result = sparql.query().convert()
    results = int(json_result['results']['bindings'][0]['callret-0']['value'])

    return results


def get_acts_data(limit, offeset):
    query = """
		PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
		PREFIX ars: <http://www.openars.org/core#>
		PREFIX ars_16_ddl: <http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/>

		SELECT ?ddl ?titolo ?text
		FROM <http://www.openars.org/9/>
		WHERE {
			   ?ddl a        ars:DisegnoDiLegge;   
								ars:testo ?text;
								ars:titolo ?titolo.
						
		   }
		limit %d
		offset %d
    """ % (limit, offeset)

    sparql = SPARQLWrapper("http://virtuosa.pa2.itd.cnr.it:8890/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()['results']['bindings']

    return results

def iterate_acts():
    limit = 100
    offset = 0
    total = get_total_acts()
    last_chunk_index = int(total/limit)+1

    for i in range(0, last_chunk_index):
        chunk = get_acts_data(limit, offset)
        offset += limit

        for act in chunk:
            act_id = act['ddl']['value']
            act_text = act['text']['value']

            yield (act_id, act_text)
