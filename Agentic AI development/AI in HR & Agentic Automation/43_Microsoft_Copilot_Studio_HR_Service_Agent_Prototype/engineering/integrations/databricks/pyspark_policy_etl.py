"""OPTIONAL PySpark/Databricks lab notebook script; not executed in a Databricks workspace.
Inputs: synthetic policies.json uploaded to DBFS/Unity Catalog accessible path.
Outputs: validated Delta data and quarantined examples (no PII).
"""
from pyspark.sql import SparkSession, functions as F


def run(input_json, silver_delta_path, quarantine_delta_path):
    spark=SparkSession.builder.appName("HRPolicyLab_ETL").getOrCreate()
    raw=spark.read.option("multiLine",True).json(input_json)
    checks=(F.col("policy_id").startswith("HR-POL-") &
            F.col("approved").eqNullSafe(True) &
            (F.length(F.col("body")) >= 60) &
            (F.to_date("effective_from") <= F.current_date()) &
            (F.to_date("effective_to") >= F.current_date()))
    enriched=raw.withColumn("is_valid",checks).withColumn("source_ingested_at",F.current_timestamp())
    enriched.filter("is_valid").drop("is_valid").write.format("delta").mode("overwrite").save(silver_delta_path)
    enriched.filter("NOT is_valid").write.format("delta").mode("overwrite").save(quarantine_delta_path)
    return {"bronze_records":raw.count(),"silver_records":enriched.filter("is_valid").count(),
            "quarantined":enriched.filter("NOT is_valid").count()}
