from fastapi import FastAPI, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import requests
from typing import Annotated


API_URL = "http://127.0.0.1:5000"


app = FastAPI(title="render templates")
templates = Jinja2Templates(directory="templates")


@app.get('/')
def index(request: Request):
      r = requests.get(f"{API_URL}")
      data = r.json()
      return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to Shelf Stream", "g_list" : data})


@app.post('/order')
async def submit(product_name : Annotated[str, Form(...)], order_qty: Annotated[str, Form(...)]):
      requests.get(f"{API_URL}/order/{product_name}?order_qty={order_qty}")
      return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
