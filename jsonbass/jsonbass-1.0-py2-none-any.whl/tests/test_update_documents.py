from jsonbass.db import DB


TEXT = 'hello world'


def change_text(doc):
    doc['text'] = TEXT

    return doc


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

    updates = DB.iterate_documents(column, document_update=change_text)

    assert isinstance(updates, list)
    assert len(updates) > 0

    for note in DB.iterate_documents(column):
        assert note['text'] == TEXT
