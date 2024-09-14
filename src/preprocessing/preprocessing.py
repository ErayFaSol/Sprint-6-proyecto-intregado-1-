# src/preprocessing/preprocessing.py
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.lower()
    df['year_of_release'] = df['year_of_release'].astype('Int64')
    df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
    df.dropna(subset=['name', 'genre', 'year_of_release'], inplace=True)
    df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)
    return df
