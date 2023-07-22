# import statements
import pandas as pd
import numpy as np

def main():
    path = 'projects/sales_data_analysis/data'
    df = pd.read_csv(path+'/Sales_Transaction_reformatted.csv')

    # split Date into Year, Month, and Day columns
    temp = df['Date'].str.split("-", expand=True).astype('int')
    temp.columns = ['Year', 'Month', 'Day']
    df.insert(2, 'Year', temp['Year'])
    df.insert(3, 'Month', temp['Month'])
    df.insert(4, 'Day', temp['Day'])

if __name__ == '__main__':
    main()