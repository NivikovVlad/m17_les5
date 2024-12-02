"""
Использование БД в маршрутизации. 1.2
Цель: закрепить навык управления записями в БД, используя SQLAlchemy и маршрутизацию FastAPI.
"""
import uvicorn
from fastapi import FastAPI
from app.routers import task, user


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


if __name__ == "__main__":
    # !!!!
    # Запускать через консоль
    # uvicorn app.main:app --host 127.0.0.1 --port=8000 --reload
    # !!!!

    # http://127.0.0.1:8000/docs
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
