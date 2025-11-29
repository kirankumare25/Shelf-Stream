from fastapi import FastAPI
from models import Grocery_list
import uvicorn


server = FastAPI(title="Shelfstream")

@server.get('/')
@server.get('/store')
def index():
    return Grocery_list

@server.get('/order/{product}')
def order_product(product, order_qty):
    Grocery_list[product]["units"] -= int(order_qty)

    return {
        "product": product,
        "order_quantity": order_qty,
        "left_units": Grocery_list[product]["units"] 
    }

if __name__ == "__main__":
     uvicorn.run(
        server,
        host="127.0.0.1",
        port=5000 # <-- Service B is now on port 8080
    )
