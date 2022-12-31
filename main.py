from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")
df = open('chats.csv', 'r+', encoding="UTF-8")
for line in df:
    category = classifier([line])
    @app.get("/")
    async def root(line, category):
        print(line, category)
@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text )[0]