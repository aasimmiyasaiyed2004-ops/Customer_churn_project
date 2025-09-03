import pandas as pd
import csv

df=pd.read_csv("C:/Users/Aasimmiya saiyed/OneDrive/Documents/Telco_customer_churn.csv")
print(df.describe())
print(df.info())


df['Total Charges']=pd.to_numeric(df['Total Charges'],errors='coerce')

invalid=df[pd.to_numeric(df['Total Charges'],errors='coerce').isna()]
print(invalid)


df.fillna({"Churn Reason":"Nan"},inplace=True)

print(df.drop_duplicates())

print(df.info())

output_path = "C:/Users/Aasimmiya saiyed/Desktop/telco_cleaned.csv"
df.to_csv(output_path, encoding="UTF-8", index=False)
print(f"File saved successfully at: {output_path}")
