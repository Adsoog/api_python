from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message:" "hola martin pelotudo"}
