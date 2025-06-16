# analysis/performance_metrics.py
import numpy as np
import pandas as pd

def calculate_performance(df, capital=10000, periods_per_year=365*24):  # hourly = 8760 per year
    equity = df['equity_curve']
    returns = df['strategy_returns']

    total_return = equity.iloc[-1] / capital - 1
    annualized_return = (1 + total_return) ** (periods_per_year / len(df)) - 1

    sharpe_ratio = np.mean(returns) / np.std(returns) * np.sqrt(periods_per_year)
    
    cumulative = equity
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()

    return {
        "Total Return": total_return,
        "Annualized Return": annualized_return,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown": max_drawdown,
    }
