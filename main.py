from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from students.router import router

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(router, prefix="/students")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("public/index.html", {"request": request})

