import matplotlib.pyplot as plt
import urllib
import numpy as np
import datetime as dt
import time
import matplotlib.dates as mdates 
from matplotlib import style

style.use('fivethirtyeight')


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
                
#    date, Open, high_price, low_price, close, adjusted_close, volume = np.loadtxt(stock_data,
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
  

    ax1.plot_date(date, close, '-', label = 'Closing Price')
    ax1.plot_date(date, volume, '-', label = 'Volume')  

    ax1.plot([],[], linewidth = 5, label = 'loss', color = 'r', alpha = 0.5)
    ax1.plot([],[], linewidth = 5, label = 'gain', color = 'g', alpha = 0.5)
    
    
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        ax1.grid(True)#, color = 'r', linestyle = '-')
    
#    ax1.xaxis.label.set_color('c')
#    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0,100,200,300,400,500,600,700])
    
    ax1.spines['left'].set_color('c')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.tick_params(axis = 'x', colors = '#514e4e')

    ax1.fill_between(date,close,close[0],where=(close>close[0]),alpha = 0.5,
                     facecolor = '#88ce36')
#    print(close[0])
#    print(adjusted_close[0]) 
#    print(Open[0])                
    ax1.fill_between(date,close,close[0],where=(close<close[0]),alpha = 0.5,
                     facecolor = 'r')  
    ax1.axhline(close[0],color = 'k', linewidth = '3' )
    
    
    
    plt.xlabel('date')
    plt.ylabel('closing price')
    plt.title('Stock')
    plt.legend()
    plt.subplots_adjust(left = 0.09, bottom = 0.20, right = 0.90, top = 0.93,
                        wspace = 0.2, hspace = 0)
    plt.show()
    
    
graph_data('Ebay')    