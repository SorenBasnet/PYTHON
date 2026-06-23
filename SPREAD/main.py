import numpy as np
import yfinance as yf
import pandas as pd

if __name__ == "__main__":

    TICKER_A = "GC"
    START = "1979-01-01"
    END = "2026-06-23"

    data = yf.download([TICKER_A], start=START, end=END)["Adj Close"]

    #df = data[[TICKER_A]].dropna()

    print(data)


