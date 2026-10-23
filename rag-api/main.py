from fastapi import FastAPI

app = FastAPI(title="RAG API Project")

@app.get("/")
def home():
    return {"message": "FastAPI 서버가 실행 중입니다."}

@app.get("/health")
def health_check():
    return {"status": "ok"}