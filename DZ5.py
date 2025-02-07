import pandas as pd
resumes_data = pd.DataFrame({
    'resume_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Иван', 'Мария', 'Алексей', 'Сергей', 'Ольга', 'Николай', 'Анна', 'Павел', 'Юлия', 'Максим'],
    'email': ['ivan@mail.com', 'maria@mail.com', 'alex@mail.com', 'sergey@mail.com', 'olga@mail.com',
              'nikolay@mail.com', 'anna@mail.com', 'pavel@mail.com', 'yulia@mail.com', 'max@mail.com'],
    'phone': ['+79110001111', '+79110002222', '+79110003333', '+79110004444', '+79110005555',
              '+79110006666', '+79110007777', '+79110008888', '+79110009999', '+79110000000'],
    'experience_years': [2, 5, 1, 10, 7, 3, 0, 8, 6, 12],
    'skills': ['Python, SQL', 'Java, Spring', 'HTML, CSS, JavaScript', 'C++, Linux', 'Go, Docker',
               'Python, Machine Learning', 'Senior Developer, Management', 'JavaScript, React',
               'C#, .NET', 'Data Science, AI']
})


resumes_data_clean = resumes_data.drop_duplicates(subset=['email', 'phone'])


senior_candidates = resumes_data[(resumes_data['experience_years'] < 1) & resumes_data['skills'].str.contains('Senior Developer')]


experienced_candidates = resumes_data[resumes_data['experience_years'] > 5]
skills_list = experienced_candidates['skills'].str.split(', ').explode()
top_10_skills = skills_list.value_counts().head(10)

resumes_data_clean, senior_candidates, top_10_skills
