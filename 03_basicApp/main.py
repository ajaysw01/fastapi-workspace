from fastapi import FastAPI, Path, Query
from typing import Annotated
app = FastAPI()

# Path parameters Validation 
# we use Annotated and Path
# You can declare all the same parameters as for Query.

@app.get("/items/{item_id}")
async def read_items(
  item_id : Annotated[int, Path(title="item id of the product"),],
  q : Annotated[str | None , Query(alias="item-query")]
) : 
  results = {"item id " : item_id}
  if q : 
    results.update({"q" : q})
  return results

# Number Validations : 
# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal

@app.get("/show_items/{item_id}")
async def show(
  item_id : Annotated[int, Path(title="item id of the product", gt=0, le=1000),],
  q : Annotated[str | None , Query(alias="item-query")]
) : 
  results = {"item id " : item_id}
  if q : 
    results.update({"q" : q})
  return results