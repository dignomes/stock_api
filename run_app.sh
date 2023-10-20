#!/bin/bash
python manage.py makemigrations  --settings=config.settings
python manage.py migrate  --settings=config.settings
python manage.py runserver
