
from   pandas.io.data import DataReader
from   datetime import datetime
import pylab
import matplotlib


def plotStock(symbol, startDate, endDate):
    """returns a plot of stock (symbol) between startDate and endDate
    symbol: String, stock ticker symbol
    startDate, endDate = tuple(YYYY, MM, DD)
    """
    company = symbol
    
    sYear, sMonth, sDay = startDate
    eYear, eMonth, eDay = endDate

    start = datetime(sYear, sMonth, sDay)
    end   = datetime(eYear, eMonth, eDay)
    
    data = DataReader(company,  "yahoo", start, end)
    
    closingVals = data["Adj Close"]
    
    #convert to matplotlib format
    dates = [i for i in data.index]
    dates = matplotlib.dates.date2num(dates)
    
    pylab.ylim([0, int(max(closingVals)*1.2)])
    
    pylab.plot_date(dates, closingVals, label = symbol, xdate = True,
                    ydate=False, linestyle = '-')
    
    pylab.legend()
    pylab.show()


#example
plotStock("goog", (2004, 05, 01), (2014, 2, 10))
        

