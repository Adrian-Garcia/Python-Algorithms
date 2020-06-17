import operator as op 
from functools import reduce

class ProbabilityDistributions(object):

	'''
	Calculate number of combinations
		n = number of objects
		r = number of samples
	'''
	def nCr(self, n, r):

		r = min(r, n-r)	
		num = reduce(op.mul, range(n, n-r, -1,), 1)
		denom = reduce(op.mul, range(1, r+1), 1)

		return num // denom

	'''
	Binomial distibution
		n = number of experiments
		x = number of successful experiments
		p = probability of success
	'''
	def binomial(self, n, x, p):

		return self.nCr(n, x) * pow(p,x) * pow((1 - p), (n-x))


calculus = ProbabilityDistributions()
print(calculus.binomial(9, 5, 0.5))