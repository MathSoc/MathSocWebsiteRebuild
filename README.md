## Mathsoc Website

A remake of the MathSoc website (mathsoc.uwaterloo.ca)

To setup:

- Change .envexample to .env and modify the variables as neededA
- Get the keys needed in keys_and_pws(see its README.md)
- run `docker-compose up` (first time will take a while, but after that it should be  much faster)
- run `docker-compose run web python manage.py migrate`
- run `docker-compose run web python manage.py collectstatic` 
- run `docker-compose run web python manage.py loaddata db_basedata.json` 

To run:
- run `docker-compose up`
