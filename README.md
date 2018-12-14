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

# Enrichment:
L'enrichment usa il vocabolario definito in: 

Hellmann S., Lehmann J., Auer S., Brümmer M. (2013) Integrating NLP Using Linked Data. In: Alani H. et al. (eds) The Semantic Web – ISWC 2013. ISWC 2013. Lecture Notes in Computer Science, vol 8219. Springer, Berlin, Heidelberg

http://svn.aksw.org/papers/2013/ISWC_NIF/public.pdf

# Todo (next sprint //):
- Spike: Lista di UI interessanti che usano Wikidata (pubblicazione su DataNinja);
- approfondire la modalità per specificare la relazione tra la risorsa disegno di legge e il suo campo:
-  
