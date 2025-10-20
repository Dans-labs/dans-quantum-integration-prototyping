from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()

# quality labels stuff below, basics for now

class DatasetQualityLabel(BaseModel):
    id: int
    datasetUrl: str
    labelScore: float

# The labelScore is a float between 0 and 1, 
# where 1 is the highest quality (100%) and 0 is the lowest quality (0%)
# In a real application, this would be stored in a database
# For simplicity, we use an in-memory list here
labels_db: List[DatasetQualityLabel] = [
    DatasetQualityLabel(id=1, 
                        datasetUrl="http://example.com/dataset1", 
                        labelScore=0.85)
]

@app.get("/labels/", response_model=List[DatasetQualityLabel])
async def list_labels():  
    return labels_db

@app.get("/labels/{label_id}", response_model=DatasetQualityLabel)
async def get_label(label_id: int):    
    for label in labels_db:
        if label.id == label_id:
            return label
    raise HTTPException(status_code=404, detail="Label not found") 

# get a label by the url as query parameter
@app.get("/labels/by-url/", response_model=DatasetQualityLabel)
async def get_label_by_url(datasetUrl: str):    
    for label in labels_db:
        if label.datasetUrl == datasetUrl:
            return label
    raise HTTPException(status_code=404, detail="Label not found") 

@app.post("/labels/", response_model=DatasetQualityLabel)
async def create_label(label: DatasetQualityLabel):
    for existing_label in labels_db:
        if existing_label.id == label.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    labels_db.append(label)
    return label

@app.put("/labels/{label_id}", response_model=DatasetQualityLabel)
async def update_label(label_id: int, updated_label: DatasetQualityLabel):        
    for index, label in enumerate(labels_db):
        if label.id == label_id:
            labels_db[index] = updated_label
            return updated_label
    raise HTTPException(status_code=404, detail="Label not found")  

@app.delete("/labels/{label_id}")
async def delete_label(label_id: int):    
    for index, label in enumerate(labels_db):
        if label.id == label_id:
            del labels_db[index]
            return {"detail": "Label successfully deleted"}
    raise HTTPException(status_code=404, detail="Label not found")

# end quality labels stuff
