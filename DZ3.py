import pandas as pd
orders_data = pd.DataFrame({
    'customer_id': [101, 102, 103, 101, 104, 105, 102, 103, 106, 107, 101, 108],
    'order_date': pd.to_datetime([
        '2023-05-01', '2023-06-01', '2023-07-01', '2024-01-01', '2024-02-15', '2024-02-20',
        '2023-08-10', '2024-03-05', '2024-03-15', '2024-04-01', '2023-09-20', '2023-10-10'
    ]),
    'order_amount': [15000, 20000, 10000, 5000, 7000, 8000, 25000, 12000, 18000, 20000, 16000, 9000]
})


previous_year = pd.to_datetime('2023-01-01')
current_year = pd.to_datetime('2024-01-01')
customers_previous_year = set(orders_data[orders_data['order_date'] < current_year]['customer_id'])
customers_current_year = set(orders_data[orders_data['order_date'] >= current_year]['customer_id'])
lost_customers = customers_previous_year - customers_current_year


orders_count = orders_data.groupby('customer_id').size()
one_order_percentage = (orders_count[orders_count == 1].count() / len(orders_count)) * 100


active_customers = orders_count[orders_count > 3].index
active_orders = orders_data[orders_data['customer_id'].isin(active_customers)]
active_orders = active_orders.sort_values(by=['customer_id', 'order_date'])
active_orders['time_diff'] = active_orders.groupby('customer_id')['order_date'].diff().dt.days
median_time_between_orders = active_orders['time_diff'].median()

lost_customers, one_order_percentage, median_time_between_orders
