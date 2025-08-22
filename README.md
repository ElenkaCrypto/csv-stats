[![tests](https://img.shields.io/github/actions/workflow/status/ElenkaCrypto/<repo>/tests.yml?branch=<branch>)](../../actions)
[![license](https://img.shields.io/github/license/ElenkaCrypto/csv-stats)](LICENSE)

# csv-stats
Отримай базову статистику по колонці CSV: count, min, max, mean, median, stdev. Автовизначення розділювача, підтримка назви або індексу колонки.

## Вимоги
- Python 3.10+

## Використання
```bash
# За назвою колонки
python csv_stats.py data.csv "price"

# За індексом колонки (0-базований)
python csv_stats.py data.csv 2

# З вказаним розділювачем
python csv_stats.py data.csv price -d ";"
