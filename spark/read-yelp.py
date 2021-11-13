import pyspark
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('local[*]').getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

# df = spark.read.json("hdfs://localhost:9000/input/yelp/trial.json")
df = spark.read.json("file:///tmp/trial.json")
df.printSchema()
df.show()