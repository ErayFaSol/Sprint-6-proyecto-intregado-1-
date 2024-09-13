# src/utilities/helpers.py
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def show_data(df, n=15):
    return df.head(n)
