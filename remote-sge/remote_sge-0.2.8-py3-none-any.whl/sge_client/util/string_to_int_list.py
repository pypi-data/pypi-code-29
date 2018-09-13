"String parsing utility function for parsing string into list of integers."

def string_to_int_list(job_range):
    """
    Receives a string in the form of "1,2,3-10,20" etc, and returns a list of integers
    represented by the input.
    """
    result = set()
    # for x in job_ranges:
    for part in job_range.split(','):
        if '-' in part:
            a, b = part.split('-')
            a, b = int(a), int(b)
            for i in range(a, b+1):
                result.add(i)
        else:
            a = int(part)
            result.add(a)
    return sorted(result)
