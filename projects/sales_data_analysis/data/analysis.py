# import statements
import pandas as pd
import numpy as np

def main():
    path = 'projects/sales_data_analysis/data'
    sales_data = pd.read_csv(path+'/Sales_Transaction_reformatted.csv')

    """
    data preprocesing:
    split columns as needed
    check missing values
    """

    # split Date into Year, Month, and Day columns
    temp = sales_data['Date'].str.split("-", expand=True).astype('int')
    temp.columns = ['Year', 'Month', 'Day']
    sales_data.insert(2, 'Year', temp['Year'])
    sales_data.insert(3, 'Month', temp['Month'])
    sales_data.insert(4, 'Day', temp['Day'])

    # check missing values
    null_val = sales_data.isnull().sum()
    #print(null_val)
    # 55 missing values in CustomerNo
    #print(sales_data[sales_data['CustomerNo'].isnull()])
    # missing values include both completed and canceled orders

    # add new column for items actually bought -> canceled items as 0
    temp = sales_data[['TransactionNo', 'Quantity']]
    temp.insert(2, 'ActualQuantity', temp['Quantity'])
    temp.loc[temp['TransactionNo'].str[0] == 'C', 'ActualQuantity'] = 0
    sales_data.insert(9, 'ActualQuantity', temp['ActualQuantity'])   

if __name__ == '__main__':
    main()