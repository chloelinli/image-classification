# import statements
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


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
    #   3414 canceled (math and code checks out -> unneeded now)
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
    transacSpent = transac.aggregate({
        'Price':'sum', 'QuantitySold':'sum'}).reset_index()
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
focusing on time of month/year and total sales
"""
def productSales(data):

    # group and aggregate data
    sales = data.groupby(['Year-Month', 'ProductNo', 'ProductName'])
    salesPerMonth = data.groupby(['Year-Month'])
    products = data.groupby(['ProductNo', 'ProductName'])


    """
    best time of year for sales/purchases
    line to show quantity of items purchases

    most sales and income september-november -> leading to holiday season
    least sales december 2019 -> not enough data? compared to december 2018
    least sales february and april -> not around or leading to anything?
    ---
    rename line trace to Quantity
    rename axes
    change colors?
    show ticks for all x-axis values
    """
    monthlySales = salesPerMonth.aggregate({'Quantity':'sum', 'FinalPrice':'sum'}).sort_values(['Year-Month']).reset_index()
    maxSales = monthlySales['FinalPrice'].max()
    msPlot = px.bar(monthlySales, x='Year-Month', y='FinalPrice', range_x=['2018-12', '2019-12'], range_y=[0, maxSales])
    msPlot.add_trace(go.Line(x=monthlySales['Year-Month'], y=monthlySales['Quantity']))
    msPlot.show()

    
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


"""
desc
"""
def m2():
    y = 2
    # group and aggregate data

    # graph


"""
desc
"""
def m3():
    z = 3
    # group and aggregate data

    # graph


if __name__ == '__main__':
    main()