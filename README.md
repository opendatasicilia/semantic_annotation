# semantic_annotation
Arrichimento semantico degli Atti di OpenArs 
Attraverso l'utilizzo di [tagme](https://services.d4science.org/web/tagme) permette di linkare il contenuto testuale degli atti di OpenArs.org con tag semantici presenti in Wikidata.

# Installazione:
1. Creare un python virtual environment (python3)
2. Installare le dipendenze in requirements.txt

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

# Esecuzione:
``` bash
python annotator.py
```
