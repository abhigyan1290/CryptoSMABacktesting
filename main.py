from utils.binance_import import fetch_binance_ohlcv
from strategy.rules import generate_signals
from strategy.backtest import backtest
import matplotlib.pyplot as plt
from analysis.performance_metrics import calculate_performance

def main():
    df = fetch_binance_ohlcv("BTCUSDT", "1h", "1 Jan, 2023")
    df = generate_signals(df)
    df = backtest(df)

    df[['close', 'equity_curve']].plot(subplots=True, figsize=(12, 8))
    plt.suptitle("Live Binance Dual MA Strategy")
    plt.show()

    metrics = calculate_performance(df)
    print("\n📊 Performance Metrics:")
    for k, v in metrics.items():
        print(f"{k:20}: {v:.2%}")

if __name__ == "__main__":
    main()
