import pyspark
from pyspark.sql import SparkSession
import logging as l
l.basicConfig(format='%(levelname)s | %(asctime)s | %(message)s', level=l.INFO)

FILESYSTEM = "file://" # localfile needs 'file://'
HDFS_NODE = "localhost:9000" # hostname and namenode port, default = 9000
HDFS_PATH = "/input/yelp/yelp_academic_dataset_review.json" # include first '/' but not last, use entire path if accessing local file


# if not hdfs, disregard node variable
if "hdfs" not in FILESYSTEM:
    HDFS_NODE = ""

FILE_ACCESS = f"{FILESYSTEM}{HDFS_NODE}{HDFS_PATH}"


spark = SparkSession.builder.appName('local[*]').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("WARN")
l.info("-----SPARK SESSION STARTED-----")

l.info(f"Accesing file: {FILE_ACCESS}")
df = spark.read.json(FILE_ACCESS)
l.info("file read complete")
l.info(f"file details - rows: {df.count()}, columns: {len(df.columns)}")
df.printSchema()
# df.show()