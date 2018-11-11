# semantic_annotation
Arrichimento semantico degli Atti di OpenArs 

# Configurazione
Creare un file .env con il seguente contenuto:

``` bash
# Token per le API di TAGME:
# https://tagme.d4science.org/tagme/
TAGME_TOKEN = '****'
```

# TODO:
- modulo query SPARQL
- finire l'interfaccia con TAGME
- generatore URI dbpedia
- salvataggio csv file, formato: uri_atto, start, end, dbpedia_uri