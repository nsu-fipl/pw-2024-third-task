import potter

def test_empty_csv():
    potter.find_place('tests/csv/empty.csv')
    with open('where.csv') as f:
        lines = f.readlines()
        assert len(lines) == 1
        assert lines[0] == 'price,title\n'

def test_one_good_csv():
    potter.find_place('tests/csv/one_good.csv')
    with open('where.csv') as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0] == 'price,title\n'
        assert lines[1] == '4500.0,мыш\n'

def test_one_bad_csv():
    potter.find_place('tests/csv/one_bad.csv')
    with open('where.csv') as f:
        lines = f.readlines()
        assert len(lines) == 1
        assert lines[0] == 'price,title\n'


def test_one_good_one_bad_csv():
    potter.find_place('tests/csv/one_good_one_bad.csv')
    with open('where.csv') as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0] == 'price,title\n'
        assert lines[1] == '4500.0,мыш\n'

def test_one_bad_one_good_csv():
    potter.find_place('tests/csv/one_bad_one_good.csv')
    with open('where.csv') as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0] == 'price,title\n'
        assert lines[1] == '4500.0,мыш\n'

def test_empty_xml():
    verb = potter.find_method('tests/xml/empty.xml')
    assert not verb

def test_one_non_verb_xml():
    verb = potter.find_method('tests/xml/one_non_verb.xml')
    assert not verb

def test_one_verb_xml():
    verb = potter.find_method('tests/xml/one_verb.xml')
    assert verb == "опростоволоситься"

def test_two_verbs_first_is_frequent_xml():
    verb = potter.find_method("tests/xml/two_verbs_first_is_frequent.xml")
    assert verb == "опростоволоситься"

def test_two_verbs_second_is_frequent_xml():
    verb = potter.find_method("tests/xml/two_verbs_first_is_frequent.xml")
    assert verb == "опростоволоситься"

def test_empty_json():
    words = potter.find_item('tests/json/empty.json')
    assert not words

def test_no_suitable_lines_json():
    words = potter.find_item('tests/json/no_suitable_lines.json')
    assert not words

def test_one_word_json():
    words = potter.find_item('tests/json/one_word.json')
    assert words == ['halo']

def test_two_words_same_frequency_json():
    words = potter.find_item('tests/json/two_words_same_frequency.json')
    assert words == ['halo', 'welt']

def test_two_words_different_frequency_json():
    words = potter.find_item('tests/json/two_words_different_frequency.json')
    assert words == ['welt', 'halo']

if __name__ == '__main__':
    test_empty_csv()
    test_one_good_csv()
    test_one_bad_csv()
    test_one_good_one_bad_csv()
    test_one_bad_one_good_csv()
    test_empty_xml()
    test_one_verb_xml()
    test_one_non_verb_xml()
    test_two_verbs_first_is_frequent_xml()
    test_two_verbs_second_is_frequent_xml()
    test_empty_json()
    test_no_suitable_lines_json()
    test_one_word_json()
    test_two_words_same_frequency_json()
    test_two_words_different_frequency_json()