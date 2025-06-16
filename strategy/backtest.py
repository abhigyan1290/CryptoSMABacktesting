#Portfolio simulation + metrics

# strategy/backtest.py
import pandas as pd

def backtest(df: pd.DataFrame, capital=10000, fee=0.001):
    df['position'] = df['signal'].shift(1).fillna(0)  # shift to avoid lookahead bias
    df['returns'] = df['close'].pct_change()
    df['strategy_returns'] = df['returns'] * df['position']

    df['strategy_returns'] = df['strategy_returns'] - (fee * abs(df['position'].diff().fillna(0)))  # fees

    df['equity_curve'] = capital * (1 + df['strategy_returns']).cumprod()

    return df

