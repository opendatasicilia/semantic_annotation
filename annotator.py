import os

import tagme

tagme.GCUBE_TOKEN = os.environ['TAGME_TOKEN']
tagme.DEFAULT_LANG = 'it'


def annotate_act(act):
    annotations = tagme.annotate(act, lang=tagme.DEFAULT_LANG)
    for annotation in annotations.get_annotations():
        yield annotation.begin, annotation.end, annotation.uri()


from SPARQLWrapper import SPARQLWrapper, JSON
def check_dbpedia_resource(resource):
    query = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?label
        WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
    """

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        print(result["label"]["value"])

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
    results = int(sparql.query().convert()['results']['bindings'][0]['callret-0']['value'])
    
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