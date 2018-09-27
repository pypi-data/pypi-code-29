import subprocess
from midiutil.MidiFile import MIDIFile

def write_mid_file(mid, file_name = 'test.mid'):
    if not file_name.endswith('.mid'): 
        file_name += '.mid'
    with open(file_name, 'w+b') as f: 
        mid.writeFile(f)

def add_notes_to_midi(mid, notes):
    for note in notes:
        mid.addNote(note['track'], note['channel'], note['pitch'], note['start'], note['length'], note['volume'])

    return mid

def add_program_change(mid, block, program):
    s_data = block['structure_data']['timing_data']
    for starting_beat in s_data['starting_beats']: 
        mid.addProgramChange(block['block_data']['track'], block['block_data']['track'], starting_beat, program)
    return mid

def midi_to_wav(file_name, soundfont):
    if file_name.endswith('.mid'): 
        file_name = file_name[:-4]
    wav_name = file_name +'.wav'
    midi_name = file_name + '.mid'
    cmd = ['fluidsynth', '-F', wav_name, soundfont, midi_name]
    subprocess.call(cmd)

def handle_midi_changes(mid, block):
    b_data = block['block_data']
    lower_blocks = b_data.get('blocks')

    if lower_blocks: 
        for b in lower_blocks: 
            mid = handle_midi_changes(mid, b)

    block_instrument = b_data.get('instrument', {})
    block_program_number = block_instrument.get('program_number') or b_data.get('program_number')

    if b_data.get('track'):
        if block_program_number: 
            add_program_change(mid, block, block_program_number)
        if b_data.get('bpm'): 
            for starting_beat in block['structure_data']['timing_data']['starting_beats']:
                mid.addTempo(b_data['track'], starting_beat, b_data['bpm'])
    return mid
