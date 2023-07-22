# import statements
import pandas as pd
import numpy as np

def main():
    path = 'projects/sales_data_analysis/data'
    sales_data = pd.read_csv(path+'/Sales_Transaction_reformatted.csv')

    # preprocess data - unnecessary due to no real action
    #sales_data = preprocessing(sales_data)

    # transform data - add new columns
    sales_data = transforming(sales_data)

    # analyze data
    analysis(sales_data)


"""
data preprocessing:
check missing values
def preprocessing(data):

    # check missing values
    null_val = data.isnull().sum()
    #print(null_val)
    # 55 missing values in CustomerNo
    #print(sales_data[sales_data['CustomerNo'].isnull()])
    # missing values include both completed and canceled orders - keep

    return data
"""


"""
data transformation:
splitting columns as needed
date into year/month,day
new column to display non-negative quantity bought
"""
def transforming(data):
    # split Date into Year, Month, and Day columns
    temp = data['Date'].str.split("-", expand=True).astype('int')
    temp.columns = ['Year', 'Month', 'Day']
    data.insert(2, 'Year', temp['Year'])
    data.insert(3, 'Month', temp['Month'])
    data.insert(4, 'Day', temp['Day'])

    # add new column for items actually bought -> canceled items as 0
    temp = data[['TransactionNo', 'Quantity']]
    temp.insert(2, 'ActualQuantity', temp['Quantity'])
    temp.loc[temp['TransactionNo'].str[0] == 'C', 'ActualQuantity'] = 0
    data.insert(9, 'ActualQuantity', temp['ActualQuantity'])

    return data


"""
this method contains data analysis for this project.
questions:
"""
def analysis(data):
    print()

if __name__ == '__main__':
    main()