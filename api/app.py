from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.get("/check")
def check():
  return "Your API is up!"

class Item(BaseModel):
    name: str
    description: str

@app.post("/news")
def predict_news(item:Item):
    return item


@app.post("/bnewscore")
def create_upload_file(file: UploadFile = File()):
    try:
        df=pd.read_csv(file.file)
        
        # 
        # prediction pipeline goes heere
        #

          
    except Exception as e:
        return {"error":f"Error occured:{e}"}
    return df.to_json()
    
@app.post("/jdentities")
def create_upload_file(file: UploadFile = File()):
    try:
        df=pd.read_csv(file.file)
        
        # 
        # prediction pipeline goes heere
        #

          
    except Exception as e:
        return {"error":f"Error occured:{e}"}
    return df.to_json()
