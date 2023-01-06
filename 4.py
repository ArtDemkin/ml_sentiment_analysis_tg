import streamlit as st
from transformers import pipeline
classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
df = open('chats.pkl', 'r+', encoding="UTF-8")
st.title('Классификация изображений')
for line in df:
    category = classifier([line])
    print(line, category)
    st.write(line, category)
