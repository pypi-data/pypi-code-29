""" Common functions not related to parsing or IO.
"""
from math import factorial


def is_strand_value_legal(strand):
    legal_value_set = {"+", "-"}
    if strand in legal_value_set:
        return True
    return False


def impute_strand(a_to_g_cnt=0, t_to_c_cnt=0, impute_threshold=0.8, throw_error_on_fail=False):
    """

    :param record_strand:
    :param a_to_g_cnt:
    :param t_to_c_cnt:
    :param impute_threshold:
    :param throw_error_on_fail:
    :return:
    """
    strand = "."
    if a_to_g_cnt * impute_threshold > t_to_c_cnt:
        strand = "+"
    elif a_to_g_cnt < t_to_c_cnt * impute_threshold:
        strand = "-"
    elif throw_error_on_fail:
        print("ERROR: Cannot accurately impute strand.")
        exit()
    return strand


def get_refernce_and_alt_characters(strand, throw_error_on_fail=False):
    """

    :param strand:
    :param throw_error_on_fail:
    :return:
    """
    reference_character, alternative_character = None, None
    if strand == "+":
        reference_character, alternative_character = "A", "G"
    elif strand == "-":
        reference_character, alternative_character = "T", "C"
    elif throw_error_on_fail:
        print("ERROR: Cannot accurately impute strand.")
        exit()

    return reference_character, alternative_character



def find_countable_character_positions(reference_genome, chromosome, start, end, count_char):
    """

    :param reference_genome:
    :param chromosome:
    :param start:
    :param end:
    :param count_char:
    :return:
    :return:
    """
    # Next get the reference sequence
    sequence = reference_genome.fetch(chromosome, start, end)
    # Make a list of all editable positions i.e. locations of all A or C in region depending on strand.
    # Here we use a set as we will iterate over reads in the next step checking to see if the site is
    # included in the positions to check list.
    return get_set_of_positions_matching_character_from_sequence(sequence, count_char, start)


def passes_min_coverage(coverage, min_coverage):
    """ Check to ensure coverage passes the minimum coverage requirement.
     This function is intended to prevent confusion between < and <= if each comparision was done independently.

    :param coverage:
    :param min_coverage:
    :return:
    """
    if coverage >= min_coverage:
        return True
    return False


def passes_min_editing(editing, min_editing):
    """
    Check to ensure editing rate passes the minimum coverage requirement.
    This function is intended to prevent confusion between < and <= if each comparision was done independently.


    >>> passes_min_editing(10, 5)
    True

    :param editing:
    :param min_editing:
    :return:
    """
    if editing >= min_editing:
        return True
    return False


def passes_max_percent_editing(ref_cnt, alt_cnt, max_percent_coverage):
    """ This function is intended to allow us to filter out SNVs, under the assumption that SNVs mistaken as editing
    will have an extremely high percentage of editing bases i.e. around 100%.

    :param ref_cnt: The number of reference bases overlapping a site.
    :param alt_cnt: The number of alt or edited bases at a site.
    :param max_percent_coverage: A float between 0 and 1:
    :return:
    """

    editing_ratio = alt_cnt / float(ref_cnt+alt_cnt)
    if editing_ratio <= max_percent_coverage:
        return True
    return False


def choose(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)


def determine_aggregation_depth(min_editing):
    # =============================================================================================
    # Determine depth to begin aggregation.
    # After a certain depth more reads will negligibly increase the change of detecting editing.
    # =============================================================================================
    # min_coverage = int(min_coverage)
    min_editing = int(min_editing)
    max_depth = 1
    for i in range(min_editing, 5000):
        detection_prob = 1.0 - choose(i, min_editing) * 0.2 * 0.8**i
        max_depth = i
        if detection_prob > 0.99:
            break
    return max_depth


def get_ref_and_alt_bases_at_site(aligned_reads, chromosome, position, ref_char, alt_char):
    """

    :param aligned_reads:
    :param chromosome:
    :param position:
    :param ref_char:
    :param alt_char:
    :return:
    """
    ref_cnt, alt_cnt,other_cnt = 0, 0, 0

    for read in aligned_reads.fetch(chromosome, position, position+1):
        for i in range(len(read.query_sequence)):
            if read.pos + i == position:

                read_base = read.query_sequence[i]

                if read_base == ref_char:
                    ref_cnt += 1
                elif read_base == alt_char:
                    alt_cnt += 1
                else:
                    other_cnt += 1

    return ref_cnt, alt_cnt, other_cnt


def get_edited_character(record_strand, a_to_g_cnt=0, t_to_c_cnt=0, pos_editing_char="G", neg_editing_char="C"):
    """

    :param record_strand:
    :param a_to_g_cnt:
    :param t_to_c_cnt:
    :param pos_editing_char:
    :param neg_editing_char:
    :return:
    """

    # First decide which strand we are on.
    if record_strand == "+":
        count_char = pos_editing_char
    elif record_strand == "-":
        count_char = neg_editing_char
    else:
        try:
            pos_strand_alt_cnt = a_to_g_cnt
        except KeyError:
            pos_strand_alt_cnt = 0

        try:
            neg_strand_alt_cnt = t_to_c_cnt
        except KeyError:
            neg_strand_alt_cnt = 0

        if pos_strand_alt_cnt > neg_strand_alt_cnt:
            count_char = pos_editing_char
        else:
            count_char = neg_editing_char

    return count_char





def get_strand(record_strand, a_to_g_cnt, t_to_c_cnt):
    """ Determine the reference character for editing should be given a strand or character counts.

    :param record_strand:
    :param a_to_g_cnt:
    :param t_to_c_cnt:
    :return:
    """
    pos_strand_char = "A"
    neg_strand_char = "T"

    # First decide which strand we are on.
    if record_strand == "+":
        # Count A
        count_char = pos_strand_char
    elif record_strand == "-":
        # Count C
        count_char = neg_strand_char
    else:
        try:
            pos_strand_alt_cnt = a_to_g_cnt
        except KeyError:
            pos_strand_alt_cnt = 0

        try:
            neg_strand_alt_cnt = t_to_c_cnt
        except KeyError:
            neg_strand_alt_cnt = 0

        if pos_strand_alt_cnt > neg_strand_alt_cnt:
            count_char = pos_strand_char
        else:
            count_char = neg_strand_char

    return count_char


def base_transition_tuples_and_titles(bases=("A", "C", "G", "T")):
    # Generate data structures for Base counting.
    transition_tuple_list = []
    transition_tuple_titles = []
    # Make all unique transitions
    for b1 in bases:
        for b2 in bases:
            if b1 != b2:
                transition_tuple_list.append((b1, b2))
                transition_tuple_titles.append("%s>%s" % (b1, b2))

    return transition_tuple_titles, transition_tuple_list



