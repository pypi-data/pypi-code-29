from . import chord_handler, instrument_handler, note_generator, timing_organizer, midi_handler
from midiutil.MidiFile import MIDIFile


#The block_parser uses all the other modules in order to process a batch of blocks. Blocks hold the following sort of data: 

test_block = {
    "block_data" : {
        "bpm" : 120,
        "instrument" : "piano",
        "track" : 1,
        "blocks" : [{
                "block_data" : {
                    "bpm" : 140
                }, 
                "structure_data" : {
                    "notes_data" : {
                        "chord_root" : "C4",
                        "base_volume" : 30,
                    }, 
                    "timing_data" : {
                        "starting_beats" : [0]
                    }
                }
            }, {
                "block_data" : {
                }, 
                "structure_data" : {
                    "notes_data" : {
                        "chord_root" : "F3",
                    }, 
                    "timing_data" : {
                        "starting_beats" : [14]
                    }
                }
            }, {
                "block_data" : {
                }, 
                "structure_data" : {
                    }, 
                    "timing_data" : {
                        "starting_beats" : [28]
                    }
            }, {
                "block_data" : {
                }, 
                "structure_data" : {
                    }, 
                    "timing_data" : {
                        "starting_beats" : [42]
                }
            }

        ]
    },
    "structure_data" : {
        "notes_data" : {
            "chord_root" : "G3",
            "chord_type" : "major",
            "base_volume" : 30, 
        },
        "timing_data" : {
            "starting_beats" : [12], 
            "bar_length" : 13, 
            "number_of_bars" : 50,
            "accents" : {0 : 20, 2 : 10, 5 : 10, 7 : 20},
            "base_volume" : 50,
        },
    }
}

#TODO finish writing up what should be stored in this data. 


#Updates a child block with its parent's data if the child doesn't have that key populated. Allows certain keys to be excluded or accumulated (added up with the parent)
def update_child_from_parent(child, parent, excluded_keys = []):
    for key in parent: 
        if key not in child and key not in excluded_keys: 
            child[key] = parent[key]

    return child
   


def get_block_notes(block, parent_data = {}):

    #If this is a child block, we first update any data only present in its parents. 
    if parent_data: 
        block['block_data'] = update_child_from_parent(block['block_data'], parent_data['block_data'], excluded_keys = ['blocks', 'id'])
        block['structure_data']['notes_data'] = update_child_from_parent(block['structure_data'].get('notes_data', {}), parent_data['structure_data']['notes_data'])
        block['structure_data']['timing_data'] = update_child_from_parent(block['structure_data'].get('timing_data', {}), parent_data['structure_data']['timing_data'])

    #If this is a block containing other blocks, it doesn't generate notes by itself. 
    #Instead it just gets notes from its child blocks. 
    if block['block_data'].get('blocks'): 
        notes = []
        for child_block in block['block_data']['blocks']: 
            notes += get_block_notes(child_block, parent_data = block)
        return notes
   
    #Returns a list of dicts, depicting bars with data about where the bar starts, and data about each note, like so: [{"start" : 0, "notes" : []}, {"start" : 3, "notes" : []}]
    #Each note has a start, length and volume; start and length are based on the bar pattern, volume is based on the accents
    bars = timing_organizer.get_timings(base_volume = block['structure_data']['notes_data'].get('base_volume'), **block['structure_data']['timing_data'])

    #For each element of the timings, we put a note there. 
    #This should update the existing timings with values for the specific notes: {"start" : 0, "end" : 2, "volume" : 60, "value" : "A"}
    notes = note_generator.generate_notes(bars = bars, starting_beats = block['structure_data']['timing_data']['starting_beats'], **block['structure_data']['notes_data'])

    #Then we update the notes with the instruments, which may modify the volume (for instance, trumpet may be loud, so it should have a multiplier, like {"insturment" : "trumpet", "volume" : 0.5, "program_number" : 123}, not the actual program_number tho.
    notes = instrument_handler.add_instrument_data_to_notes(notes = notes, block_data = block['block_data'])
    #NOTE we don't actually need instrument data in the notes themselves - only when we need to change. So we handle this at the block level atm. 

    return notes


def make_block_music(block, soundfont, song_name):
    notes = get_block_notes(block)

    midi_file = MIDIFile(100)

    #We have a list of notes in dictionary form with all the data needed to convert them to midi. 
    midi_file = midi_handler.add_notes_to_midi(midi_file, notes)

    #We also have to add the program, bpm, etc. changes, if any. 
    midi_handler.handle_midi_changes(midi_file, block)

    midi_handler.write_mid_file(midi_file, song_name)

    #midi_file should just be a filename. We want to make it into a wav. 
    midi_handler.midi_to_wav(song_name, soundfont)
    
    #And done!
    return song_name 

#parse_block(test_block)
