from annotator import annotate_act
from annotator.openars import get_total_ddl, get_ddl_data
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


def test_get_ddl_data():
    limit = 100
    offset = 0
    total = get_total_ddl()
    last_chunk_index = int(total/limit)+1

    for i in range(0, last_chunk_index):
        chunk = get_ddl_data(limit, offset)
        offset += limit

        # do something with chunk
        print('chunk no: %d \n\n' % i)
        for ddl in chunk:
            ddl_id = ddl['ddl']['value']
            print('id: %s \n' % ddl_id)

            title = ddl['titolo']['value']
            print('title: %s \n' % title)

            text = ddl['text']['value']
            print('text:\n\n\n%s' % text)

            exit()
