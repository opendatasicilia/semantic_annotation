# semantic_annotation
Arrichimento semantico degli Atti di OpenArs 
Attraverso l'utilizzo di [tagme](https://services.d4science.org/web/tagme) permette di linkare il contenuto testuale degli atti di OpenArs.org con tag semantici presenti in Wikidata.
Usa Airflow, docker, docker-compose e opzionalmente celery.

# Build:
``` bash
make local-build
```

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
make local-up
```


# Sviluppo:
``` bash
pip install -r requirements/dev.txt
```

# Todo:
- plug nicely airflow and testing;
- 
- Spike: Lista di UI interessanti che usano Wikidata (pubblicazione su DataNinja);

