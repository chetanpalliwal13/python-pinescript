from pinescript import *
from tradingView import *

# @version=4
study("security Function Test", overlay=True)

MSFT_Close = security("MSFT", "D", close)
MSFT_Open = security("MSFT", "D", open)

MSFT_High = security("MSFT", "D", high)
MSFT_Low = security("MSFT", "D", low)


#print(iff(lastup < lastdown, color.red , color.green))
