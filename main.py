from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI-API-KEY"))
model = genai.GenerativeModel("gemini-3.8-flash")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    text: str

@app.get("/")
def home():
    return {"fast api server is running"}

@app.post("/generate")
def generate(prompt: Prompt):
    response=model.generate_content(prompt.text)
    return {'response': response.text}

    