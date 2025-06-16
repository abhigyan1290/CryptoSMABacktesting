# utils/binance_fetcher.py
from binance.client import Client
import pandas as pd
import os

def fetch_binance_ohlcv(symbol="BTCUSDT", interval="1h", start_str="1 Jan, 2023"):
    client = Client()
    klines = client.get_historical_klines(symbol, interval, start_str)

    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['close'] = pd.to_numeric(df['close'])

    df = df[['timestamp', 'close']]
    df.set_index('timestamp', inplace=True)
    return df

def save_to_csv(df, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath)
