import tagme
import config

def annotate_act(act):
    annotations = tagme.annotate(act, lang=tagme.DEFAULT_LANG)
    for annotation in annotations.get_annotations():
        yield annotation.begin, annotation.end, annotation.uri()

