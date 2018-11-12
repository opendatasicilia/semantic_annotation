from SPARQLWrapper import SPARQLWrapper, JSON


def get_total_ddl():
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
    print(json_result)
    results = int(json_result['results']['bindings'][0]['callret-0']['value'])

    return results


def get_ddl_data(limit, offeset):
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
