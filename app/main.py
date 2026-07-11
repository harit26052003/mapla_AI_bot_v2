from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Mapla AI Bot Running 🚀"}
