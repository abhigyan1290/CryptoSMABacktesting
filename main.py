# main.py

import os
import matplotlib.pyplot as plt
from utils.binance_fetcher import fetch_binance_ohlcv
from strategy.rules import generate_signals
from strategy.backtest import backtest   
from analysis.performance_metrics import calculate_performance

def main():
    df = fetch_binance_ohlcv("BTCUSDT", "1h", "1 Jan, 2023")
    df = generate_signals(df)
    df = backtest(df)
    fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    df['close'].plot(ax=axs[0], title='BTC/USDT Price')
    df['equity_curve'].plot(ax=axs[1], title='Strategy Equity Curve', color='red')
    fig.suptitle("Dual MA Mean Reversion Strategy")
    fig.tight_layout()

    fig.savefig("figures/dual_ma_strategy_result.png", dpi=300, bbox_inches='tight')
    print("Figure saved!")

    plt.show()
    metrics = calculate_performance(df)
    print("\n Performance Metrics:")
    for k, v in metrics.items():
        print(f"{k:20}: {v:.2%}")

if __name__ == "__main__":
    main()
