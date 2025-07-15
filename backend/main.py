from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()
app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Sample destinations
destinations = [
    {"name": "Paris", "description": "City of Lights and Love."},
    {"name": "Bali", "description": "Tropical paradise with beaches."},
    {"name": "Tokyo", "description": "Modern meets traditional Japan."},
]

@app.get("/destinations")
def get_destinations():
    return destinations

class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/contact")
def receive_contact(contact: Contact):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT, message TEXT
    )''')
    cursor.execute("INSERT INTO contact (name, email, message) VALUES (?, ?, ?)",
                   (contact.name, contact.email, contact.message))
    conn.commit()
    conn.close()
    return {"message": "Thanks for contacting us!"}
