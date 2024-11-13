from fastapi import FastAPI, HTTPException, Header
import pandas as pd

app = FastAPI()

password = "weather1234"

weatherData = [
    {
       "Location"         : "New York City",
       "Temperature"      : 4,
       "Weather Condition": "Clear" 
    },
    {
       "Location"         : "Los Angeles",
       "Temperature"      : 13,
       "Weather Condition": "Clear"
    },
    {
       "Location"         : "Chicago",
       "Temperature"      : 7,
       "Weather Condition": "Clear"
    }   
]

# First endpoint (/weather/{location}) provide weather data for a spesific location
@app.get('/weather/{location}')
def displayData(location: str):
    for city in weatherData:
        if city["Location"].lower() == location.lower():
            return city
    raise HTTPException(status_code=404, detail="Location not found!")
        

# Second endpoint (/authenticate) handle api key authentication
@app.get('/authenticate')
def authenticate(pw: str = Header(None)):
    if pw != password:
        raise HTTPException(status_code=401,detail="Unauthorized!" )
    else:
        return {"message":"Authorized"}