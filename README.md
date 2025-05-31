# FastAPI People Demo

A simple RESTful API built with FastAPI for managing a list of people (id, name,
 age).  
This project is intended for learning and experimentation purposes.

---

## Features

- List all people
- Add new person
- Get person by ID
- Update person data
- Delete person

---

## Requirements

- Python 3.8+
- fastapi
- uvicorn

Install requirements with:

``bash``
```
pip install fastapi uvicorn
---
```

## How to Run

Start the server locally with:

``bash``
```
uvicorn main:app --reload
```

> Replace `main` with your Python filename if different.

The API will be available at [http://localhost:8000](http://localhost:8000)

You can test and explore the API via the interactive docs:
- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Example Endpoints

- `GET /all`        List all people
- `GET /{id}`        Get person by ID
- `POST /`          Add new person (JSON body)
- `PUT /{id}`        Update person data
- `DELETE /{id}`      Delete person

---

## Live Demo

- [Live API](https://fastapidemo.up.railway.app/)
- [Live API Control](https://fastapidemo.up.railway.app/docs)

---


## License

MIT License.  
For learning and demo purposes.
