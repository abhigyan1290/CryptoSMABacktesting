# strategy/rules.py
import pandas as pd
from .indicators import sma, rsi

def generate_signals(df: pd.DataFrame, fast_period=20, slow_period=50, rsi_period=14, rsi_oversold=30, rsi_overbought=70):
    df['fast_ma'] = sma(df['close'], fast_period)
    df['slow_ma'] = sma(df['close'], slow_period)
    df['rsi'] = rsi(df['close'], rsi_period)

    df['signal'] = 0  # default = no position

    long_entry = (df['close'] < df['fast_ma']) & (df['fast_ma'] > df['slow_ma']) & (df['rsi'] < rsi_oversold)
    long_exit = (df['close'] > df['fast_ma'])

    short_entry = (df['close'] > df['fast_ma']) & (df['fast_ma'] < df['slow_ma']) & (df['rsi'] > rsi_overbought)
    short_exit = (df['close'] < df['fast_ma'])

    df.loc[long_entry, 'signal'] = 1
    df.loc[long_exit, 'signal'] = 0

    df.loc[short_entry, 'signal'] = -1
    df.loc[short_exit, 'signal'] = 0

    return df
