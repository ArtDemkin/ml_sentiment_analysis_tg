from transformers import pipeline
import streamlit as st
classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

with open("chats.csv", 'r+', encoding="UTF-8") as df:
    for line in df:
        category = classifier([line])
        st.write(line, category)