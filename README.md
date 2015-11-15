pip install -U -r requirements.txt

python manage.py --settings=py_board.settings.local

python manage.py migrate --settings=py_board.settings.local

python manage.py runserver 8080 --settings=py_board.settings.local


python manage.py makemigrations board file

python migrate