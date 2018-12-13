import csv
import os

import tagme
from SPARQLWrapper import SPARQLWrapper, JSON


LANGUAGE = 'it'

# TagMe associates an attribute to each annotation,
# called ρ (rho), which estimates the "goodness" of the annotation with respect to the other entities of the input text.
# We stress here that ρ does not indicate the relevance of the entity in the input text,
# but is rather a confidence score assigned by TagMe to that annotation.
# You can use the ρ value to discard annotations that are below a given threshold.
# The threshold should be chosen in the interval [0,1].
# A reasonable threshold is between 0.1 and 0.3.
# https://services.d4science.org/web/tagme/tagme-help
MIN_RHO = 0.3

# loading the tagme info needed for the annotation
tagme.GCUBE_TOKEN = os.environ['TAGME_TOKEN']
tagme.DEFAULT_LANG = LANGUAGE


def annotate_act(act):
    print("Annotating act: {act_text}".format(act_text=act[:100]))
    annotations = tagme.annotate(act, lang=LANGUAGE)
    for annotation in annotations.get_annotations(min_rho=MIN_RHO):
        yield annotation.begin, annotation.end, annotation.entity_id, annotation.uri(lang=LANGUAGE), annotation.mention


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


def check_wikidata_resource(wikipedia_uri_resource):
    """
    Checks if exists an Entity in Wikidata with the passed wikipedia_uri_resource parameter, and returns the Wikidata URI.
    The query is performed by checking if exists a wikidata entity with binded with the Wikipedia entity uri passed.
    Calls the Wikidata endpoint.
    :param resource: str
    :return: boolean, the Wikidata URI if exists (str), None otherwise.
    """
    query = """SELECT ?item
WHERE
{{
  # look for articles (sitelinks) in Italian ("it")
  <{resource}> schema:about ?item . 
  <{resource}> schema:inLanguage "it" .
}}""".format(resource=wikipedia_uri_resource)

    print("checking wikidata resource: {resource}".format(resource=wikipedia_uri_resource))

    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    json_result = sparql.query().convert()

    bindings = json_result['results']['bindings']
    num_binds = len(bindings)

    if num_binds == 0:
        return None
    elif num_binds == 1:
        return bindings[0]['item']['value']
    else:  # l_binds > 1
        raise Exception('More than one element correspondS to the passed URI')


def generate_csv():
    # initializing the csv file
    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=["act_uri", "ann_begin", "ann_end", "wikidata_uri", "mention"])

        # for each act start, end, wikidata_uri
        for act_uri, act_text in iterate_acts():
            # for each annotation
            for beg, end, ent_id, ent_wikipedia_uri, mention in annotate_act(act_text):
                # if exists a wikidata entry
                ent_wikidata_uri = check_wikidata_resource(ent_wikipedia_uri)
                if ent_wikidata_uri is not None:
                    # adding an entry to the csv file
                    entry = dict(act_uri=act_uri, ann_begin=beg, ann_end=end, wikidata_uri=ent_wikidata_uri, mention=mention)
                    csv_writer.writerow(entry)
                    # print(entry)
                    csvfile.flush()
    print('*** End ***')

generate_csv()