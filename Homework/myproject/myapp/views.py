from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    description_main = '''
Добро пожаловать на главную страницу. На данный момент показывать нечего, так что пока тут будет инструкция как начать работу в Django:
<br><br> 
1. установка Django
- pip install django<br>
- django-admin startproject myproject<br>
- cd myproject<br>
- python3 manage.py startapp myapp</i>
<br><br>
2.  Необходимо создать и активировать виртуальное окружение: <br>
Вводим в терминал директории:
- <i>python -m venv .venv</i>, и затем
- /.venv/Scrypts/activae.ps1
<br><br>
3. Откройте файл settings.py и добавьте 'myapp' в список установленных приложений:
<br><br>
INSTALLED_APPS = [ <br>
  ... <br>
  'myapp', <br>
  ... <br>
]
<br><br>
4. Далее прописываем маршруты
<br><br>
5. Теперь вы можете запустить свой сайт с помощью команды в терминале:
<br>
- <i>python manage.py runserver</i>
<br><br>
Вы должны увидеть сообщение о том, что сервер работает. 
<br>
Теперь вы можете открыть браузер и перейти по адресу который вам даст терминал , чтобы увидеть главную страницу вашего интернет-магазина.
    '''
    logger.info("Visit page main")
    return HttpResponse(description_main)


def about(request):
    descryption_about = '''
    <h2> Меня зовут Александр.<br>
    Мне 21 год и я изучаю IT.<br>
    Даётся не легко но я стараюсь.<br>
    </h2><br>
    '''
    logger.info("Visit page about")
    return HttpResponse(descryption_about)