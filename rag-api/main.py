from fastapi import FastAPI

app = FastAPI(title="RAG API Project")

@app.get("/")
def home():
    return {"message": "FastAPI 서버가 실행 중입니다."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

 
# 홈 url : http://127.0.0.1:8000/
# health check url : http://127.0.0.1:8000/health
# API 문서 url : http://127.0.0.1:8000/docs