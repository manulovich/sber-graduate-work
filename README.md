# Сбер. Дипломный проект

Все начинается [здесь](https://github.com/manulovich/sber-graduate-work/blob/main/Main.ipynb).

## Структура репозитория
```
├── Data_preparation.ipynb
├── EDA.ipynb
├── Main.ipynb
├── README.md
├── Recom_collab_base.ipynb
├── Recom_rating_base.ipynb
├── __pycache__
│   ├── utils.cpython-310.pyc
│   └── utils.cpython-39.pyc
├── data
│   ├── articles.csv
│   ├── customers.csv
│   ├── sample_submission.csv
│   └── transactions_train.csv
├── data_prepared
│   ├── article_and_top_age_group.csv
│   ├── articles.csv
│   ├── customers.csv
│   ├── last_transactions.csv
│   └── transactions.csv
├── prediction
│   ├── collab_base.csv
│   └── rating_base.csv
└── utils.py
```

### Директории
1. `/data` - Директория с исходными файлами из [задания](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/overview). Скачивается самостоятельно.
2. `/data_prepared` - Директория с подготовленными данными для алгоритмов. Заполняется в процессе выполнения скриптов ноубуков .ipynb.
3. `/prediction` - Директория с предсказаниями. Заполняется в процессе выполнения скриптов ноубуков .ipynb.

## Развертка
1. Клонируем данный репозиторий.
2. Создаем директории `/data`, `/data_prepared`, `/prediction`.
3. Скачиваем датасет из [задания](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/overview) и распаковываем в директорию `/data`.
4. Выполняем все скрипты последовательно, начиная с главного файла `./Main.ipynb`.