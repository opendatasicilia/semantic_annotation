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
PREFIX dbres: <http://dbpedia.org/resource/>
        
DESCRIBE dbres:{resource}
LIMIT 1 
    """.format(resource=resource)

    print(query)
    sparql = SPARQLWrapper("http://it.dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    print(results)



