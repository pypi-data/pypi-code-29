'''
How to run:

'''

import os
import sys

class normalizeData(object):
  """docstring for normalizeData"""
  def __init__(self, *args):
      # super(normalizeData, self).__init__()
      # self.args = "100,200,300,400"
      self.data_argv = self.data_set = sys.argv[1]
      try:
          validation_result = self.validate_argv()
          if validation_result:
              # print self.data_set
              print "\nStandard Deviation(Population): ", self.stddev()
              print "\nStandard Deviation(Sample): ", self.stddev(std_dev_var = 1)
              print "\nZ-score: ", self.z_score()
              print "\nDecimal Scaling: ", self.dec_scaling()
              print "\nMin-Max(0-1): ", self.min_max()
      except Exception as constructor_err:
          print 'Please enter a valid arguments', constructor_err
          sys.exit()

  def validate_argv(self):
      # self.data_argv = self.args[0]
      try:
          self.data_argv = self.data_argv.split(",")
          # check if all values are digits/numeric
          # self.data_set = list( map(lambda val: int(val) if val.isnumeric() else False, self.data_argv))
          self.data_set = list(map(int, self.data_argv))
          return True
      except Exception as e:
          raise e
      return False

  def num_of_digits(self, number):
      count = 0
      while (number > 0):
        number = number//10
        count = count + 1
      return count

  def dec_scaling(self):
      """Return the sample arithmetic mean of data."""
      max_val = max(self.data_set)
      num_of_dig = self.num_of_digits(max_val)
      denom = 10.0**num_of_dig
      def dec_scaling_inner(val):
          return (val/denom)
      dec_scaling_res = map(dec_scaling_inner, self.data_set)
      return dec_scaling_res

  def min_max(self):
      """Return the sample arithmetic mean of data."""
      min_val = min(self.data_set) 
      max_val = max(self.data_set)
      delta = max_val - min_val
      def min_max_inner(val):
          return ((val - min_val)/ delta)*(1-0)+0

      min_max_res = map(min_max_inner, self.data_set)
      return min_max_res

  def mean(self):
      """Return the sample arithmetic mean of data."""
      n = len(self.data_set)
      if n < 1:
          raise ValueError('Mean requires at least one data point')
      return sum(self.data_set)/n

  def stddev(self, std_dev_var=0):
      """Calculate the Standard-Deviation(population) by default;
      specify ssd=1 to compute the standard deviation(sample)"""
      total_data_len = len(self.data_set)
      # print "\ntotal_data_len: ", self.data_set
      if total_data_len < 2:
          raise ValueError('Variance requires at least two data points')
      mean_val = self.mean()
      summation_val = sum((x-mean_val)**2 for x in self.data_set)
      return (summation_val/(total_data_len - std_dev_var))**0.5

  def z_score(self):
      sigma = self.stddev()
      mean_val = self.mean()
      def z_score_calc(val):
          return (val-mean_val)/sigma
      z_score_val = map(z_score_calc, self.data_set)
      return z_score_val

n = normalizeData()
