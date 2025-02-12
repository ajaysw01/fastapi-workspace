from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# path parameters
@app.get("/items/{item_id}")
async def get_id(item_id : int) :
    return {"item id ": item_id}

# we can pass predefined values as Enum
class ModelName(str, Enum):
    tata = "neo"
    maruti = "suzuki"

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName) :
    #comparing enumeration no
    if model_name is ModelName.tata :
        return {"Model Name ": model_name}
    #value of a enum can be return as ModelName.maruti.value
    if model_name.value == "suzuki" :
        return  {"model naem " : model_name}

# path converter : normally FA scans single segment of the url
# we use : path
@app.get("/files/home/{file_path:path}")
async def read_file(file_path : str) :
    return {"file_path":file_path}

# query parameters
# can be optional and we can set default values as well

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/read_items")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# optional

@app.get("/show_item/{item_id}")
async def show_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item": item_id}


# Multiple path and query parameters

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
    