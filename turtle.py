from rdflib.namespace import Namespace

from rdflib import Graph, Literal, BNode, RDF

#### testing configuration: ######
act_text = """Disegno di Legge n 12.

"""
start = 11
end = 16
uri_wikidata = 'https://www.wikidata.org/wiki/Q686822'


###### end ######


NEE = Namespace('http://www.ics.forth.gr/isl/oae/core#')

store = Graph()

# Bind a few prefix, namespace pairs for pretty output
store.bind("NEE", NEE)

# Create an identifier to use as the subject for Donna.
act = BNode()

# Add triples using store's add method.
store.add((act, RDF.type, NEE.Entity))

    # todo: check the following fields, one by one:
# reference from: https://www.ics.forth.gr/isl/oae/specification/index.html

# Relates the annotation process to a configuration.
# store.add((act, NEE.usingConfiguration,

# Relates an entity to a literal representing the string in the document that was detected and considered an entity.
store.add((act, NEE.detectedAs, Literal(act_text[start:end])))

# Relates an entity to a literal representing the actual entity name that exists in a gazetteer of the NEE system.
# store.add((act, NEE.regardsEntityName, # using Wikidata italian label?

# Relates an entity to one or more literals representing the positions in the document in which the entity name was detected.
store.add((act, NEE.position, Literal(start)))

# Relates an entity to a literal (or a URI to a literal) representing the score of an entity (or of URI).
# store.add((act, NEE.score,

# Relates an entity to a literal representing the confidence of an ambiguous entity.
# store.add((act, NEE.confidence,

# Relates an entity to a category.
# store.add((act, NEE.belongsTo,

# Relates an entity to a URI.
           #todo: check if using a literal for a URI is right
store.add((act, NEE.hasMatchedURI, Literal(uri_wikidata)))

byte_output = store.serialize(format="turtle")

import sys
sys.stdout.buffer.write(byte_output)
