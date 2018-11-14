# semantic_annotation
Arrichimento semantico degli Atti di OpenArs 

Permette di linkare il contenuto testuale degli atti di OpenArs.org con tag semantici presenti in dbpedia.

# Configurazione
Creare un file .env con il seguente contenuto:

``` bash
# Token per le API di TAGME:
# https://tagme.d4science.org/tagme/
export TAGME_TOKEN='****'
```

Caricarlo con: 
``` bash
source .env
``` 

# TODO:
- iterare per ogni atto, iterare per ogni annotazione, se esiste una entry su wikidata, aggiungere linea al file csv, formato: uri_atto, start, end, wikidata_uri
