from jsonbass.db import DB


def test_write_documents():
    column = 'notes'

    DB.iterate_documents(column, delete=True)

    notes = [
        {
            'text': 'I should by milk today',
            'tags': ['milk', 'food', 'todo']
        },
        {
            'text': 'Go to the gym',
            'tags': ['fitness', 'health']
        },
        {
            'text': 'Call mother',
            'tags': ['health', 'social']
        }
    ]

    for _note in notes:
        note = DB.insert_document(column, _note)

        assert isinstance(note, dict)
        assert 'text' in note
        assert 'tags' in note
        assert 'id' in note

    assert len(list(DB.iterate_documents(column))) == 3

    social_notes = DB.iterate_documents(
        column,
        lambda x: 'social' in x['tags']
    )

    assert len(social_notes) == 1

    for note in social_notes:
        assert 'social' in note['tags']

    gym_notes = DB.iterate_documents(
        column,
        lambda x: 'gym' in x['text']
    )

    assert len(gym_notes) == 1

    no_notes = DB.iterate_documents(column, lambda x: x['text'] == 'peanuts')

    assert isinstance(no_notes, list)
    assert len(no_notes) == 0
