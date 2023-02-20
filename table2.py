import csv
# importing the zipfile module
from zipfile import ZipFile
from sqlalchemy import text,create_engine
import pandas as pd
import psycopg2
from config import db_password

  
# loading the temp.zip and creating a zip object
with ZipFile("./AccessGUDID_Delimited_Small_Release_20220201.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall(
        path="./temp")

conn = psycopg2.connect("host=tech-assessment.ccualigexsnc.us-east-1.rds.amazonaws.com dbname=tech user=psingh password=28JK3C72D09S")
cur = conn.cursor()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE device_data_2(
    id PrimaryDI PRIMARY KEY,
    some_new_id INTEGER,
)
""")

df = pd.read_csv("./temp/gmdnTerms.txt", sep="|")
print(df)


df.to_csv('gmdnTerms.csv', index=False,encoding='utf-8')
