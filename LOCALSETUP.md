# Local Setup

After cloning this repo, here are the steps (not covered in the workshop) to get it working locally!

### Prerequisites to success:

[ ] `git clone repo`
[ ] [Python 3.7 installed locally](https://www.python.org/downloads/)

## Environment setup
[ ] `python3 -m venv djangowiki` to create an [environment](https://docs.python.org/3/library/venv.html)
[ ] `source djangowiki/bin/activate` (on Mac)
[ ] `pip install -r requirements.txt`
[ ] `cd` to the directory where `manage.py` lives
[ ] Drink some water and stretch out

## 3
Run the following command:

`python3 manage.py migrate`

## 4
Next, create a superuser:

`python3 manage.py createsuperuser`

## 5
Locally, you can use either the provided `runserver` or `gunicorn` for dev-prod parity. Either command works:

`python3 manage.py runserver`

-OR-

`gunicorn dynowiki.wsgi`

