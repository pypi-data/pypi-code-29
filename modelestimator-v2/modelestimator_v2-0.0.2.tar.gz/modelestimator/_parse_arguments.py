def parse_arguments(argument_list):
    FORMAT = argument_list.pop(0)
    FORMAT = FORMAT.lower()

    if FORMAT not in ['fasta', 'stockholm', 'phylip']:
        raise Exception()

    #   Options
    bootstrap = False
    threshold = None
    resamplings = None

    while argument_list[0][0] == "-":
        if argument_list[0][1] == "t" or argument_list[0][1] == "threshold":
            argument_list.pop(0)
            threshold = float(argument_list.pop(0))
            if not(threshold > 0 and threshold < 1):
                raise Exception()
        
        elif argument_list[0][1] == "b" or argument_list[0][1] == "bootstrap":            
            argument_list.pop(0)
            bootstrap = True

            resamplings = int(argument_list.pop(0))
            if not(resamplings > 0):
                raise Exception()


    FILE_LIST = argument_list
    if (len(FILE_LIST) == 0) or (bootstrap and len(FILE_LIST) > 1):
        raise Exception()

    return FORMAT, bootstrap, resamplings, threshold, FILE_LIST