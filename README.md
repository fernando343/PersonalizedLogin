# Personalized login

Django by default gives us an already predefined user system where the necessary fields to start session are username and password but many times we want to have a personalized login either by email or by phone number like many web applications to be able to do this. What we have to do is create an app with the username for this we do it with the following code 

    python manage.py startapp users

This will create a user app we go to models and import the library that allows us to change the configuration

    from django.contrib.auth.models import AbstractUser

We create a user model as we want in this case since our login will be through email that will be like our username for that we define this compo 

    email = models.EmailField('email address', unique=True, error_messages={
        'unique': 'Este email ya esta en uso'
    })

We indicate that it is unique since it is the field by which we will start the session and it should not be repeated.

Then we add the other fields that we want to include in this.

We must also add

    USERNAME_FIELD = 'email'

since it is the field that we indicate that it will be the main one.
After doing this we go to our settings.py file and add a new variable indicating what our new user model will be.

    AUTH_USER_MODEL = 'users.User'

We must not forget to add the app to settings.py and to do this before starting to build our application since doing it later could bring us problems and we only need to implement the migrations and we have our custom login ready
