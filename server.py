from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class AskRequest(BaseModel):
    message: str

@app.post("/ask")
def ask(req: AskRequest):
    # Your Muse logic here, e.g.
    return {"reply": "Muse responds: " + req.message}

