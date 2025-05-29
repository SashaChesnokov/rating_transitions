# yourapp/management/commands/import_scores.py
import csv
from django.core.management.base import BaseCommand
from first.models import Scores


class Command(BaseCommand):
    help = 'Imports database rankings from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                Scores.objects.create(
                    place=int(row['Позиция в рейтинге (май 2025)']),
                    name=row['Название базы данных'],
                    type=row['Тип базы данных'],
                    score=float(row['Очки (май 2025)']),
                    month_change=float(row['Изменение очков (месяц)']),
                    year_change=float(row['Изменение очков (год)']),
                    predict=float(row['Прогноз изменения очков (июнь 2025)'])
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported data'))