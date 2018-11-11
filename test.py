from annotator import annotate_act, check_dbpedia_resource


def test_annotate_act():
    file = open('prova.txt', 'r')
    text = file.read()

    for annotation in annotate_act(text):
        print(annotation)


def test_check_dbpedia_resource():
    resource = "https://en.wikipedia.org/wiki/Attributi_araldici_di_posizione"
    print(check_dbpedia_resource(resource))

test_check_dbpedia_resource()
