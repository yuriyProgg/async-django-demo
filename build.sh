poetry install
python manage.py migrate
python3 manage.py test
python3 manage.py collectstatic --noinput
python3 manage.py compress --force
