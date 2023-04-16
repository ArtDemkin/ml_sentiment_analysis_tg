from transformers import pipeline
import streamlit as st

classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
st.title('Анализ тональности текста сообщений из группы телеграмм')
path_to_strings = 'chats.csv'


def strings_analize():
    global line
    with open(path_to_strings, 'r+', encoding="UTF-8") as df:
        for line in df:
            category = classifier([line])
            print(line, category)
            st.write(line, category)


strings_analize()
