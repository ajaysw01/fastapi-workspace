from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Optional
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


# apis
@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}



# path parameters

@app.get("/blog/{blog_id}")
def index(blog_id:int) : 

    return { 'data':blog_id}

@app.get('/blog/{id}/comments')
def comments(id:int, limit = 10):
    return {'data':{'1','2','3'}}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    elif food_name == FoodEnum.fruits:
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }
    return {"food_name": food_name, "message": "i like chocolate milk"}

# Query Paraemters
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items")
# async def list_items(skip: int = 0, limit : int =10):
#     return fake_items_db[skip:skip+limit]


@app.get("/item/{item_id}")
async def getItemId(item_id : int, qparam: str):
    if qparam : 
        return {"item id : ": item_id, "query param : ": qparam}
    else : 
        return {"item id : ": item_id}


@app.get("/blog")
def unpublished(limit=10,published:bool=True, sort : Optional[str] = None) : 
    if published:
        return {'data':f'{limit} publishedblogs from db'} 
    else : 
        return {'data': f'{limit} normal blogs'}


#RequestBody

class Item(BaseModel):
    name : str
    description : Optional[str] = None #below 3.10
    price : int
    tax : float | None = None #above 3.10

@app.post("/items")
async def createitems(item : Item):
    return {item}



class Blog(BaseModel):
    title : str
    body : str 
    published : Optional[bool]

@app.post("/blog")
async def create_blog(blog:Blog):
    return {'data' : f'blog is created with title {blog.title}'}


client = TestClient(app)

def test_root() : 
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}





