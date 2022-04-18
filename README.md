# TweeForeTell

This webapp fetch the recent tweets and predict the mood as angry, happy, netural or sad.


## Team members

[Aanand S](https://www.github.com/unniznd/)

[Anaswara V Kumar](https://github.com/AnaswaraVKumar)

## How it Works

* Fetch the recent tweets with random query using tweepy in python
* Predict the mood of tweets 
* Render the results to a webpage

## How to Run locally

* Clone the repo
* Install the requirements ``` pip install -r requirements.txt ```
* Create a file ```dev_settings.py``` in ```twitterapi``` folder with suitable variables

Model of ```dev_settings.py```
```
ALLOWED_HOSTS = ['localhost']
bearer_token = 'add_bearer_token_here'
SECRET_KEY = 'add_secret_key_key'

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}
```
* Set ``` debug = False ``` in ```twitterapi/settings.py```
* Run the server
```
python manage.py runserver 
```
