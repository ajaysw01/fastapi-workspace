from fastapi import FastAPI,Query
from typing import Annotated , Literal
from pydantic import BaseModel, Field


# Request Body 
# we use Pydanctic models 
#
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

# delclare as param in function 
# Fastapi will read req as json, convert to corresponidng types if needed
# validate the data 
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None : 
        price_with_tax = item.price + item.tax
        item_dict.update({"price with tax": price_with_tax})
    return item_dict


# query parameters and string validation 
@app.get("/read_items/")
async def read_items(q: Annotated[str | None, Query(title="Read Items",description = " thsi is metadata", max_length=20, min_length=5)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# add regex too, by using pattern attribute
# we can declare expilcity a value a required by add Ellipsis (...)
# To do that, you can declare that None is a valid type but still use ... as the default:

# Type Hints 
# we can provide metadata in Annotated 
# first paramter = actual type , rest is metadata for other tools
# title, descriptoin ,alias

@app.get("/")
def say_hello(name : Annotated[str, "this is just metadata"]) -> str : 
    return f"hello {name}"

# query parameter list 
# When you define a query parameter explicitly with Query you can also declare it to receive a list of values, or said in another way, to receive multiple values.

@app.get("/multiple")
async def multiple_queries(q : Annotated[list[str] | None, Query()]= ["foo","bar"]) : 
    queryItems = {"q": q}
    return queryItems

# To declare a query parameter with a type of list, like in the example above, you need to explicitly use Query, otherwise it would be interpreted as a request body.
# metadata example 

@app.get("/metadata")
async def show(
    q : Annotated[str | None,
                  Query(
                      alias="item-query",
                      title="Query String",
                      description="This is metadata of query",
                      min_length=3,
                      max_length=50,
                      pattern="^fixedquery$",
                      deprecated=True
                  ),
                ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems), set the parameter include_in_schema of Query to False:

@app.get("/excluding/")
async def exclude_params(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}

# Query parameter models 
# If you have a group of query parameters that are related, you can create a Pydantic model to declare them.

class FilterParams(BaseModel) : 
    model_config = {"extra","forbid"} #o restrict the query parameters that you want to receive.
    limit : int = Field(100, gt = 0, le= 100)
    offset : int = Field(0, ge=0)
    order_by : Literal["created_at","updated_at"] = "created_at"
    tags : list[str] = []

@app.get("/querymodel")
async def querymodel(filter_query : Annotated[FilterParams, Query()]) : 
    return filter_query
