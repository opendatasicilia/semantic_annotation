from annotator import annotate_act
from annotator.openars import get_total_acts, get_acts_data, iterate_acts
from annotator.wikidata import check_dbpedia_resource


def test_annotate_act():
    file = open('prova.txt', 'r')
    text = file.read()

    for annotation in annotate_act(text):
        print(annotation)
        assert annotation


def test_check_dbpedia_resource_sunny():
    resource_uri = "https://it.wikipedia.org/wiki/Attributi_araldici_di_posizione"
    result = check_dbpedia_resource(resource_uri)
    assert result
    assert result == 'http://www.wikidata.org/entity/Q3053322'


def test_check_dbpedia_resource_rainy():
    # wrong URI:
    resource_uri = "https://en.wikipedia.org/wiki/Attributi_araldici_di_posizione"
    result = check_dbpedia_resource(resource_uri)
    assert not result


def test_iterate_acts():
	
	for act_id, act_text in iterate_acts():
		print(act_id)
		print(act_text)
		input()

test_iterate_acts()