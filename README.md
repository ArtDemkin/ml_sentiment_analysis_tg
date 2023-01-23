# Приложение для определения тональности сообщений в группе Telegram.
Приложение состоит из следующих структурных блоков:

[st_app.py](https://github.com/ArtDemkin/ml_sentiment_analysis_tg/blob/main/st_app.py) - модуль для анализа текстов сообщений, выполненный с помощью библиотеки Streamlit на основе модели rubert-base-cased-sentiment. Код модуля работоспособный, запускается.

[parser.py](https://github.com/ArtDemkin/ml_sentiment_analysis_tg/blob/main/parser.py) - модуль парсинга сообщений Telegram групп для их последующей обработки. ВНИМАНИЕ! Из кода удалены персональные данные (номер мобильного телефона и токен клиента Telegram), в связи с чем код можно запустить только указав свои данные. Без этих идентификационных параметров код запускаться не будет!

В репозитории размещен файл [chats.csv](https://github.com/ArtDemkin/ml_sentiment_analysis_tg/blob/main/chats.csv), содержащий 100 предобработанных сообщений открытого [Telegram-чата](https://t.me/+KxlX36pb-3hjMjRi) 

[Ссылка на равёрнутое приложение на платформе streamlit](https://artdemkin-ml-sentiment-analysis-tg-st-app-ln9oar.streamlit.app/)

Участники:
Демкин Артем Андреевич
