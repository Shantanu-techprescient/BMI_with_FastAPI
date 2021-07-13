from fastapi import FastAPI, HTTPException

def calculate_bmi(height_feet: int, height_inches: int, weight: float, age: int):
	if age < 13:
	    raise HTTPException(status_code=400, detail="Age not valid")
	else:
		height = (height_feet * 30.48 + height_inches * 2.54)
		weight = round(weight,2)
		bmi = round((weight * 10000) / (height **2),2)
		return bmi, round(height,2)

	
