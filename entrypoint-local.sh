#!/usr/bin/env bash
sleep 10
resources/wait-for-db.sh -h db -p 3306 -t 120
python3.7 manage.py makemessages -all
python3.7 manage.py compilemessages
python3.7 manage.py makemigrations
python3.7 manage.py migrate --noinput

# Start deploy commands:

# ^^^^ DEPLOY COMMANDS HERE ^^^^

python3.7 manage.py runserver 0.0.0.0:8000