# MACD Crossover Trading Strategy

This repository contains a Python script that implements a basic MACD (Moving Average Convergence Divergence) crossover trading strategy using historical stock price data. The script uses the yfinance library to fetch historical stock data, calculates the MACD indicator, and generates buy and sell signals based on the crossover of the MACD and its signal line.

## Dependencies

- [yfinance](https://pypi.org/project/yfinance/)
- [pandas](https://pypi.org/project/pandas/)
- [numpy](https://pypi.org/project/numpy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [talib](https://pypi.org/project/talib/)

Install the required dependencies using the following command:
```
pip install yfinance pandas numpy matplotlib talib
```

## Usage

1. Clone or download this repository to your local machine.

2. Install the required dependencies as mentioned above.

3. Run the `macd_trading_strategy.py` script using a Python interpreter.

4. Follow the prompts to input the stock symbol, time frame, start date, and end date for which you want to analyze the trading strategy.

5. The script will generate buy and sell signals based on the MACD crossover strategy and plot the stock's price along with the buy and sell points.

## Example

Here's a brief example of how to use the script:

```
python macd_trading_strategy.py
```
```
Enter the stock symbol (e.g., AAPL): AAPL
Enter the time frame (1m, 2m, 5m, ...): 1d
Enter the start date (YYYY-MM-DD): 2020-01-01
Enter the end date (YYYY-MM-DD): 2023-08-01
```

The script will generate trading signals and display a plot showing the stock's price with buy (green) and sell (red) signals.
![Figure_1](https://github.com/armahmoodian/MACD-Trading-Strategy/assets/82238399/10f0a665-61d3-4efb-a771-3d366ca88772)


## Disclaimer
This code is provided for educational and informational purposes only. Trading strategies and financial decisions involve risk, and past performance is not indicative of future results. Use this code at your own risk and consider seeking professional financial advice before making any trading decisions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
