#!/usr/bin/env bash
sleep 10
resources/wait-for-db.sh -h db -p 3306 -t 120
python3.10 manage.py makemigrations
python3.10 manage.py migrate --noinput

# VVVV DEPLOY COMMANDS HERE VVVV

# ^^^^ DEPLOY COMMANDS HERE ^^^^

# VVVV TESTS VVVV
pytest .
# ^^^^ END TESTS ^^^^

python3.10 manage.py runserver 0.0.0.0:8000