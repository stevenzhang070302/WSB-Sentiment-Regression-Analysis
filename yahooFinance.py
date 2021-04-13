#In progress, Just some code I found/worked on. Have not tested.

from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd
# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list=['GME']
today = date.today()
# We can get data by our choice by giving days bracket
start_date= "2021–01–01"
end_date="2021–03–20"
files=[]
def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname= ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)

# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv('./data/'+filename+'.csv')
    #This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
    for tik in ticker_list:
        getData(tik)
        for i in range(0,11):
            df1= pd.read_csv('./data/'+ str(files[i])+'.csv')
            print(df1.head())