from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import uvicorn
from pydantic import BaseModel
from typing import List
from contextlib import asynccontextmanager
from load import load_condition_model, load_disease_model
import os
from dotenv import load_dotenv

load_dotenv()

model = {}

# load model initially
@asynccontextmanager
async def lifespan(api: FastAPI):
    model["condition"] = await load_condition_model()
    model["disease"] = await load_disease_model()
    yield
    model.clear()

app = FastAPI(lifespan=lifespan)

class input_tensor(BaseModel):
    # array 4D based on input from backend server
    array: List[List[List[List[float]]]]

@app.post("/predict/condition")
async def predictCondition(req: input_tensor):
    tensor_array = np.array(req.array)
    try:
        predictions = model["condition"].predict(tensor_array)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return JSONResponse(content={"predictions": predictions.tolist()})

@app.post("/predict/disease")
async def predictDisease(req: input_tensor):
    tensor_array = np.array(req.array)
    try:
        predictions = model["disease"].predict(tensor_array)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return JSONResponse(content={"predictions": predictions.tolist()})
    
if __name__ == '__main__':
    env = os.getenv("ENV", "development")
    if env == 'development':
      uvicorn.run(app, host='localhost', port=7777)
    else:
      uvicorn.run(app, host='0.0.0.0', port=80)