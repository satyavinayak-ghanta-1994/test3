import time
from google.cloud import bigquery
key_path="D:\GCP\Projects Key Json files\myprojectthroughsdk-d4c5b54c5700.json"
client=bigquery.Client.from_service_account_json(key_path)
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

table_id = "myprojectthroughsdk.US_Airport.USAirport"

with open(r'D:\GCP\Public Data Set Biquery\US Airports.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

while job.state != 'DONE':
    time.sleep(2)
    job.reload()
    print(job.state)

print(job.result())

table = client.get_table(table_id)
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
) 