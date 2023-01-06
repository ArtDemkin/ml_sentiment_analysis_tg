from transformers import pipeline
classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
df = open('chats.csv', 'r+', encoding="UTF-8")
for line in df:
    category = classifier([line])
    print(line, category)