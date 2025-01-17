from fastapi import FastAPI, Query
from app.routes import route_lookup

app = FastAPI()

#Includes the router
app.include_router(route_lookup.router, prefix="/route", tags=["Route lookup"])

# @app.get("/")
# def read_root():
#   return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#   return {"item_id": item_id, "q": q} 