# Приложение для определения тональности сообщений в группе Telegram.
Приложение состоит из следующих структурных блоков:

1) [parser.py](https://github.com/ArtDemkin/ml_sentiment_analysis_tg/blob/main/parser.py) - модуль парсинга сообщений Telegram групп для их последующей обработки. Из кода удалены персональные данные (номер мобильного телефона, api_id и api_hash, получить их можно перейдя по [ссылке](https://my.telegram.org/auth) и авторизовавшись с номера привязанного к аккаунту telegram), в связи с чем код можно запустить только указав свои данные. Без этих идентификационных параметров код запускаться не будет.

2) [st_app.py](https://github.com/ArtDemkin/ml_sentiment_analysis_tg/blob/main/st_app.py) - модуль для анализа текстов сообщений, выполненный с помощью библиотеки Streamlit на основе модели [rubert-base-cased-sentiment](https://huggingface.co/blanchefort/rubert-base-cased-sentiment). Код модуля работоспособный, запускается.

В репозитории размещен файл [chats.csv](https://github.com/ArtDemkin/ml_sentiment_analysis_tg/blob/main/chats.csv), содержащий 100 предобработанных сообщений открытого [Telegram-чата](https://t.me/+KxlX36pb-3hjMjRi) 

Используются библиотеки:

- [TensorFlow](https://www.tensorflow.org/).
- [Streamlit](https://streamlit.io/).
- [Transformers](https://huggingface.co/docs/transformers/index).
- [Telethon](https://pypi.org/project/Telethon/).

# [Ссылка на равёрнутое приложение на платформе streamlit](https://artdemkin-ml-sentiment-analysis-tg-st-app-zks4ln.streamlit.app/)

Участники:
Дёмкин Артем
