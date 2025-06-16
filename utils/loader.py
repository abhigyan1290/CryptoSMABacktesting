# utils/loader.py
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=['timestamp'], index_col='timestamp')
    df = df.sort_index()
    return df
