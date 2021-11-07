# SpotDraft
To run server on local: 
python manage.py runserver

- MUST load planets and movies from the JSON API provided by https://swapi.dev/
Used fixture to load data - planets.json and films.json (provided by Swapi)
python manage.py loaddata <fixturename>

- MUST expose list APIs - one for movies and one for planets
Movies: GET http://127.0.0.1:8000/api/movies/
Planets: GET http://127.0.0.1:8000/api/planets/

- MUST expose APIs to add a movie and planet as a favorite
Movies: PUT http://127.0.0.1:8000/api/movies/<pk>/favorite
Body: JSON :
{
	"is_favorite":true
}
Planets: PUT http://127.0.0.1:8000/api/planets/<pk>/favorite
Body: JSON :
{
	"is_favorite":true
}

- The favorite API should also allow setting a custom title/name to the movie/planet
Movies: PUT http://127.0.0.1:8000/api/movies/<pk>/favorite
Body: JSON :
{
	"custom_name":"test"
}
Planets: PUT http://127.0.0.1:8000/api/planets/<pk>/favorite
Body: JSON :
{
	"custom_name":"test"
}

- The planet list API must return the name, created, updated, URL, and is_favorite fields
Response:
{
        "id": 4,
        "name": "Hoth",
        "custom_name": "",
        "created": "2014-12-10T11:39:13.934000Z",
        "edited": "2014-12-20T20:58:18.423000Z",
        "url": "https://swapi.dev/api/planets/4",
        "is_favorite": false
    }

- The movies list API must return the title, release_date, created, updated, URL and is_favorite fields
Response:
{
        "id": 3,
        "title": "Return of the Jedi",
        "custom_title": "",
        "created": "2014-12-18T10:39:33.255000Z",
        "edited": "2014-12-20T09:48:37.462000Z",
        "release_date": "1983-05-25",
        "url": "https://swapi.dev/api/films/3",
        "is_favorite": false
    }
    
- Additionally, the list APIs must support searching by title/name
GET http://127.0.0.1:8000/api/movies/?search=Attack
GET http://127.0.0.1:8000/api/planets/?search=Tatooine
