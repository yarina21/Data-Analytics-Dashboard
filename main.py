from fastapi import FastAPI

app = FastAPI() #am creat un server


@app.get("/") #este un decorator specific fastapi
async def root(): #o functie asincrona
    return {"message": "Hello Yari"} 