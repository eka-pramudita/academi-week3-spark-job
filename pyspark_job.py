# Python imports
import sys

# A Spark Session is how we interact with Spark SQL to create Dataframes
from pyspark.sql import SparkSession

# These allow us to create a schema for our data
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

# This will help catch some PySpark errors
from pyspark.sql.utils import AnalysisException

# Data transforming functions
from pyspark.sql import functions as f

# Create a SparkSession under the name "flight". Viewable via the Spark UI
spark = SparkSession.builder.appName("flight").getOrCreate()

# Create columns schema
fields = [StructField("flight_date", StringType(), True),
          StructField("airline_code", IntegerType(), True),
          StructField("flight_num", IntegerType(), True),
          StructField("source_airport", StringType(), True),
          StructField("destination_airport", StringType(), True),
          StructField("departure_time", StringType(), True),
          StructField("departure_delay", IntegerType(), True),
          StructField("arrival_time", StringType(), True),
          StructField("arrival_delay", IntegerType(), True),
          StructField("airtime", IntegerType(), True),
          StructField("distance", IntegerType(), True),
          StructField("id", IntegerType(), True)]
schema = StructType(fields)

# Create an empty DataFrame. We will continuously union our output with this
flight_data = spark.createDataFrame([], schema)

dates = ["gs://week3/2021-04-27.csv","gs://week3/2021-04-28.csv","gs://week3/2021-04-29.csv", "gs://week3/2021-04-30.csv"]

for i in range(len(dates)):
  flight_data = spark.read.format('csv').option("header", True).load(dates[i], schema=schema).union(flight_data)



# Convert departure and arrival time from str to datetime
# departure_time
flight_data = flight_data.withColumn('length_dep', f.length('departure_time'))
flight_data = flight_data.withColumn('temp1', f.when(flight_data.length_dep == 4,flight_data.departure_time).otherwise(f.concat(f.lit('0'), f.col('departure_time'))))
flight_data = flight_data.withColumn('length_dep', f.length('temp1'))

for i in range(3):
  flight_data = flight_data.withColumn('temp1', f.when(flight_data.length_dep == 4,flight_data.temp1).otherwise(f.concat(f.lit('0'), f.col('temp1'))))
  flight_data = flight_data.withColumn('length_dep', f.length('temp1'))

# arrival_time
flight_data = flight_data.withColumn('length_arr', f.length('arrival_time'))
flight_data = flight_data.withColumn('temp2', f.when(flight_data.length_arr == 4,flight_data.arrival_time).otherwise(f.concat(f.lit('0'), f.col('arrival_time'))))
flight_data = flight_data.withColumn('length_arr', f.length('temp2'))

for i in range(3):
  flight_data = flight_data.withColumn('temp2', f.when(flight_data.length_arr == 4,flight_data.temp2).otherwise(f.concat(f.lit('0'), f.col('temp2'))))
  flight_data = flight_data.withColumn('length_arr', f.length('temp2'))

# concat date and time then convert to datetime
flight_data = flight_data.withColumn('departure_datetime', f.concat(f.col('flight_date'),f.lit(' '), f.col('temp1')))
flight_data = flight_data.withColumn('dt_departure', f.to_timestamp(flight_data.departure_datetime, 'yyyy-MM-dd HHmm'))
flight_data = flight_data.withColumn('arrival_datetime', f.concat(f.col('flight_date'),f.lit(' '), f.col('temp2')))
flight_data = flight_data.withColumn('dt_arrival', f.to_timestamp(flight_data.arrival_datetime, 'yyyy-MM-dd HHmm'))

# drop temporary columns
columns_to_drop = ['departure_time', 'arrival_time', 'temp1', 'temp2', 'departure_datetime',
                   'arrival_datetime', 'flight_date', 'length_dep', 'length_arr']
flight_data = flight_data.drop(*columns_to_drop)

# get triptime
timeFmt = "yyyy-MM-dd HH:mm:ss"
timeDiff = (f.unix_timestamp('dt_arrival', format=timeFmt) - f.unix_timestamp('dt_departure', format=timeFmt))
flight_data = flight_data.withColumn("triptime", timeDiff/60)
flight_data = flight_data.withColumn("triptime", flight_data["triptime"].cast(IntegerType()))

# save table to bigquery
flight_data.write.format('bigquery').option("temporaryGcsBucket", "week3/temp").mode('overwrite').save("flight_data.flight-data")