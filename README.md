# Simpletracker

A proof of concept solution for tracking user visits.

## Getting started

Make sure you have Docker installed.

```
git clone <this repository>
cd path/to/project
docker-compose up -d
```

Visit http://localhost:8000/admin to see that it works.

### Maybe you have to do this as well

In case there are new migrations:

```
docker-compose exec app bash
python manage.py migrate
```

In case you want to sign in to the Admin app:

```
docker-compose exec app bash
python manage.py createsuperuser
```
