import numpy as np

### Private functions
def _matching_letters(a,b, COMPARE_INDELS_FLAG):
    assert(len(a) == len(b))

    number_of_matching_positions = 0

    if COMPARE_INDELS_FLAG:
        for x,y in zip(a,b):
            if x == y and x != '-' :
                number_of_matching_positions += 1
    else:
        number_of_matching_positions = np.sum(a==b) # Faster than when indels have to be ignored
                   
    return number_of_matching_positions

### Interface
def match_closest_pairs(sequence_list, COMPARE_INDELS_FLAG):
    assert (len(sequence_list) % 2) == 0

    indexes_and_matching_letters = []

    for PRIMARY_INDEX, PRIMARY_SEQUENCE in enumerate(sequence_list):
        for SECONDARY_INDEX in range(PRIMARY_INDEX+1, len(sequence_list)):
            SECONDARY_SEQUENCE = sequence_list[SECONDARY_INDEX]
            MATCHING_LETTERS = _matching_letters(PRIMARY_SEQUENCE, SECONDARY_SEQUENCE, COMPARE_INDELS_FLAG)

            INDEXES = (PRIMARY_INDEX, SECONDARY_INDEX)
            INDEX_SCORE_TUPLE = (INDEXES, MATCHING_LETTERS)
            indexes_and_matching_letters.append(INDEX_SCORE_TUPLE)

    indexes_and_matching_letters.sort(key=lambda tup: tup[1], reverse = True)   # Sort on matching letters
    matched_indexes = []
    closest_pairs = []
    NUMBER_OF_SEQUENCES = len(sequence_list)

    while len(matched_indexes) != NUMBER_OF_SEQUENCES:
        CURRENT_INDEX_AND_MATCHING_LETTERS_TUPLE = indexes_and_matching_letters.pop(0)
        FIRST_INDEX = CURRENT_INDEX_AND_MATCHING_LETTERS_TUPLE[0][1]
        SECOND_INDEX = CURRENT_INDEX_AND_MATCHING_LETTERS_TUPLE[0][0]

        if not(FIRST_INDEX in matched_indexes) and not(SECOND_INDEX in matched_indexes):
            matched_indexes.append(FIRST_INDEX)
            matched_indexes.append(SECOND_INDEX)

            FIRST_SEQUENCE = sequence_list[FIRST_INDEX]
            SECOND_SEQUENCE = sequence_list[SECOND_INDEX]
            closest_pairs.append((FIRST_SEQUENCE, SECOND_SEQUENCE))

    return closest_pairs