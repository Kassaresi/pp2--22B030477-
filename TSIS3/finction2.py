movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def ismorethan(string, movies):
    for i in movies:
        if i['name'] == string.capitalize():
            if i['imdb'] > 5.5:
                return True
    return False
# print(ismorethan('hitman', movies))

def allmorethan(movies):
    filmmorethan = []
    for film in movies:
        if film['imdb'] > 5.5:
            filmmorethan.append(film)
    return filmmorethan
# print(allmorethan(movies))

def searchcat(category, movies):
    films = []
    for film in movies:
        if film['category'] == category.capitalize():
            films.append(film)
    return films
# print(searchcat('Thriller', movies))

def avgscore(movies):
    avg = 0
    for film in movies:
        avg += film['imdb']
    avg /= len(movies)
    return avg
# print(avgscore(movies))
def avgscoreofcat(movies, cat):
    avg = 0
    avgmember =0
    for film in movies:
        if film['category'] == cat:
            avg += film['imdb']
            avgmember += 1
    avg = avg / avgmember
    return avg
# print(avgscoreofcat(movies, 'Thriller'))



