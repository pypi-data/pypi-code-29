import random

base_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notes_list = [x + y for y in  [str(i) for i in range(0, 9)] for x in base_notes]

pitch_offset = 24

def get_frequency(note):
    fixed_note = 'A4'
    fixed_note_frequency = 440

    fixed_note_index = notes_list.index(fixed_note)
    note_index = notes_list.index(note)

    half_step_distance = fixed_note_index - note_index
    a = 2**(1.0/12)

    frequency = fixed_note_frequency * (a ** half_step_distance)
 
    return frequency

def get_pitch(note):
    return notes_list.index(note) + pitch_offset


chords_diffs = {
    'major' : [0, 2, 4, 5, 7, 9, 11, 12],
    'minor' : [0, 2, 3, 5, 7, 8, 10, 12],
    'acoustic' : [0, 2, 4, 6, 7, 9, 10],
    'algerian' : [0, 2, 3, 6, 7, 8, 11, 12, 14, 15, 17],
    'altered' : [0, 1, 3, 4, 6, 8, 10],
    'augmented' : [0, 3, 4, 7, 8, 11],
    'bebop' : [0, 2, 4, 5, 7, 9, 10, 11],
    'blues' : [0, 3, 5, 6, 7, 10],
    'chromatic' : [0, 1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11],
    'double_harmonic' : [0, 1, 4, 5, 7, 8, 11],
    'enigmatic' : [0, 1, 5, 6, 8, 9, 11],
    'flamenco' : [0, 1, 4, 5, 7, 8, 11],
    'gypsy' : [0, 2, 3, 6, 7, 8, 10],
    'half_iminished' : [0, 2, 3, 5, 6, 8, 10],
    'harmonic_major' : [0, 2, 4, 5, 7, 8, 11],
    'harmonic_minor' : [0, 2, 3, 5, 7, 8, 11],
    'hijaroshi' : [0, 4, 6, 7, 11],
    'hungarian_minor' : [0, 2, 3, 6, 7, 8, 11],
    'insen' : [0, 1, 5, 7, 10],
    'iwato' : [0, 1, 5, 6, 10],
    'locrian' : [0, 1, 3, 5, 6, 8, 10],

    'percussion' : [0, 1, 2, 4, 5, 6, 8, 10],
}

def get_chord_notes(chord_root, chord_type):
    chord_root_index = notes_list.index(chord_root)
    chord_diffs = chords_diffs[chord_type]

    #If someone requests a chord really high up (like B8) we loop around the notes list. This should happen, realistically. 
    chord_notes = [notes_list[(chord_root_index + x) % len(notes_list)] for x in chord_diffs]

    return chord_notes

def get_base_notes_for_chord(chord_root, chord_type):
    chord_notes = get_chord_notes(chord_root, chord_type)
    chord_base_notes = [x[:-1] for x in chord_notes]
    return chord_base_notes

def chords_notes_difference(first_chord_notes, second_chord_notes):
    return len([x for x in second_chord_notes if x not in first_chord_notes])

def get_chords_base_notes(chord_choices):
    chords = [{'root' : note[:-1], 'type' : chord, 'notes' : get_base_notes_for_chord(note, chord)} for note in notes_list for chord in chord_choices]
    return chords

#The idea behind this is we take all chords from chord_choices and compare the number of notes that are different from the base chord. 
#Then, we reduce this list based on the lower_chord_diff_limit and upper_chord_diff_limit, and randomly choose a chord from it. 
def make_chord_progression(base_root, base_chord, number_of_chords, chord_choices, lower_chord_diff_limit = 0, upper_chord_diff_limit = 100):
    chords_base_notes = get_chords_base_notes(chord_choices)
    base_chord = [x for x in chords_base_notes if x['root'] == base_root and x['type'] == base_chord][0]

    #We calculate the differences between each chord and the base chord
    [chord.update({'chord_diff' : chords_notes_difference(base_chord['notes'], chord['notes'])}) for chord in chords_base_notes]

    chord_candidates = [x for x in chords_base_notes if lower_chord_diff_limit <= x['chord_diff'] < upper_chord_diff_limit]
    chords = [random.choice(chord_candidates) for i in range(number_of_chords)]

    chords = [(x['root'], x['type']) for x in chords]
    return chords

def get_note_from_offset(note_offset, chord_root, chord_type):
    chord_notes = get_chord_notes(chord_root, chord_type)
    note = chord_notes[note_offset]
    return note
