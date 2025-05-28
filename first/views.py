import csv
from django.shortcuts import render
from django.conf import settings
import os
# Create your views here.


# views.py
import csv
from django.shortcuts import render
from django.conf import settings
import os


def index_page(request):
    # Чтение данных из CSV файлов
    ranking_data = []
    scores_data = []

    # Пути к файлам
    ranking_path = os.path.join(settings.BASE_DIR, 'db_ranking.csv')
    scores_path = os.path.join(settings.BASE_DIR, 'db_scores.csv')

    # Чтение файла с рейтингами
    with open(ranking_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ranking_data.append(row)

    # Чтение файла с оценками
    with open(scores_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores_data.append(row)

    # Объединение данных
    combined_data = []
    for rank in ranking_data[:50]:  # Берем топ-50 для отображения
        dbms = rank['DBMS'].split('Detailed')[0].strip()  # Удаляем "Detailed..." из названия
        score = next((item for item in scores_data if item['DBMS'].startswith(dbms)), None)

        if score:
            # Определяем тип СУБД
            db_type = score['Database Model'].split(',')[0].strip()
            if 'Multi-model' in score['Database Model']:
                db_type += " (Multi-model)"

            combined_data.append({
                'rank': rank['May 2025 Rank'].replace('.', ''),
                'name': dbms,
                'type': db_type,
                'score': score['May 2025 Score'],
                'month_change': score['Apr 2025 Score Change'],
                'year_change': score['May 2024 Score Change']
            })

    context = {
        'databases': combined_data
    }

    return render(request, 'index.html', context)


def about_page(request):
    context = {}
    return render(request, 'about.html', context)


def methodology_page(request):
    context = {}
    return render(request, 'methodology.html', context)


def contacts_page(request):
    context = {}
    return render(request, 'contacts.html', context)