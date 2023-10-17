from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import json


app = FastAPI()


@app.get("/items/")
async def read_items():
   
    df = pd.read_excel('smaller.xls')
    jsondata = df.to_json()
    parsed_json = json.loads(jsondata)
    pretty =json.dumps(parsed_json, indent=4, sort_keys=True)
    return pretty

# server run command $uvicorn kawohl_app:app --reload