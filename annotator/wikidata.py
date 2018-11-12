from SPARQLWrapper import SPARQLWrapper, JSON


def check_dbpedia_resource(wikipedia_uri_resource):
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