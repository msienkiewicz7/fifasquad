# Python: Django Application

## Data source
FIFA 2019 players database: https://www.kaggle.com/karangadiya/fifa19

## App features
- Search within the database with a text query
- Display the players that match the search criteria ( the “searchable”
attributes are: name, club & nationality )
- Team Builder

## Team Builder
- Build your team based on your budget given in millions €

Once the budget defined, the tool shows a list of 11 players
that constitute the best team for this specific budget .
Best player is defined from their overall score.

## TODO
- enable search ignoring foregin characters

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
