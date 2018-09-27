import json
import os

instruments_path = os.path.dirname(os.path.realpath(__file__)) + '/instruments.json'

def get_all_instrument_data(instruments_file = ''):
    instruments_file = instruments_file or instruments_path

    with open(instruments_file) as f:
        instruments = json.load(f)
    return instruments

def get_instrument_data(instrument_name):
    instruments = get_all_instrument_data()
    instrument = [x for x in instruments if x['instrument_name'] == instrument_name]
    if not instrument: 
        raise Exception("Instrument " + str(instrument_name) + " not found in json. All instrument names are : " + str([x['instrument_name'] for x in instruments]))

    return instrument[0]

def get_list_of_instruments(instruments_file = ''):
    instruments = get_all_instrument_data(instruments_file)

    return [x['instrument_name'] for x in instruments]

def add_instrument_data_to_notes(notes, block_data):
    instrument = block_data.get('instrument')
    program_number = block_data.get('program_number')
    for note in notes:
        note['channel'] = block_data['track']
        note['track'] = block_data['track']
        if instrument: 
            note['program_number'] = instrument['program_number']
            note['volume'] = min(note['volume'] + instrument['volume'], 99)
        elif program_number: 
            note['program_number'] = program_number

    return notes
