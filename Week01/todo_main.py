from fastapi import FastAPI
from todo_model import Todo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo): # (todo: int)
    todos.append(todo)
    return {"message": "Todo has been added"}

# Get single todo
# https://fastapi.tiangolo.com/tutorial/path-params/
@app.get("/todos/{todo_id}")
async def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been DELETED!"}
    return {"message": "No todos found"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No todos found to update"}
