import pandas as pd
import matplotlib.pyplot as plt

xls = pd.read_excel("test_data_file.xlsx", usecols = 5)
xls = xls.dropna(how='any')
xls = xls.reset_index(drop=True)
xls.columns = ['a','b','c','d','e','f']
#name columns to easily take out unuseful data

xls = xls.drop('c', axis =1)
xls = xls.drop('d', axis =1)
xls = xls.drop('f', axis =1)
#take out every data except 2017

xls = xls.T.drop(0, axis=1)
#twist the file to a useable file 

xls.T.to_csv('test.csv', header=False, index=False, encoding="cp949")