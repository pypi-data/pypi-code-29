from ._calculate_q_eq.match_closest_pair import match_closest_pairs
from ._calculate_q_eq.create_count_matrices import create_count_matrices
from ._calculate_q_eq.calculate_q_eq import calculate_q_eq

# COMPARE_INDELS_FLAG decides if indels should be included when comparing likeness of sequences
def bw_estimator(THRESHOLD, MULTIALIGNMENT_LIST, COMPARE_INDELS_FLAG = False):
    aggregated_count_matrix_list = []
    
    for MULTIALIGNMENT in MULTIALIGNMENT_LIST:
        CLOSEST_PAIRS = match_closest_pairs(MULTIALIGNMENT, COMPARE_INDELS_FLAG)
        COUNT_MATRIX_LIST = create_count_matrices(CLOSEST_PAIRS)
        aggregated_count_matrix_list.extend(COUNT_MATRIX_LIST)

    Q, EQ = calculate_q_eq(aggregated_count_matrix_list, THRESHOLD)
    
    return Q, EQ