import mysql.connector
import pandas as pd
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# --- MySQL Connection ---
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

# --- Fetch incident data ---
query = "SELECT * FROM incidents LIMIT 10;"
df = pd.read_sql(query, conn)
print("Data fetched from MySQL:")
print(df)

# --- OpenAI Integration ---
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = f"Summarize this incident data and provide actionable recommendations:\n{df.to_dict()}"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
print("\nAI Summary and Recommendations:")
print(response['choices'][0]['message']['content'])
