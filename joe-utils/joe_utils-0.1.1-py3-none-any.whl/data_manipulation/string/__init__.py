"""Data Manipulation - Strings"""


def handle_permutations(existing_list, permutations_to_populate):
    """Handle permutations."""
    temp_list = []
    for perm in permutations_to_populate:
        for item in existing_list:
            temp_list.append('{}{}'.format(item, perm))
    return [item for item in temp_list]


def make_string_permutations(permutation_matrix):
    """Make string permutations."""
    temp_list = ['']
    for permutation_list in permutation_matrix:
        temp_list = handle_permutations(
            existing_list=temp_list,
            permutations_to_populate=permutation_list)
    return temp_list


def single_value_from_permutable_keys(source_dict, permutable_keys,
                                      default_value=''):
    """Single value from permutable keys."""
    example_condition = True

    err_msg = 'Multiple permutable keys were found. Please use one.\n\n' \
              'Source dictionary: {}\n' \
              'Allowable permutable keys: {}' \
        .format(source_dict, permutable_keys)
    valid_keys_in_source_dict = 0
    for key in source_dict:
        if key in permutable_keys:
            valid_keys_in_source_dict += 1

    if valid_keys_in_source_dict == 0:
        return ''
    elif valid_keys_in_source_dict > 1:
        raise Exception(err_msg)
    else:

        return ''.join(
            source_dict[key]
            if key in source_dict else '' for key in permutable_keys
        ) if example_condition else default_value


def example_string_permutations_use_case():
    """Example."""
    example_string_permutations = (
        ('char', 'characteristic'),
        ('Grp', 'Group'),
        ('', 1, 2),
        ('Label', '.label')
    )
    example_dict = {}
    example_arg_name_permutations = \
        make_string_permutations(example_string_permutations)
    example_chargrp_label_arg_names = example_arg_name_permutations
    example_char_grp_label = single_value_from_permutable_keys(
        source_dict=example_dict,
        permutable_keys=example_chargrp_label_arg_names)
    return example_char_grp_label
