!pip install yfinance
import pandas as pd
import yfinance as yf

symbols_table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                             header=0)[0]
symbols_table_new = symbols_table.set_index("Symbol")
symbols_table_new["Ticker Yahoo"] = symbols_table_new.index.str.replace(".", "-", regex=False)
symbols = list(symbols_table_new.loc[:, "Ticker Yahoo"])
sp500 = yf.download(tickers = symbols,
                        start="2019-01-01",
                        group_by = "column",
                        interval = "1d",
                        auto_ajust = True,
                        threads = True,
                           )