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



def period(BJD,flux,**kwargs):

    from gatspy.periodic import LombScargleFast

    if ('dmag' in kwargs): dmag=kwargs['dmag']
    else: dmag=0.000005
    if ('nyquist_factor' in kwargs): nyquist_factor=kwargs['nyquist_factor']
    else: nyquist_factor=40
    
    model = LombScargleFast().fit(BJD, flux, dmag)
    periods, power = model.periodogram_auto(nyquist_factor)
    
    if ('model.optimizer.period_range' in kwargs): model.optimizer.period_range=kwargs['model.optimizer.period_range']
    else: model.optimizer.period_range=(0.2, 1.4)

    period = model.best_period
    return period
