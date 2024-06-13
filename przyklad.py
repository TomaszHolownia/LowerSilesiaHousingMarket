import requests
from bs4 import BeautifulSoup
import json
url = 'https://m.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
movies = []
for movie_tag in soup.find_all('div', class_='movie'):
    title = movie_tag.find('h2').text
    genre = movie_tag.find('span', class_='genre').text
    rating = movie_tag.find('span', class_='rating').text
    movie_data = {
        'title': title,
        'genre': genre,
        'rating': rating
    }
    movies.append(movie_data)
with open('movies.json', 'w') as file:
    json.dump(movies, file)


with open('movies.json', 'r') as file:
    data = json.load(file)
ratings = [float(movie['rating']) for movie in data]
average_rating = sum(ratings) / len(ratings)
genres = [movie['genre'] for movie in data]
most_common_genre = max(set(genres), key=genres.count)
print(f'Średnia ocena filmów: {average_rating}')
print(f'Najczęściej występujący gatunek filmowy: {most_common_genre}')