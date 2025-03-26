from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Explorer(BaseModel):
    id: int
    name: str
    rank: str
    assignment: str
    species: str

class Alien(BaseModel):
    id: int
    name: str
    species: str
    homeworld: str
    affiliation: str

explorers_db = []
aliens_db = []

@app.post("/explorers/")
async def create_explorer(explorer: Explorer):
    explorers_db.append(explorer)
    return explorer

@app.get("/explorers/", response_model=List[Explorer])
async def read_explorers(skip: int = 0, limit: int = 10):
    return explorers_db[skip: skip + limit]

@app.get("/explorers/{explorer_id}", response_model=Explorer)
async def read_explorer(explorer_id: int):
    for explorer in explorers_db:
        if explorer.id == explorer_id:
            return explorer
    return {"error": "Explorer not found"}

@app.put("/explorers/{explorer_id}", response_model=Explorer)
async def update_explorer(explorer_id: int, updated_explorer: Explorer):
    for i, explorer in enumerate(explorers_db):
        if explorer.id == explorer_id:
            explorers_db[i] = updated_explorer
            return updated_explorer
    return {"error": "Explorer not found"}

@app.delete("/explorers/{explorer_id}")
async def delete_explorer(explorer_id: int):
    for i, explorer in enumerate(explorers_db):
        if explorer.id == explorer_id:
            del explorers_db[i]
            return {"message": "Explorer deleted"}
    return {"error": "Explorer not found"}

@app.post("/aliens/")
async def create_alien(alien: Alien):
    aliens_db.append(alien)
    return alien

@app.get("/aliens/", response_model=List[Alien])
async def read_aliens(skip: int = 0, limit: int = 10):
    return aliens_db[skip: skip + limit]

@app.get("/aliens/{alien_id}", response_model=Alien)
async def read_alien(alien_id: int):
    for alien in aliens_db:
        if alien.id == alien_id:
            return alien
    return {"error": "Alien not found"}

@app.put("/aliens/{alien_id}", response_model=Alien)
async def update_alien(alien_id: int, updated_alien: Alien):
    for i, alien in enumerate(aliens_db):
        if alien.id == alien_id:
            aliens_db[i] = updated_alien
            return updated_alien
    return {"error": "Alien not found"}

@app.delete("/aliens/{alien_id}")
async def delete_alien(alien_id: int):
    for i, alien in enumerate(aliens_db):
        if alien.id == alien_id:
            del aliens_db[i]
            return {"message": "Alien deleted"}
    return {"error": "Alien not found"}