# import statements
import pandas as pd
import plotly.express as px
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
"""
"""
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
    temp1 = data['Date'].str.split("-", expand=True)
    temp.columns = temp1.columns = ['Year', 'Month', 'Day']
    data.insert(index+1, 'Year', temp['Year'])
    data.insert(index+2, 'Month', temp['Month'])
    data.insert(index+3, 'Day', temp['Day'])
    data.insert(index+4, 'Year-Month', temp1['Year']+'-'+temp1['Month'])

    # add new column for items actually bought -> canceled items as 0
    index = data.columns.get_loc('Quantity')
    temp = data[['TransactionNo', 'Quantity']]
    temp.insert(2, 'QuantitySold', temp['Quantity'])
    temp.loc[temp['TransactionNo'].str[0] == 'C', 'QuantitySold'] = 0
    data.insert(index+1, 'QuantitySold', temp['QuantitySold'])

    # add column for quantity x price
    index = data.columns.get_loc('QuantitySold')
    data.insert(index+1, 'FinalPrice', data['Price']*data['QuantitySold'])
    
    return data


"""
this method contains data analysis for this project.
questions:
"""
def analysis(data):

    # 23204 total transactions, 19790 completed transactions
    #   3414 canceled, math and code checks out -> unneeded now
    noncanceled = data[data['QuantitySold'] > 0]

    
    """product quantity and sales - ProductNo/Quantity/Date"""
    """time of purchases - total lines/Date/ProductNo"""
    productSales(noncanceled)
    

    """group transactions - TransactionNo/total lines"""
    transac = noncanceled.groupby(['TransactionNo'])

    # total number of transactions
    #print(transac.count())

    # total spent per transaction
    # what is the total number of sales?
    transacSpent = transac.aggregate({'Price':'sum','QuantitySold':'sum'}).reset_index()
    #print(transacSpent)


    """customer stats - CustomerNo/ProductNo/Quantity"""
    customers = noncanceled.groupby(['CustomerNo'])

    # total orders (made in a year)?
    #print(customers.aggregate({'TransactionNo':'count'}))

    # number of times purchasing an item
    customerProduct = noncanceled.groupby(['CustomerNo', 'ProductNo'])
    #print(customerProduct.aggregate({'ProductNo':'count'}))


"""
this method contains the analysis of product sales
focusing on time of month/year and total sales"""
def productSales(data):

    # group and aggregate data
    daily = data.groupby(['Date', 'ProductNo', 'ProductName', 'Price'])
    sales = data.groupby(['Year-Month', 'ProductNo', 'ProductName'])
    products = data.groupby(['ProductNo', 'ProductName'])

    """
    time of year of most purchases
    sales per item per month?

    ->
    total sales per month
    interactive for products
    best month for sales?
    """
    monthlySales = sales.aggregate({'Quantity':'sum'}).reset_index()
    maxQuantity = monthlySales['Quantity'].max()
    msPlot = px.bar(monthlySales, x='Year-Month', y='Quantity',
                 range_x=['2018-12', '2019-12'], animation_frame='ProductNo',
                 hover_name='Year-Month', range_y=[0, maxQuantity])
    #msPlot.show()


    """
    best time of month for product sales and discounts

    ->
    product sales every day of month
    different color for different price - drop down menu for price
    quantity vs price
    """
    dailyPurchases = daily.aggregate({'Quantity':'sum'}).reset_index()

    # boolean column for price comparison
    prices = products.aggregate(maxPrice=('Price', 'max'), minPrice=('Price', 'min')).reset_index()
    prices['Discounted'] = np.where(prices['maxPrice'] == prices['minPrice'], False, True)
    # add boolean to daily purchases
    dailyPurchases['Discounted'] = np.where(dailyPurchases['Price'] > 7, True, False)
    for r in dailyPurchases.itertuples():
        pn = r.ProductNo
        p = r.Price

        mp = prices.loc[prices['ProductNo'] == pn, 'maxPrice']
        
        dailyPurchases['Discounted'].at[r.Index] = (p != mp)
    
    # add column for different prices
    dailyPurchases['PriceChange'] = 0
    # if not discounted, 0, else +1 for each discount
    # loop through prices
    for r in prices.itertuples():
        # for each ProductNo in prices
        pn = r.ProductNo
        # new dataframe containing individual ProductNo
        temp = dailyPurchases.loc[dailyPurchases['ProductNo'] == pn]
        # group by Price, aggregate count, sort by descending Price, reset index
        temp = temp.groupby(['Price'])
        temp = temp.aggregate({'Quantity':'count'})
        temp = temp.sort_values('Price', ascending=False).reset_index()
        # for each row in aggregate, +1 to previous in dailyPurchases
        # loop through aggregate
        temp['PriceChange'] = 0
        for i in temp.itertuples():
            index = i.Index
            temp['PriceChange'].at[i.Index] = index
        
        for i in dailyPurchases.itertuples():
            if i.ProductNo != pn:
                continue

            p = i.Price

            pc = temp.loc[temp['Price'] == p, 'PriceChange']

            dailyPurchases['PriceChange'].at[i.Index] = pc
    
    dpPlot = px.line(dailyPurchases, x='Date', y='Quantity', animation_frame='ProductNo', color='PriceChange', range_x=['2018-12-01', '2019-12-31'])
    dpPlot.show()
    """
    """

    # which products sell best?
    # which products should the company order more or less of?
    productsSold = products.aggregate({
        'QuantitySold':'sum'}).reset_index().sort_values([
            'QuantitySold'], ascending=False)
    
    # total sales/quantity sold in a year

    yearMonth = data.groupby(['Year', 'Month'])

    # what is the average sales per month?
    avgSales = yearMonth.aggregate({'FinalPrice':'mean'})
    #print(avgSales['FinalPrice'].round(decimals=2))


def m2():
    y = 2
    # group and aggregate data

    # graph

def m3():
    z = 3
    # group and aggregate data

    # graph

if __name__ == '__main__':
    main()