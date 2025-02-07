import pandas as pd
movies_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10, 1, 3, 5, 7, 9],
    'movie_id': [101, 102, 103, 104, 105, 101, 102, 103, 104, 105, 106, 107, 108, 106, 107, 108, 109, 110],
    'rating': [5, 4, 3, 5, 2, 4, 3, 5, 4, 5, 3, 2, 4, 5, 4, 3, 2, 1],
    'timestamp': pd.to_datetime([
        '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06',
        '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12',
        '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'
    ])
})


rating_count = movies_data.groupby('movie_id').size()
average_rating = movies_data.groupby('movie_id')['rating'].mean()
top_movies = average_rating[rating_count > 50].sort_values(ascending=False).head(5)




ratings_per_day = movies_data.groupby(['user_id', movies_data['timestamp'].dt.date]).size()
average_ratings_per_user = ratings_per_day.groupby('user_id').mean()
max_avg_user = average_ratings_per_user.idxmax()

top_movies, max_avg_user
