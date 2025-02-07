import pandas as pd
transactions_data = pd.DataFrame({
    'user_id': [1, 2, 3, 1, 4, 5, 2, 3, 4, 1, 5, 2],
    'amount': [500, 2000, 1500, 800, 5000, 750, 3000, 1200, 3500, 200, 250, 900],
    'transaction_type': ['debit', 'credit', 'debit', 'debit', 'credit', 'debit', 'credit', 'debit', 'credit', 'debit', 'debit', 'credit'],
    'timestamp': pd.to_datetime([
        '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02', '2024-01-03',
        '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05', '2024-01-05', '2024-01-06'
    ])
})


percentile_95 = transactions_data['amount'].quantile(0.95)
mean_per_user = transactions_data.groupby('user_id')['amount'].mean()
high_value_users = mean_per_user[mean_per_user > percentile_95].index.tolist()


percentile_90 = transactions_data['amount'].quantile(0.90)
large_transactions = transactions_data[transactions_data['amount'] > percentile_90]
large_transactions_count = large_transactions.groupby(['user_id', large_transactions['timestamp'].dt.date]).size()
users_with_large_transactions = large_transactions_count[large_transactions_count >= 3].index.get_level_values(0).unique()


active_day = transactions_data.groupby(transactions_data['timestamp'].dt.date).size().idxmax()

high_value_users, users_with_large_transactions, active_day
