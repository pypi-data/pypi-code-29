from fyrgo import utils

def test_load_from_string():
    teststr = ''.join(['config {\nlevel0 {\nkey1 value1\nkey2 value2\nlevel1 ',
                      '{\nkey11 value11\nlevel2 {\n}\n}\n}\nlevel0 ',
                       '{\nkey1 value1\nkey2 VALUE2\nlevel1 ',
                       '{\nkey11 value11\nlevel2 {\n}\n}\n}\n}'])
    utils.XmlTree(teststr, strmode=True)

def test_load_from_info_file():
    utils.XmlTree('tests/param_examples/config.info')

def test_load_from_par_file():
    utils.XmlTree('tests/param_examples/treated.par')

def test_browse_through_xmletree_structure():
    config = utils.parse_conf("tests/param_examples/config.info")

def test_find_planets():
    config = utils.parse_conf("tests/param_examples/config.info")
    planets = []
    for p in config.iter('Planet'):
        planets.append(p)
    assert(len(planets)==2)
