# Databricks notebook source
import requests
from datetime import datetime
from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    
    return response.json()


# COMMAND ----------

data = get_crypto_prices()

schema = StructType([
    StructField("id", StringType()),
    StructField("symbol", StringType()),
    StructField("name", StringType()),
    StructField("current_price", DoubleType()),
    StructField("market_cap", DoubleType()),
    StructField("total_volume", DoubleType())
])

df = spark.createDataFrame(data, schema=schema)


# COMMAND ----------

df_bronze = (
    df
    .withColumn("ingestion_timestamp", current_timestamp())
    .withColumn("ingestion_date", current_date())
)


# COMMAND ----------

(
    df_bronze
    .write
    .format("delta")
    .mode("append")
    .partitionBy("ingestion_date")
    .saveAsTable("bronze_crypto_prices")
)


# COMMAND ----------

spark.sql("SELECT * FROM bronze_crypto_prices").display()
