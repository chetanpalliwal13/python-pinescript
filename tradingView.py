import yfinance as yf
import pandas as pd
import numpy as np
import time
import re
import random
import datetime
from threading import Timer
from contextvars import ContextVar
from pinescript import *

#import matplotlib.pyplot as plt

close = ContextVar("close")
open = ContextVar("open")
high = ContextVar("high")
low = ContextVar("low")
volume = ContextVar("volume")

def security(symbol, resolution, expression, gaps=None, lookahead=None):
    ohlcvMmapper = {"open":"Open", "high":"High", "low":"Low", "close":"Close", "volume":"Volume"}
    symbolLen = len(symbol)
    if symbolLen<0:
        raise Exception("No Tick Identified")
    expression = expression.get()
    interval = int("0" if len(re.findall(r'\d', expression))==0 else re.findall(r'\d', expression)[0])
    #print("Interval is = {}".format(type(interval)))
    whatToGet = re.findall(r'[A-Za-z]+', expression)[0]
    #print("whatToGet is = {} and type = {}".format(whatToGet, type(whatToGet)))
    if interval<0:
        raise Exception("Future Date is not possible to display. Please Change {} in {}".format(interval, whatToGet))

    today = datetime.datetime.now()
    delta = datetime.timedelta(days = interval)
    days = (today - delta).strftime("%Y-%m-%d")

    getHis = yf.download(symbol, days, today.strftime("%Y-%m-%d"))
    #print(getHis)
    if interval==0:
        whatToReturn = round(getHis.tail(1)[ohlcvMmapper[whatToGet]][0], 2)
    else:
        whatToReturn = round(getHis.tail(interval)[ohlcvMmapper[whatToGet]][0], 2)
	
    return whatToReturn
