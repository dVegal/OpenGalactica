![alt text](https://github.com/hmikihth/OpenGalactica/Screenshot_20200609_145743.jpg "Open Source GalacticaX Fork")

# OpenGalactica

It will be a Django based open source fork of the galacticaX.com ( gal6.com / galactica.haon.hu ) game.

## Installation

1.) Set up the database username, password and the Django Secret Key in your cfg file (template has been added). Do not forget it to rename and to write it into the settings.py.

2.) Migrate and create a superuser:
```bash
./manage.py makemigrations; 
./manage.py migrate;
./manage.py createsuperuser;
```

3.) Run it and enjoy :)

```bash
./manage.py runserver
```