from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession,SQLContext
from pyspark.sql.functions import when, lit, col
from pyspark.sql.types import DateType
from py4j.protocol import Py4JJavaError

from functools import reduce
from pyspark.sql import DataFrame
import pandas
#Biblioteca pyspark com tipo das vars
from pyspark.sql.types import DoubleType, FloatType

#Biblioteca pyspark com tipo das vars
from pyspark.sql.types import *

from pyspark.sql import SparkSession, SQLContext

class Spark:
  def __init__(self):
    self.spark = SparkSession.builder\
                .appName("BaseEnriquecida")\
                .enableHiveSupport()\
                .config("spark.yarn.executor.memoryOverhead","4G")\
                .config("spark.executor.memory", "12G")\
                .config("spark.dynamicAllocation.enabled", "true")\
                .config("spark.dynamicAllocation.initialExecutors", "2")\
                .config("spark.dynamicAllocation.maxExecutors","5")\
                .config("spark.executor.cores", "8")\
                .config("spark.cores.max", "3")\
                .config("spark.driver.memory", "4G")\
                .config("spark.ui.killEnabled", "true")\
                .getOrCreate()
    
    self.sqlContext = SQLContext(self.spark)
  
  def getSpark(self):
    return self.spark
  
  def getSqlContext(self):
    return self.sqlContext