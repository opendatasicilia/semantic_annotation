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



