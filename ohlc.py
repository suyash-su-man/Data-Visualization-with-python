import matplotlib.pyplot as plt
import urllib
import numpy as np
import datetime as dt
import time
import matplotlib.dates as mdates 
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style
print(plt.style.available)

style.use('ggplot')

def bytes_dates_toNum(format, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(format)
    def bytes_converter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytes_converter    
    
def graph_data(stock):
    
    figure = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    
    STOCK_PRICE_URL = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(STOCK_PRICE_URL).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Date' not in line and 'Open' not in line and 'High' not in line and 'Low' not in line and 'Adjusted_close' not in line and 'Volume' not in line:
                stock_data.append(line)
                
#    date, Open, high_price, low_price, close, adjusted_close,
#    volume = np.loadtxt(stock_data,
#                      delimiter = ',', unpack = True)            
#     
#    date_converter = np.vectorize(dt.datetime.fromtimestamp)
#    date = date_converter(date)
           
            
    date, Open, high_price, low_price, close, adjusted_close, volume = np.loadtxt(stock_data,
                        delimiter = ',', unpack = True,
                        converters = {0: bytes_dates_toNum('%Y-%m-%d')})
                                     # %Y = full year 2019
                                     # %y = partial year 19
                                     # %m = number month
                                     # %d = number day
                                     # %H = hours
                                     # %M = minutes
                                     # %S = seconds
                                     # 12-06--2014
                                     # %d-%m-%Y
    x = 0
    y = len(date)
    ohlc = []
    
    while x < y:
        append_me = date[x], Open[x], high_price[x], low_price[x], close[x],adjusted_close[x],volume[x]
        ohlc.append(append_me)
        x+=1
    candlestick_ohlc(ax1,ohlc, width = 0.4, colorup = '#52b017', colordown = '#f01919')     
     

#    ax1.plot(date,close)
#    ax1.plot(date,volume)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))    
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    ax1.annotate('Drop in Prices!', (date[500],close[500]), xytext = (0.3, 0.3),
                 textcoords = 'axes fraction', arrowprops = dict(facecolor='grey',
                                                                 color = 'grey'))
    
    #font_dict = {'family':'serif','size': 10, 'color':'darkred'}   
    #ax1.text(date[10], close[1], 'Stock prices', fontdict = font_dict)
    bbox_props = dict(boxstyle = 'round', fc = 'w', ec = 'k', lw = 1)
    ax1.annotate(str(close[0]), (date[0],close[0]), 
                 xytext = (date[0]+4, close[0]), bbox = bbox_props)
    
    plt.xlabel('date')
    plt.ylabel('closing price')
    plt.title('Stock')
   #plt.legend()
    plt.subplots_adjust(left = 0.11, bottom = 0.24, right = 0.90, top = 0.90,
                        wspace = 0.2, hspace = 0)
    plt.show()
    
    
graph_data('Ebay')                                 