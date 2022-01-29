import pyspark
from pyspark.sql import SparkSession

sc = pyspark.SparkContext("local[*]")
print("spark version = ", sc.version)

URI           = sc._gateway.jvm.java.net.URI
Path          = sc._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem    = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration

fs = FileSystem.get(URI("hdfs://localhost:9000"), Configuration())

status = fs.listStatus(Path('/input/yelp'))

for fileStatus in status:
    print(fileStatus.getPath())

