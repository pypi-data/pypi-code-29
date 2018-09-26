def csvtodict(filename, **kwargs):
    if ('skipheader' in kwargs):
        if kwargs['skipheader']==True:skip=0
        else:skip=-1
    else: skip=-1
    
    if ('headers' in kwargs):
        headers={}
        for each in kwargs['headers']: headers[each]=[]
    else:
        return("provide headers!")
    
    with open(filename) as f:
        for index, line in enumerate(f):
            if index!=skip:
                splitline=line.split()
                for INDEX, EACH in enumerate(headers): headers[EACH].append(float(splitline[INDEX]))
    return(headers)

