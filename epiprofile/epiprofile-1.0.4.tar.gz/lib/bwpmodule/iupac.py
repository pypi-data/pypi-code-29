def compliment(seq):
	'''make a complementary sequence of DNA'''
	comp_str=""
	iupac = {
	'A':'T',
	'T':'A',
	'C':'G',
	'G':'C',
	'M':'K',
	'R':'Y',
	'W':'W',
	"S":"S",
	"Y":"R",
	"K":"M",
	"V":"B",
	"B":"V",
	"H":"D",
	"D":"H",
	"N":"N"
	}
	for i in seq.upper():
		if i in iupac:
			comp_str += iupac[i]
		else:
			comp_str += "X"
	return comp_str[::-1]

def gap_palindrome(seq,gap_st=0,gap_end=10):
	'''make gapped palindrome for motif sequence'''
	half1 = seq
	half2 = compliment(half1)
	patterns=[]
	for i in range(gap_st,gap_end + 1):
		patterns.append(half1 + 'N'*i + half2)
	
	half1 = compliment(seq)
	half2 = compliment(half1)
	for i in range(gap_st,gap_end + 1):
		patterns.append(half1 + 'N'*i + half2)
	return patterns
	
	