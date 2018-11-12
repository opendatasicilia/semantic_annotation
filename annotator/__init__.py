import os

import tagme

LANGUAGE = 'it'
# loading the tagme info needed for the annotation
tagme.GCUBE_TOKEN = os.environ['TAGME_TOKEN']
tagme.DEFAULT_LANG = LANGUAGE


def annotate_act(act):
    annotations = tagme.annotate(act, lang=LANGUAGE)
    for annotation in annotations.get_annotations():
        yield annotation.begin, annotation.end, annotation.entity_id, annotation.uri(lang=LANGUAGE)
