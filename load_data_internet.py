import matplotlib.pyplot as plt
import urllib
import numpy as np
import matplotlib.dates as mdates

def bytes_dates_toNum(format, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(format)
    def bytes_converter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytes_converter    
    
def graph_data(stock):
    STOCK_PRICE_URL = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(STOCK_PRICE_URL).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Date' not in line and 'Open' not in line and 'High' not in line and 'Low' not in line and 'Adjusted_close' not in line and 'Volume' not in line:
                stock_data.append(line)
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
  

    plt.plot_date(date, close, '-', label = 'Closing Price')     
        
    plt.xlabel('date')
    plt.ylabel('closing price')
    plt.title('Interesting graph\nCheck it out')
    plt.legend()
    plt.show()
    
    
graph_data('Tesla')    