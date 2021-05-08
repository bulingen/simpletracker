# Simpletracker

A proof of concept solution for tracking user visits.

## Getting started

1. Make sure you have Docker installed.
1. Get and run the application:
   ```
   git clone <this repository>
   cd path/to/project
   docker-compose up -d
   ```
1. Run migrations:
   ```
   docker-compose exec app bash
   python manage.py migrate
   ```
1. Optional, in case you want to access the admin app:
   ```
   docker-compose exec app bash
   python manage.py createsuperuser
   ```
1. Visit http://localhost:8000/admin to see that it works.

## How to use the application

1. Make sure the application is running.
1. Get the log output going:
   ```
   docker-compose logs -f
   ```
1. Visit a tracked page: http://localhost:8000/contact
1. Check the log output and observe that a `PAGEVIEW ...` line is printed.
1. Get a report of previous visitor logs:
   ```
   docker-compose exec app bash
   python manage.py report
   ```
1. Specify interval for which you would like to get visitor logs:
   ```
   python manage.py report --from "1970-01-01 00:00" --to "2021-12-31 23:59"
   ```
1. Check out an HTML version of the report: http://localhost:8000/report

## Run tests

```
docker-compose exec app bash
python manage.py test  --settings=simpletracker.settings_test
```
