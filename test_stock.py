import pytest
import stock

def setUp():
    sp = stock.createStockPortfolio()
    return sp
    
# 2.1
def test_Create():
    assert stock.createStockPortfolio() == {}

# 2.2
def test_isEmpty():
    sp = setUp()
    assert stock.isEmpty(sp) == True

# 2.3
def test_stock_count():
    sp = setUp()
    stock.addShares(sp, "GMR", 5)
    stock.addShares(sp, "RMLX", 10)
    assert stock.tickerCount(sp) == 2

# 2.4
def test_update_portfolio():
    sp = setUp()
    stock.addShares(sp, "RMLX", 10)
    stock.addShares(sp, "RMLX", 12)
    assert stock.checkShares(sp, "RMLX") == 22

# 2.5
def test_sell_shares():
    sp = setUp()
    stock.addShares(sp, "RMLX", 10)
    stock.sellShares(sp, "RMLX", 6)
    assert stock.checkShares(sp, "RMLX") == 4

# 2.6
def test_shares_count():
    sp = setUp()
    stock.addShares(sp, "GMR", 7)
    assert stock.checkShares(sp, "GMR") == 7

# 2.7
def test_shares_less_than_one():
    sp = setUp()
    stock.addShares(sp, "GMR", 10)
    stock.addShares(sp, "APPL", 0)
    stock.addShares(sp, "TSLA", 2)
    assert stock.meetsMinReq(sp) == False

def test_keep_owned_symbols():
    sp = setUp()
    stock.addShares(sp, "GMR", 10)
    stock.addShares(sp, "APPL", 0)
    stock.addShares(sp, "TSLA", 2)
    stock.atLeastOneStock(sp)
    assert stock.meetsMinReq(sp) == True

# 2.8
def test_sell_shares_negative():
    sp = setUp()
    stock.addShares(sp, "RMLX", 10)
    with pytest.raises(stock.ShareSaleException):
        stock.sellShares(sp, "RMLX", 12)

