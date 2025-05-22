from fastapi import FastAPI

app = FastAPI()

list =[
[1,"yazan", 25]
]

@app.get("/")
def read_root():
    return {"message": "Hello YAZAN from Railway!"}

@app.get("/{id}")
def read_id(id: int):
    for item in list:
        if id in item:
            return {"name": item[1], "age": item[2]}
    return {"message" : "Error"}

@app.post("/")
def post_item(id,name,age):
    item = [id,name,age]
    list.appind(item)
    return {"message" : "Sccessfull"}
