from google.cloud import bigquery
import os
from key_info import info
def get_dataset_schema(dataset_id, project_id):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id, project=project_id)
    dataset = client.get_dataset(dataset_ref)
    tables = client.list_tables(dataset_ref)

    schema = {}

    for table in tables:
        table_ref = dataset_ref.table(table.table_id)
        table_info = client.get_table(table_ref)
        schema[table.table_id] = table_info.schema

    return schema

CREDENTIALS = r"client_secret_167305746624-jplbjth8bc4spgbptv1khkjcvvmvjr34.apps.googleusercontent.com.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS
schema = get_dataset_schema(info["dataset_id"],info["project_id"])
print(schema)
output_file = "dataset_schema.py"
with open(output_file, "w") as f:
    f.write("schema = ")
    f.write(repr(schema))
