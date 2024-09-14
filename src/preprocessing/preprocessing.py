import pandas as pd

def preprocess_data(df):
    df.columns = df.columns.str.lower()
    df['year_of_release'] = df['year_of_release'].astype('Int64')
    df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
    df = df.dropna(subset=['name', 'genre', 'year_of_release'])
    df.loc[:, 'total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)
    return df