import csv
# importing the zipfile module
from zipfile import ZipFile
from sqlalchemy import text,create_engine
import pandas as pd
from config import db_password
import psycopg2

  
# loading the temp.zip and creating a zip object
with ZipFile("./AccessGUDID_Delimited_Small_Release_20220201.zip", 'r') as zObject:
  
    zObject.extractall(
        path="./temp")

df = pd.read_csv("./temp/device.txt", sep="|")
# print(df)
relevant_df = df[['PrimaryDI', 'publicDeviceRecordKey', 'deviceDescription']]
print(relevant_df)

conn = psycopg2.connect("host=tech-assessment.ccualigexsnc.us-east-1.rds.amazonaws.com dbname=tech user=psingh password=28JK3C72D09S")
cur = conn.cursor()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE device_data(
    id PrimaryDI PRIMARY KEY,
    publicDeviceRecordKey VARCHAR,
    deviceDescription VARCHAR,
)
""")

