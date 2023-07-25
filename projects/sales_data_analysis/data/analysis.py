# import statements
import pandas as pd

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
new column for final price of quantity * price
"""
def transforming(data):

    # split Date into Year, Month, and Day columns
    index = data.columns.get_loc('Date')
    temp = data['Date'].str.split("-", expand=True).astype('int')
    temp.columns = ['Year', 'Month', 'Day']
    data.insert(index+1, 'Year', temp['Year'])
    data.insert(index+2, 'Month', temp['Month'])
    data.insert(index+3, 'Day', temp['Day'])

    # add new column for items actually bought -> canceled items as 0
    index = data.columns.get_loc('Quantity')
    temp = data[['TransactionNo', 'Quantity']]
    temp.insert(2, 'QuantitySold', temp['Quantity'])
    temp.loc[temp['TransactionNo'].str[0] == 'C', 'QuantitySold'] = 0
    data.insert(index+1, 'QuantitySold', temp['QuantitySold'])

    # add column for quantity x price
    index = data.columns.get_loc('QuantitySold')
    data.insert(index+1, 'FinalPrice', data['Price']*data['QuantitySold'])
    print(data)
    
    return data


"""
this method contains data analysis for this project.
questions:
"""
def analysis(data):

    """group transactions - TransactionNo/total lines"""
    # 23204 total transactions, 19790 completed transactions
    #   3414 canceled, math and code checks out -> unneeded now
    noncanceled = data[data['QuantitySold'] > 0]
    transac = noncanceled.groupby(['TransactionNo'])

    # total number of transactions
    #print(transac.count())

    # total spent per transaction
    # what is the total number of sales?
    transacSpent = transac.aggregate({
        'Price':'sum','QuantitySold':'sum'}).reset_index()
    #print(transacSpent)


    """time of purchases - total lines/Date/ProductNo"""
    # what is the average sales per month?
    # time of month/year of most purchases
    # sales per item per month?


    """product quantity and sales - ProductNo/Quantity/Date"""
    products = data.groupby(['ProductNo'])

    # which products sell best?
    # which products should the company order more or less of?
    productsSold = products.aggregate({
        'QuantitySold':'sum'}).reset_index().sort_values([
            'QuantitySold'], ascending=False)
    
    # total sales/quantity sold in a year


    """customer stats - CustomerNo/ProductNo/Quantity"""
    customers = data.groupby(['CustomerNo'])

    # total orders (made in a year)?
    #print(customers.aggregate({'TransactionNo':'count'}))

    # number of times purchasing an item
    customerProduct = data.groupby(['CustomerNo', 'ProductNo'])
    #print(customerProduct.aggregate({'ProductNo':'count'}))

if __name__ == '__main__':
    main()