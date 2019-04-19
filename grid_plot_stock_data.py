import matplotlib.pyplot as plt
import urllib
import numpy as np
import matplotlib.dates as mdates 
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.ticker as mticker


style.use('fivethirtyeight')


ma_1 = 10
ma_2 = 30

def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs-lows

highs = [11,12,13,14,15]
lows = [1,2,3,4,5]

highlow = list(map(high_minus_low, highs, lows)) 
print(highlow)
    
def bytes_dates_toNum(format, encoding = 'utf-8'):
    strconverter = mdates.strpdate2num(format)
    def bytes_converter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytes_converter    
    
def graph_data(stock):
    
    figure = plt.figure(facecolor = '#f0f0f0')

    ax1 = plt.subplot2grid((6,1),(0,0), rowspan = 1, colspan = 1 )
    plt.title('Stock')
    plt.ylabel('High - Low', fontsize = 'x-small')
    ax2 = plt.subplot2grid((6,1),(1,0), rowspan = 4, colspan = 1, sharex = ax1 )
    plt.ylabel('closing price',fontsize = 'x-small')
    ax2_volume = ax2.twinx()
    ax3 = plt.subplot2grid((6,1),(5,0), rowspan = 1, colspan = 1,sharex = ax1 )
    plt.ylabel('Moving Averages',fontsize = 'x-small')
    
    
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
                                     
                                     
                                     
    x = 0
    y = len(date)
    ohlc = []
    
    while x < y:
        append_me = date[x], Open[x], high_price[x], low_price[x], close[x],adjusted_close[x],volume[x]
        ohlc.append(append_me)
        x+=1
        
    ma1 = moving_average(close, ma_1)    
    ma2 = moving_average(close, ma_2)
    start = len(date[ma_2-1:])    

    h_l = list(map(high_minus_low, high_price, low_price))
    ax1.plot_date(date[-start:], h_l[-start:], '-', label = 'H-L')    
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 4, prune = 'upper'))
    
    candlestick_ohlc(ax2,ohlc[-start:], width = 0.4, colorup = '#52b017', colordown = '#f01919') 
                     
    
    
    ax2.grid(True)
#    ax2.annotate('Drop in Prices!', (date[500],close[500]), xytext = (0.3, 0.3),
#                 textcoords = 'axes fraction', arrowprops = dict(facecolor='grey',
#                                                                 color = 'grey'))
#    bbox_props = dict(boxstyle = 'round', fc = 'w', ec = 'k', lw = 1)
#    ax2.annotate(str(close[0]), (date[0],close[0]), 
#                 xytext = (date[0]+4, close[0]), bbox = bbox_props)
    
    ax2_volume.plot([],[],'#0079a3',alpha = 0.4, label = 'Volume')
    ax2_volume.fill_between(date[-start:],0, volume[-start:],
                            facecolor = '#0079a3')    
    ax2_volume.axes.yaxis.set_ticklabels([])
    ax2_volume.grid(False)
    ax2_volume.set_ylim(0, 3*volume.max())
#    plt.xlabel('date')
#    plt.ylabel('closing price')
#    plt.title('Stock')
   #plt.legend()
   
    print(len(date), len(ma1))
   
    ax3.plot(date[-start:], ma1[-start:], linewidth = 1,
             label = (str(ma_1)+'MA'))
    ax3.plot(date[-start:], ma2[-start:], linewidth = 1,
             label = (str(ma_2)+'MA'))
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], 
                     where = (ma1[-start:] <ma2[-start:]), 
                     facecolor = 'r', edgecolor = 'r', alpha = 0.5)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], 
                     where = (ma1[-start:] > ma2[-start:]), 
                     facecolor = 'g', edgecolor = 'g', alpha = 0.5)
    
    
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))    
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins = 4, prune = 'upper'))

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.setp(ax1.get_xticklabels(), visible = False)
    plt.setp(ax2.get_xticklabels(), visible = False)
    plt.subplots_adjust(left = 0.11, bottom = 0.24, right = 0.90, top = 0.90,
                        wspace = 0.2, hspace = 0)
    
    ax1.legend()
    leg = ax1.legend(loc = 10, ncol = 2, prop = {'size':7})
    leg.get_frame().set_alpha(0.4)
    ax2_volume.legend()
    leg = ax2_volume.legend(loc = 10, ncol = 2, prop = {'size':7})
    leg.get_frame().set_alpha(0.4)
    ax3.legend()
    leg = ax3.legend(loc = 10, ncol = 2, prop = {'size':7})
    leg.get_frame().set_alpha(0.4)
    plt.show()
    figure.savefig('stock_prices.png', facecolor =figure.get_facecolor())
    
    
graph_data('Stock Prices')                           




                                       