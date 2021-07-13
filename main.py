from fastapi import FastAPI, Query
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, constr, conint, confloat , create_model
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import sys

sys.path.append('/.../FastAPI/crud')
from update_file import write_comment
from show_comments import show_data
sys.path.append('/.../FastAPI/router')
from calculate_bmi import calculate, bmi_category

app = FastAPI()


class Height(BaseModel):
	feet: int = Field(ge= 5, description="Minimum value should be 5feet")
	inches: Optional[int] = Field(ge= 0, lt= 12, description="Value should be in range 0 to 11")

class Items(BaseModel):
	name : str = Field(max_length=20, min_length=1, regex='[a-zA-Z.]')
	age : int
	weight : float = Field(ge=45.50, description="Values should be in kgs & Minimum weight should be 45.5kgs")
	height : Height


@app.post("/bmi/")
def calculate_bmi(data : Items): #url lis
    print('#########1')
    bmi, height_cms = calculate(data.height.feet , data.height.inches, data.weight, data.age)
    print('#########1')
    category = bmi_category(bmi)
    print('#########1')
    comment = write_comment(data.name, data.age, height_cms, data.weight, bmi, category)
    print('#########1')
    return {"comment" : comment}


@app.get("/show")
def show_results():
    dump_data = show_data()
    return JSONResponse(content = dump_data)
            





    
