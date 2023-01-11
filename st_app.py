from transformers import pipeline
import streamlit as st
classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
st.title('Классификация изображений')
with open('chats.csv', 'r+', encoding="UTF-8") as df:
    for line in df:
        category = classifier([line])
        print(line, category)
        st.write(line, category)