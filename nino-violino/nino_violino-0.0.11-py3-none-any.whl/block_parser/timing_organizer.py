import random, copy

#This is kinda a dummy function, which atm only randomly makes a pattern.
#TODO I probably want to do this with some sort of AI. Maybe some neurons or something. 
def make_bar_pattern(number_of_notes, max_note_len):
    pattern = []
    while number_of_notes > 0:

        next_val = min(random.randint(1, number_of_notes), max_note_len)
#        next_dur = random.randint(1, next_val * 2)  #TODO find a better way to find durations that don't sound creepy
        next_dur = 1

        pattern.append((next_val, next_dur))
        number_of_notes -= next_val

    return pattern



#pattern is a list of tuples where the first element is the 
#example: [(3, 2), (2, 2), (2, 3)] means there's a note at the 0th position with duration 2, 0+3 = 3rd position with duration 2, 0+3+2 = 5th position with duration 3. 
def generate_notes_for_bar(bar_length, pattern):
    notes = []
    for i in range(len(pattern)):
        new_note_start = sum([x[0] for x in pattern[:i]])
        new_note_len = pattern[i][1]
        notes.append({'start' : new_note_start, 'length' : new_note_len})
    return notes


#Gets a dictionary containing data on how to order notes. 
def get_timings(starting_beats = [], bar_length = 4, number_of_bars = 4, pattern = [], accents = {}, base_volume = 50, max_note_len = 3):
    pattern = pattern or make_bar_pattern(bar_length, max_note_len)
    base_bars = [
        {'bar_offset' : bar_length * i, "base_volume" : base_volume, "notes" : generate_notes_for_bar(bar_length, pattern)}
    for i in range(number_of_bars)]

    bars = []

    for starting_beat in starting_beats: 
        new_bars = copy.deepcopy(base_bars)
        for bar in new_bars: 
            bar['start'] = bar['bar_offset'] + starting_beat
            bar['starting_beat'] = starting_beat

        bars += new_bars

    bars = handle_timing(bars)
    bars = handle_accenting(bars, accents)
    return bars

def handle_timing(bars):
    for bar in bars: 
        for note in bar['notes']: 
            note['start'] += bar['start']
 
    return bars
   

#Gets the timed list of notes and increases the volume of the notes based on the accent_list
#Example, in a list with 6 notes, the accent_list {0 : 10, 2 : 20} will increase the 
def handle_accenting(bars, accents):
    for bar in bars: 
        for i in range(len(bar['notes'])): 
            note = bar['notes'][i]
            note['volume'] = bar['base_volume'] + accents.get(i, 0)

    return bars
