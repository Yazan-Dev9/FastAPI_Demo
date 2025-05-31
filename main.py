from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

# Test data
people_list: List[Person] = [
    Person(id=1, name="yazan", age=25)
]

@app.get("/")
def read_root():
    return {"message": "Hello YAZAN ! (use fastapidemo.up.railway.app/docs link to control)"}

@app.get("/all")
def read_all():
    return people_list

@app.get("/{id}")
def read_id(id: int):
    for person in people_list:
        if person.id == id:
            return person
    raise HTTPException(status_code=404, detail="Person not found")

@app.post("/")
def post_item(person: Person):
    # Check id dons't exist in list
    if any(p.id == person.id for p in people_list):
        raise HTTPException(status_code=400, detail="ID already exists")
    people_list.append(person)
    return {"message": "Successful"}

@app.delete("/{id}")
def delete_item(id: int):
    for i, person in enumerate(people_list):
        if person.id == id:
            del people_list[i]
            return {"message": "Successful"}
    raise HTTPException(status_code=404, detail="Person not found")

@app.put("/{id}")
def update_item(id: int, name: Optional[str] = None, age: Optional[int] = None
):
    for person in people_list:
        if person.id == id:
            if name is not None:
                person.name = name
            if age is not None:
                person.age = age
            return {"message": "Successful"}
    raise HTTPException(status_code=404, detail="Person not found")
