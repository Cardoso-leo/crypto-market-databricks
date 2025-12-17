# Databricks notebook source
from pyspark.sql.functions import *


# COMMAND ----------

df = spark.table("silver_crypto_prices")


# COMMAND ----------

from pyspark.sql.window import Window

window_spec = Window.partitionBy("id").orderBy("ingestion_timestamp")

df_gold = (
    df
    .withColumn("previous_price", lag("current_price").over(window_spec))
    .withColumn(
        "price_variation_pct",
        ((col("current_price") - col("previous_price")) / col("previous_price")) * 100
    )
)


# COMMAND ----------

(
    df_gold
    .write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold_crypto_indicators")
)


# COMMAND ----------

spark.sql("""
SELECT 
    name,
    symbol,
    current_price,
    price_brl,
    price_variation_pct
FROM gold_crypto_indicators
ORDER BY price_variation_pct DESC
""").display()
