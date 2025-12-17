# Databricks notebook source
from pyspark.sql.functions import *


# COMMAND ----------

df_bronze = spark.table("bronze_crypto_prices")


# COMMAND ----------

df_silver = (
    df_bronze
    .dropDuplicates(["id", "ingestion_timestamp"])
    .withColumn("symbol", upper(col("symbol")))
    .filter(col("current_price").isNotNull())
)


# COMMAND ----------

USD_TO_BRL = 5.0

df_silver = (
    df_silver
    .withColumn("price_brl", col("current_price") * lit(USD_TO_BRL))
)


# COMMAND ----------

(
    df_silver
    .write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("silver_crypto_prices")
)


# COMMAND ----------

spark.sql("SELECT * FROM silver_crypto_prices").display()
