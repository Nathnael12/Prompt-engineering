import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import sys
import re
sys.path.append('../scripts')

from preprocessor import Processor
from pridict import Predict
from logger import Logger
app_logger = Logger("api.log").get_app_logger()
processor=Processor()
predictor = Predict()

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


@app.post("/jdentities")
def create_upload_file(file: UploadFile = File()):
    predictions=[]
    try:
        df=pd.read_csv(file.file)
        # 
        # prediction pipeline goes heere
        #
        
        for ind in df.index:
            prediction=""
            prediction=predictor.predict_job(df)
            res={}
            res={
                "Post":df['Description'],
                "Entities":prediction
            }
            predictions.append(res)


        
    except Exception as e:
        pass
    return json.dumps(predictions)

    
@app.post("/bnewscore")
def create_upload_file(file: UploadFile = File()):
    predictions=[]
    try:
        df=pd.read_csv(file.file,encoding="utf8")
        # 
        # prediction pipeline goes heere
        #
        for ind in df.index:
            try:
                prediction=""
                # predictions.append(pd.DataFrame(df.iloc[ind,:]).T.to_json())
                prediction=predictor.predict_news(pd.DataFrame(df.iloc[ind,:]).T,'e74ec85a-8e14-4913-83d5-02fe80ac7c4f-ft')
                res={}
                res={
                    "News":(df.loc[ind,'Description']),
                    "Predicted_Score":re.findall("\d+\.*\d*", prediction)[0] if len(re.findall("\d+\.*\d*", prediction)) >0 else ""
                }
                predictions.append(res)
            except Exception as e:
                app_logger.error(f"cannot convert to json {e}")

    except Exception as e:
        app_logger.erro(f"api: {e}")
        pass
    return {"predictions":predictions}
