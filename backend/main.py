from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserProfile(BaseModel):
    UserID: str
    DisplayName: str
    ImageUrl: str

@app.post("/api")
async def receive_profile(data: UserProfile):
    global latest_profile
    latest_profile = {
        "UserID": data.UserID,
        "DisplayName": data.DisplayName,
        "ImageUrl": data.ImageUrl,
    }
    return {"userId": latest_profile["UserID"], "DisplayName": latest_profile["DisplayName"], "ImageUrl": latest_profile["ImageUrl"]}

@app.get("/api")
async def get_profile():
    return {
        "DisplayName": latest_profile['DisplayName'],
        "ImageUrl" : latest_profile['ImageUrl'], 
        "UserID" : latest_profile['UserID']
    }