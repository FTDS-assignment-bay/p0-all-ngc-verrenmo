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
    # Looping dari list weatherData untuk mencari location yang sama, jika tidak ada yang sama maka akan raise error
    for city in weatherData:
        # Jika location yang diinput sama dengan location dalam list maka akan megeluarkan data cuaca location tersebut. 
        # "%20" di replace ke " " karena ketika input spasi di vercel akan terbaca sebagai %20
        if city["Location"].lower() == location.lower().replace("%20", " "):
            return city
        
    raise HTTPException(status_code=404, detail="Location not found!")
        

# Second endpoint (/authenticate) handle api key authentication
@app.get('/authenticate')
def authenticate(pw: str = Header(None)):
    # Jika password yang diinput tidak sama dengan password "weather1234" maka akan raise error Unauthorized
    if pw != password:
        raise HTTPException(status_code=401,detail="Unauthorized!" )
    else:
        return {"message":"Authorized"}