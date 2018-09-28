import math
def point_poip(actual, mean):
	'''give poisson pvalue. P[obs ==mean]'''
	# naive:   math.exp(-mean) * mean**actual / factorial(actual)
	# iterative, to keep the components from getting too large or small:
	p = math.exp(-mean)
	for i in xrange(actual):
		p *= mean
		p /= i+1
	return p

def cumu_poip(num, mean,logp=False):
	'''give poisson pvalue P[obs >=mean]'''
	s=0.0
	for i in range(0,num+1):
		s += point_poip(i,mean)
	if logp is True:
		try:
			return -10*math.log10(1-s)
		except:
			return 3000
	else:
		return 1-s
	
def poisson_cdf (n, lam,lower=True):
    """Poisson CDF evaluater.

    This is a more stable CDF function. It can tolerate large lambda
    value. While the lambda is larger than 700, the function will be a
    little slower.

    Parameters:
    n     : your observation
    lam   : lambda of poisson distribution
    lower : if lower is False, calculate the upper tail CDF
    """
    k = int(n)
    if lam <= 0.0:
        raise Exception("Lambda must > 0")

    if lower:
        if lam > 700:
            return __poisson_cdf_large_lambda (k, lam)
        else:
            return __poisson_cdf(k,lam)
    else:
        if lam > 700:
            return __poisson_cdf_Q_large_lambda (k, lam)
        else:
            return __poisson_cdf_Q(k,lam)

def __poisson_cdf (k,a):
    """Poisson CDF For small lambda. If a > 745, this will return
    incorrect result.

    """
    if k < 0:
        return 0                        # special cases
    next = math.exp( -a )
    cdf = next
    for i in xrange(1,k+1):
        last = next
        next = last * a / i
        cdf = cdf + next
    if cdf > 1:
        return 1
    else:
        return cdf
