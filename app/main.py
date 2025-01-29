from fastapi import FastAPI, Query
from app.routes import route_lookup
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

#Includes the router
app.include_router(route_lookup.router, prefix="/route", tags=["Route lookup"])

@app.get("/")
def read_root():
  return {"message": "Hello from FastAPI"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#   return {"item_id": item_id, "q": q} 