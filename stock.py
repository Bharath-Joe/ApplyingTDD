class ShareSaleException(Exception):
    """Exception raised when trying to sell more shares than there are"""

def createStockPortfolio():
    stockPortfolio = {}
    return stockPortfolio

def isEmpty(stockPortfolio):
    if len(stockPortfolio) == 0:
        return True
    return False 

def tickerCount(stockPortfolio):
    return len(stockPortfolio)

def addShares(stockPortfolio, ticker, shares):
    if ticker in stockPortfolio.keys():
        stockPortfolio[ticker] += shares
    else:
        stockPortfolio[ticker] = shares
    return stockPortfolio

def sellShares(stockPortfolio, ticker, shares):
    if stockPortfolio[ticker] >= shares:
        stockPortfolio[ticker] -= shares
        return stockPortfolio
    else:
        raise ShareSaleException

def checkShares(stockPortfolio, ticker):
    return stockPortfolio[ticker]

def atLeastOneStock(stockPortfolio):
    for key in stockPortfolio.keys():
        if stockPortfolio[key] < 1:
            stockPortfolio.pop(key)
    return stockPortfolio

def meetsMinReq(stockPortfolio):
    for key in stockPortfolio:
        if stockPortfolio[key] < 1:
            return False
    return True
