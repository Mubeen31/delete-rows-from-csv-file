import pandas as pd
import time


header_list = ['Time', 'Rank', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
bitcoin_data_file = pd.read_csv('bitcoin_data.csv', names = header_list)

i = 1
while i == 1:
    time.sleep(5)
    if bitcoin_data_file.shape[0] >= 40:
        bitcoin_data_file.drop(bitcoin_data_file.index[0:5], inplace = True)
        bitcoin_data_file.to_csv('new_file.csv')
    new_file = pd.read_csv('new_file.csv')
    print(new_file.shape[0])