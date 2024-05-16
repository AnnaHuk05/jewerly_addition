import pandas as pd
import pyodbc
import os
from key_info import info
from sqlalchemy import text
import sqlalchemy
from google.cloud.sql.connector import Connector
from google.oauth2 import service_account
from sqlalchemy import create_engine

def insert_data_from_json(json_file):
    table_name = os.path.splitext(os.path.basename())[0]
    data = pd.read_csv(json_file)
    data.replace('n/a', pd.NA, inplace=True)
    connection_str = f"postgresql://{info['db_user']}:{info['db_pass']}@{info['db_host']}:{info['db_port']}/{info['db_name']}"
    engine = create_engine(connection_str)
    print(table_name)
    data.to_sql(name=table_name, con=engine, if_exists='append', index=False)


   
tables = [
    'address',
    'traiding_point',
    'person',
    'vendor_brand',
    'customer',
    'manager',
    'orders',
    'contract',
    'consultation',
    'payment',
    'scheduled_reminder',
    'storage'
]

# Параметри підключення до бази даних
project  = info["project_id"]
region = info["db_region"]
instance = info["instance_id"]
CREDENTIALS = r"composite-set-421515-09598d364101.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS)
INSTANCE_CONNECTION_NAME = (
            f"{project}:{region}:{instance}")
print(INSTANCE_CONNECTION_NAME)
sql_connector = Connector(credentials=credentials)
conn = sql_connector.connect(
            INSTANCE_CONNECTION_NAME,
            "pg8000",
            user=info["db_user"],
            password=info["db_pass"],
            db=info["db_name"],
        )
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://", creator=lambda: conn, pool_timeout=36000
)

csv_directory = r"C:\6 sem\DW\csvresource"

for table_name in tables:
    file_path = os.path.join(csv_directory, f"{table_name}.csv")
    if os.path.exists(file_path):
        insert_data_from_json(file_path)

conn.close()