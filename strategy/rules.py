# strategy/rules.py
import pandas as pd
from .indicators import sma, rsi, bollinger_bands

def generate_signals(df: pd.DataFrame,
                     bb_period=20,
                     std_mult=2.0,
                     rsi_period=14,
                     rsi_os=30,
                     rsi_ob=70,
                     fast_trend=50,
                     slow_trend=200):
    """
    Long  when price <= lower band AND RSI < oversold AND trend filter bullish
    Short when price >= upper band AND RSI > overbought AND trend filter bearish
    Exit  when price crosses mid band or RSI normalises
    """
    # --- indicators
    df['fast_sma']   = sma(df['close'], fast_trend)
    df['slow_sma']   = sma(df['close'], slow_trend)
    df['bb_mid'], df['bb_up'], df['bb_lo'] = bollinger_bands(df['close'], bb_period, std_mult)
    df['rsi'] = rsi(df['close'], rsi_period)

    bullish = df['fast_sma'] > df['slow_sma']            # overarching up-trend
    bearish = df['fast_sma'] < df['slow_sma']

    # --- signals initialised to 0 (flat)
    df['signal'] = 0

    # LONG entry and exit
    long_entry = (df['close'] <= df['bb_lo']) & (df['rsi'] < rsi_os) & bullish
    long_exit  = (df['close'] >= df['bb_mid']) | (df['rsi'] > 50)

    # SHORT entry and exit
    short_entry = (df['close'] >= df['bb_up']) & (df['rsi'] > rsi_ob) & bearish
    short_exit  = (df['close'] <= df['bb_mid']) | (df['rsi'] < 50)

    df.loc[long_entry,  'signal'] =  1
    df.loc[long_exit,   'signal'] =  0   # flatten
    df.loc[short_entry, 'signal'] = -1
    df.loc[short_exit,  'signal'] =  0

    return df
