from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    nombre: str
    apellido: str
    dni: int
    muerto: bool = True


@app.get("/")
async def root():
    return {"message:" "hola martin pelotudod"}


@app.get("/posts")
async def get_posts():
    return {"Message": "Estos son tus mensajes"}


@app.post("/crearpost")
def create_post(mensajes: dict = Body(...)):
    print(mensajes)
    return {"message:": f"Tu nombre es {mensajes['Nombre']} y tu apellido es {mensajes['Apellido']}"}


@app.post("/mensajear")
def create_post(nuevo_mensaje: Post):
    print(nuevo_mensaje)
    return {f"Este es tu nombre: {nuevo_mensaje.nombre}/n \n Este es tu apellido: {nuevo_mensaje.apellido}"}
