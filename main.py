from fastapi import FastAPI
from typing import Optional
app = FastAPI()

list =[
[1,"yazan", 25]
]

@app.get("/")
def read_root():
    return {"message": "Hello YAZAN from Railway!"}

@app.get("/all")
def read_all():
    result = []
    for item in list:
        dict = {"id": item[0],"name": item[1],"age": item[2]}
        result.append(dict)
    return result

@app.get("/{id}")
def read_id(id: int):
    for item in list:
        if id in item:
            return {"name": item[1], "age": item[2]}
    return {"message" : "Error"}

@app.post("/")
def post_item(id: int ,name: str ,age: int):
    item = [id,name,age]
    list.append(item)
    return {"message" : "Sccessfull"}

@app.delete("/{id}")
def delete_item(id: int):
    for item in list:
        if id in item:
            list.remove(item)
            return {"message" : "Sccessfull"}

@app.put("/{id}")
def update_item(id: int,name: Optional[str] = None,age: Optional[int] = None):
    for item in list:
        if id in item:
            if name:
                item[1]=name
            if age:
                item[2]=age
            return {"message" : "Sccessfull"}
