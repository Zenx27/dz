import pandas as pd
import numpy as np


sales_data = pd.DataFrame({
    'product_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'category': ['Электроника', 'Электроника', 'Одежда', 'Одежда', 'Книги', 'Книги', 'Игрушки', 'Игрушки'],
    'price': [15000, 12000, np.nan, 2500, 500, np.nan, 800, 1000],
    'quantity_sold': [10, 15, 20, 50, 100, 80, 30, 25],
    'revenue': [150000, 180000, np.nan, np.nan, 50000, np.nan, np.nan, np.nan]
})


sales_data['price'] = sales_data.groupby('category')['price'].transform(lambda x: x.fillna(x.mean()))


sales_data['revenue'] = sales_data['price'] * sales_data['quantity_sold']


category_revenue = sales_data.groupby('category')['revenue'].sum()
top_category = category_revenue.idxmax()


sales_data, top_category
