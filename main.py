from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "안녕하세요...!!!! Sunny(Jang Seon-Ho)...Python FAST Api...!!!!!!"}
