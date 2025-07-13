
from fastapi import FastAPI, Request
from backend.chatbot import handle_message
from backend.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    init_db()

@app.post("/chat")
async def chat_endpoint(req: Request):
    data = await req.json()
    user_id = data["user_id"]
    message = data["message"]
    return {"response": handle_message(user_id, message)}
