# DB-Engines Ranking Predictor

Проект на Django, который парсит данные с сайта DB-Engines, анализирует рейтинги СУБД и предсказывает возможные изменения в их позициях.

## Основные функции

- Парсинг актуальных рейтингов СУБД с DB-Engines
- Анализ исторических данных и трендов
- Прогнозирование изменений в рейтинге
- Визуализация данных и предсказаний

## Технологии

- Python 3.9 и выше
- Django
- BeautifulSoup/Scrapy (для парсинга)
- Pandas (для анализа данных)
- Matplotlib/Chart.js (для визуализации)

## Установка и запуск

1. Клонируйте репозиторий:
```bash
    git clone https://github.com/chesnokov-an/DBMS_rating.git
    cd DBMS_rating
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows
    pip install django
    python manage.py migrate
    python manage.py runserver
```
