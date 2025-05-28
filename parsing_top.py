from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import os
import time


def parse_db_engines():
    url = "https://db-engines.com/en/ranking"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)

        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.dbi")))

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        table = soup.find("table", class_="dbi")

        if not table:
            raise Exception("Не найдена таблица с классом 'dbi' на странице")

        # Парсим единую таблицу и разделяем данные
        parse_combined_table(table)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        driver.quit()


def parse_combined_table(table):
    rows = table.find_all("tr")

    # Подготовка данных для двух таблиц
    ranking_data = []
    score_data = []

    # Пропускаем заголовки (первые 2 строки)
    for row in rows[2:]:
        cells = row.find_all(['td', 'th'])
        row_data = [cell.get_text(strip=True) for cell in cells]

        if len(row_data) >= 8:  # Проверяем, что строка содержит все нужные данные
            # Данные для таблицы с рангами
            rank_entry = {
                'May 2025 Rank': row_data[0],
                'Apr 2025 Rank': row_data[1],
                'May 2024 Rank': row_data[2],
                'DBMS': row_data[3]
            }
            ranking_data.append(rank_entry)

            # Данные для таблицы с характеристиками
            score_entry = {
                'DBMS': row_data[3],  # Название СУБД
                'Database Model': row_data[4],  # Модель базы данных
                'May 2025 Score': row_data[5],  # Текущий счёт
                'Apr 2025 Score Change': row_data[6],  # Изменение за месяц
                'May 2024 Score Change': row_data[7]  # Изменение за год
            }
            score_data.append(score_entry)

    # Сохраняем таблицу с рангами
    df_rank = pd.DataFrame(ranking_data)
    rank_path = os.path.join(os.getcwd(), "db_ranking.csv")
    df_rank.to_csv(rank_path, index=False, encoding="utf-8")
    print(f"Таблица с рангами сохранена: {rank_path}")

    # Сохраняем таблицу с характеристиками
    df_score = pd.DataFrame(score_data)
    score_path = os.path.join(os.getcwd(), "db_scores.csv")
    df_score.to_csv(score_path, index=False, encoding="utf-8")
    print(f"Таблица с характеристиками сохранена: {score_path}")


if __name__ == "__main__":
    parse_db_engines()