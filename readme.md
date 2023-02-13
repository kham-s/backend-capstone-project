# Back-End Developer Capstone

Please update settings.py database credentials or create a mysql user with the following credentials:

USER : 'admindjango'
PASSWORD : 'employee@123!'

Using pipenv recreate the project environment:
    pipenv install
    pipenv shell
    python manage.py migrate
    python manage.py runserver

## Create an account
Create an account by posting username and password to the following api endpoint:
http://localhost:8000/auth/users/ (POST)

Here is a sample payload:

    {"username": "some_username", "password": "user_password"}

## Log in to get auth token
Login by posting username and password to the following api endpoint:
http://localhost:8000/auth/token/login (POST)

or to:
http://localhost/api-auth-token (POST)

For example, with the previously created user the payload would be:

    {"username": "some_username", "password": "user_password"}

## API endpoints
The api endpoints are restricted to authenticated users.
If you logged in using a web browser, you should have access to the following endpoints.
Else, log in and include your auth token in your request header.

### Menu
http://localhost:8000/api/menus

## Bookings
http://localhost:8000/api/bookings