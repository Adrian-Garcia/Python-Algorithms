'''
Machine Learning
	Machine Learning is making the computer learn from studying data and statistics.
	Machine Learning is a step into the direction of artificial intelligence (AI).
	Machine Learning is a program that analyses data and learns to predict the outcome.

	from: https://www.w3schools.com/python/python_ml_getting_started.asp
'''
import numpy as np
from scipy import stats

class MachineLearning(object):
	
	def theTripleM(self):

		speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

		print("speed = {}".format(speed))
		print("mean = {}".format(np.mean(speed)))
		print("median = {}".format(np.median(speed)))
		print("mode = {}".format(stats.mode(speed)))

	'''
	Remember
		Standard deviation = σ
		Variance = σ²
		
		Both represents number that describes how spread out the values are
	'''
	def standardDeviation(self):


		speed = [86,87,88,86,87,85,86]

		print("speed = {}".format(speed))
		print("standard deviation = {}".format(np.std(speed)))
		print("variance = {}".format(np.var(speed)))

	'''
	Remember
		Percentiles are used in statistics to give you a number that describes the value 
		that a given percent of the values are lower than.
	'''
	def percentiles(self):	

		ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
		
		print("ages = {}".format(ages))
		print("age that 75% of the people are younger than: {}".format(np.percentile(ages, 75)))
		print("age that 90% of the people are younger than: {}".format(np.percentile(ages, 90)))

	def dataDistribution(self):
		pass

obj = MachineLearning()
obj.dataDistribution()