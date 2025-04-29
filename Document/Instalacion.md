1) Instalacion de virtual venv Git Bash

````bash
    python -m venv venv
````

2) Activar el virtual venv

````bash
    source venv/Scripts/activate
````

3) Instalar Django

````bash
    pip install django
````

4) Crear la carpeta de configuracion de django

````bash
    django-admin.exe startproject mysite .
````


5) Para crear los App de Django y empezar las paginas ahi 

````bash
python manage.py startapp blog
````


6) Para ejecutar django 

````bash
    python manage.py runserver
````
