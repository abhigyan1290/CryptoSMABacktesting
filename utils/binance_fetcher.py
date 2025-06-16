# utils/binance_fetcher.py
from binance.client import Client
import pandas as pd
import os

def fetch_binance_ohlcv(symbol="BTCUSDT", interval="1h", start_str="1 Jan, 2023"):
    client = Client()
    klines = client.get_historical_klines(symbol, interval, start_str)

    cols = [
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base', 'taker_buy_quote', 'ignore'
    ]
    df = pd.DataFrame(klines, columns=cols)

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    numeric_cols = ['open', 'high', 'low', 'close', 'volume']
    df[numeric_cols] = df[numeric_cols].astype(float)

    df = df.set_index('timestamp')[['open', 'high', 'low', 'close', 'volume']]
    return df
