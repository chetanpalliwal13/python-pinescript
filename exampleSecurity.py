from pinescript import *
from tradingView import *

# @version=4
study("security Function Test", overlay=True)

MSFT_Close = security("MSFT", "D", "close")
MSFT_Close30 = security("MSFT", "D", "close[30]")

MSFT_High_365 = security("MSFT", "M", "high[365]")
MSFT_Low_365 = security("MSFT", "Y", "low[365]")


#print(iff(lastup < lastdown, color.red , color.green))