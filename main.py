from fastapi import FastAPI
#from domain.question import question_router

app = FastAPI()


#origins = [
#    "http://13.209.183.10:5173"
#]

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=origins,
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

#app.include_router(question_router.router)



@app.get("/hello")
def hello():
    return {"message": "안녕하세요...!!!! Sunny(Jang Seon-Ho)...Python FAST Api...!!!!!!"}
