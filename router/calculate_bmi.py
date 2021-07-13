from fastapi import FastAPI, HTTPException

def calculate(height_feet: int, height_inches: int, weight: float, age: int):
	'''
	This function calculates the bmi value and return bmi and height(in cms).
	
	:para weight : this is user's weight
	:type weight : float
	:para age : age of the user. if age is less than 13yrs, then the function raises an exception
	:type age : int
	:para height_feet : height(ft) of the user
	:type height : int
	:para height_inches : height(inchs) of the user 
	:type height : int

	'''
	if age < 13:
	    raise HTTPException(status_code=400, detail="Age not valid")
	else:
		height = (height_feet * 30.48 + height_inches * 2.54)
		weight = round(weight,2)
		bmi = round((weight * 10000) / (height **2),2)
		return bmi, round(height,2) 
	

def bmi_category(bmi):
	'''
	This function decides the category based on the given bmi value.
	:para bmi: This value is used to decide the bmi category
	:type bmi: float

	'''
	category = ""
	if bmi < 18.5:
		category = "Underweight"
	elif (18.5 <= bmi <= 24.9):
		category = "Healthy-Weight"
	elif (25.0 <= bmi <= 29.9):
		category = "Overweight"
	else:
		category = "Obese"

	return category