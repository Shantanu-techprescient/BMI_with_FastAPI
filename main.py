from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel, Field, constr
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from update_file import write_comment
from calculate_bmi import calculate_bmi

app = FastAPI()

class Items(BaseModel):
	name : str = Field(max_length=20, min_length=1, regex='[a-zA-Z.]')
	age : Optional[int]
	weight : float
	height_feet : int
	height_inches: int


@app.get("/")
def root():
    return {"greetings": "hello world"}

@app.get("/shantanu")
def root():
    return {"greetings": "hello shantanu"}

@app.get("/milind")
def root():
    return {"greetings": "hello milind"}

@app.post("/bmi/")
def read_elements(data : Items): #url lis
    bmi, height = calculate_bmi(data.height_feet, data.height_inches, data.weight, data.age)
    comment = write_comment(data.name, data.age, height, data.weight, bmi)
    return {"comment" : comment}


@app.get("/bmi/")
def read_elements( name: str = Query(...,max_length=20, min_length=1, regex='[a-zA-Z.]'), 
				age: int = Query(...), 
				height_feet: int = Query(...), 
				height_inches: int = Query(...), 
				weight: float = Query(...)): 
    bmi, height = calculate_bmi(height_feet, height_inches, weight, age)
    comment = write_comment(name, age, height, weight, bmi)
    return {"comment" : comment}


@app.get("/show")
def show_data():
    comment_list = list()
    with open("bmi-info.txt","r") as bmi_file:
        for line in bmi_file:
            comment_list.append(line)
    
    dump_data = jsonable_encoder(comment_list)
    return JSONResponse(content = dump_data)
            




    
