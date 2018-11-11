import tagme
import config
text = "Ciao come stai, questa è l'assemblea regionale siciliana"

test_annotations = tagme.annotate(text)

entities = []
annotations_dict = []

cre_count = 0
for annotation in test_annotations.get_annotations():
    annotation_dic = vars(annotation)
    entity_dic = dict(
        id=annotation_dic.pop('entity_id'),
        title=annotation_dic.pop('entity_title')
    )
    print(entity_dic)