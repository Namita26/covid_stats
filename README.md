# covid_stats

Basic set up for a python flask framework for writing RESTful APIs. In addition, MongoDB database is used.


## Set up

Set up the python3 environment with virtualenv.
1. Clone the repository
2. cd covid_stats
3. python3 -m venv shopse_venv
4. python -m requirements.txt
5. With these instructions, the python3 environment will be set up.
6. For mongodb set up, install mongo db compass or set up mongo db locally. Follow instructuons from here - https://docs.mongodb.com/compass/current/install/
7. Create a mongodb database named `covid` and a document inside that named `case`
8. System environment variables to initialize are - 1. `export ENVIRONMENT=development` 2. `export FLASK_ENV=development` 3. `export FLASK_APP=app.flask_app`
9. Now, for running the flask app in a development environment - `flask run`


## Sample Request Payload for registering a covid case.

curl --location --request POST 'http://127.0.0.1:5000/v1/covid_cases' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_id": 17,
    "current_status": "ACTIVE",
    "location": {
        "area": "Bandra West",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "continent": "Asia"
    },
    "found_active_on": "2021-03-22"
}'


## Sample Response after registration of a covid case.

{
    "_id": "6071ccd7a581396785e75cad",
    "user_id": 17,
    "current_status": "ACTIVE",
    "location": {
        "area": "Bandra West",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "continent": "Asia"
    },
    "found_active_on": "2021-03-22 00:00:00",
    "created_at": "2021-04-10 16:05:43.033741",
    "modified_at": "2021-04-10 16:05:43.033741"
}


## Sample Request for to get covid cases with filters

curl --location --request GET 'http://127.0.0.1:5000/v1/covid_cases?start_date=2021-03-28&end_date=2021-04-10&type=active&period=daily'


## Sample Response for getting no of a covid cases using filters

[
    {
        "period_counter": 13,  ## if period is week the period_counter is nth week of the year.
        "cases": 1
    },
    {
        "period_counter": 14,
        "cases": 1
    }
]
