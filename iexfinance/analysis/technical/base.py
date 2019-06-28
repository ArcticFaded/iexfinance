import datetime

from iexfinance.stocks import get_historical_data


def _retrieve_data(symbol, start=None, end=None, series_type='close'):
    start = start or datetime.date(2017, 1, 1)
    end = end or datetime.date.today()
    close_only = True if series_type == 'close' else False
    data = get_historical_data(symbol, start, end, close_only=close_only)
    return data[series_type, "volume"]


def get_bollinger_bands(symbol, start=None, end=None, series_type='close'):
    data = _retrieve_data(symbol, start, end, series_type)

    # 20-day simple moving average & standard deviation
    sma_20 = data.close.rolling(window=20).mean()
    std_20 = data.close.rolling(window=20).std()

    # Calculate the bands and add to result
    data["Upper Band"] = sma_20 + 2 * std_20
    data["Lower Band"] = sma_20 - 2 * std_20

    return data
