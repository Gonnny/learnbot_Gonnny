CatBot
======

CatBot - это бот для Telegramm созданный в качестве учебного по курсу LearnPython

Установка
---------

Создайте виртуальное окружение и активируйте его. Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt

Сохраните картинки с котиками в папку images. Название файлов должно начинаться с cat, а заканчиваться на .jpg, например cat1.jpg

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

PROXY = {'proxy_url': 'socks5://Ваш_SOCKS_PROXY:1080',
    'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}


API_KEY = "API_ключ, который вы получили у BotFather"


USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']


Запуск
------

В активированном виртуальном пространстве выполните:

.. code-block:: text

    python bot.py