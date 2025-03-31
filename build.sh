poetry install
python3 manage.py test
python3 manage.py collectstatic
python3 manage.py compress --force
