#!/usr/bin/env python
from argparse import ArgumentParser 
import urllib2
from bs4 import BeautifulSoup

currentrelease = 'Get Earnings & Ex-Div Dates 1.0'





def getArgs():
    parser = ArgumentParser(description = currentrelease)
    parser.add_argument("-t", "--ticker", required=False, dest="ticker", help="ticker for lookup", metavar="ticker")
    parser.add_argument("-x", "--exdiv", required=False, dest="exdiv", help="get ex-div date", action="store_true")
    parser.add_argument("-e", "--earnings", required=False, dest="earnings", help="get earnings date", action="store_true")
    args = parser.parse_args()
    return args


def exdiv(ticker):
    baseurl = 'https://finance.yahoo.com/quote/'
    endurl = ticker
    url = baseurl + ticker
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    exdivdate = soup.find_all("span")
    return exdivdate[40].text

def earnings(ticker):
    baseurl = 'https://finance.yahoo.com/quote/'
    endurl = ticker
    url = baseurl + ticker
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read(), "html5lib")
    earningsdate = soup.find_all("span")
    return earningsdate[37].text

#----------------------------------------------------------------------
if __name__ == "__main__":
	myargs = getArgs()

ticker = myargs.ticker


print currentrelease
print "Symbol: " + str(ticker)
if myargs.earnings is True:
    earningsdate = earnings(ticker)
    print "Earnings date: " + str(earningsdate)

if myargs.exdiv is True:
    exdivdate = exdiv(ticker)
    print "Ex-Div date: " + str(exdivdate)
