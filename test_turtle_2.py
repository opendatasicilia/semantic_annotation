from rdflib.namespace import Namespace, XSD
from rdflib import Graph, Literal, BNode, RDF, URIRef

annotation_tuples = [
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 22, 51,
     "http://www.wikidata.org/entity/Q2707406", "ASSEMBLEA REGIONALE SICILIANA"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 146, 162,
     "http://www.wikidata.org/entity/Q686822", "DISEGNO DI LEGGE"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 217, 223,
     "http://www.wikidata.org/entity/Q112151", "Turano"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 376, 392,
     "http://www.wikidata.org/entity/Q686822", "DISEGNO DI LEGGE"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 496, 507,
     "http://www.wikidata.org/entity/Q11451", "agricoltura"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 509, 518,
     "http://www.wikidata.org/entity/Q8148", "industria"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 831, 841,
     "http://www.wikidata.org/entity/Q16530425", "Cancelleri"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 1225, 1241,
     "http://www.wikidata.org/entity/Q686822", "disegno di legge"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 1299, 1307,
     "http://www.wikidata.org/entity/Q3705013", "delibera"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 1589, 1607,
     "http://www.wikidata.org/entity/Q1460", "Regione  siciliana"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 1646, 1666,
     "http://www.wikidata.org/entity/Q32766", "Corte costituzionale"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 2156, 2186,
     "http://www.wikidata.org/entity/Q1221208", "contratto  a tempo determinato"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/385", 2539, 2556,
     "http://www.wikidata.org/entity/Q1460", "Regione siciliana"),
    ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 47, 84,
     "http://www.wikidata.org/entity/Q686822", """PROPOSTA
                         DI LEGGE"""),
     ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 204, 214,
      "http://www.wikidata.org/entity/Q37813", "ecosistemi"),
     ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 470, 480,
      "http://www.wikidata.org/entity/Q957076", "mondo  non"),
     ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 656, 659,
      "http://www.wikidata.org/entity/Q40970", "ciò"),
     ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 679, 691,
      "http://www.wikidata.org/entity/Q162719", "neoliberista"),
     ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 868, 878,
      "http://www.wikidata.org/entity/Q37813", "ecosistema"),
     ("http://dati.openars.org/legislatura/xvi/attivita-parlamentare/ddl/102", 881, 884,
      "http://www.wikidata.org/entity/Q40970", "Ciò"),

     ]

def urify(val):
    val=val.replace(" ", "_")
    return val

NIF = Namespace('http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#')
ITS = Namespace('http://www.w3.org/2005/11/its/rdf#')

g = Graph()
g.bind("nif", NIF)
g.bind("itsrdf", ITS)

res=URIRef("http://www.openars.org/test11")

for t in annotation_tuples:
    res=URIRef(t[0]+"#char="+str(t[1])+","+str(t[2]))
    g.add( (res, RDF.type , NIF.String) )
    g.add( (res, NIF.beginIndex ,  Literal(t[1], datatype=XSD.nonNegativeInteger)  ) )
    g.add( (res, NIF.endIndex , Literal(t[2], datatype=XSD.nonNegativeInteger) ) )
    g.add( (res, ITS.taldentRef , URIRef(t[3]) ) )
    g.add( (res, NIF.isString , Literal(t[4], lang='it') ) )

g.serialize(destination='./output.ttl', format='turtle')
