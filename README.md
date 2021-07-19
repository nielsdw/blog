## blog

It was tested on Python 3.8.

To install:

`python3.8 -m venv env`

`. env/bin/activate`

`pip install -r requirements.txt`

`./manage.py makemigrations`

`./manage.py migrate`

To run tests:

`pytest`

To run test server:

`./manage.py runserver`

To add 2-factor authentication i would suggest setting up Django Two Factor Authentication (1) using Twilio SMS service (2)

1. https://django-two-factor-auth.readthedocs.io/en/stable/index.html
2. https://www.twilio.com/sms
