import mysql.connector
import pandas as pd
import openai

# --- MySQL Connection ---
conn = mysql.connector.connect(
    host="localhost",
    user="incident_user",
    password="Rveera@12",
    database="incident_db"
)

# --- Fetch incident data ---
query = "SELECT * FROM incidents LIMIT 10;"
df = pd.read_sql(query, conn)
print("Data fetched from MySQL:")
print(df)

# --- OpenAI Integration ---
#openai.api_key = "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"

#prompt = f"Summarize this incident data and provide actionable recommendations:\n{df.to_dict()}"
#response = openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[{"role": "user", "content": prompt}]
#)

#print("\nAI Summary and Recommendations:")
#print(response['choices'][0]['message']['content'])
