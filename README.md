# convert-image-to-thumbnail


## How to use
1. run **git clone https://github.com/NobleSalt/convert-image-to-thumbnail.git**
2. **cd convert-image-to-thumbnail/**
3. run **python -m venv env**
4. run **env/Scripts/activate** *windows* || **source env/bin/activate** *linux*
5. run **pip install -r requirements.txt**
6. run **python manage.py migrate**
7. run **python manage.py makemigrations toThumb**
8. run **python manage.py migrate toThumb**
9. run **python manage.py createsuperuser** *and follow the prompt*
10. finally, run **python manage.py runserver** *and go to localhost:8000*