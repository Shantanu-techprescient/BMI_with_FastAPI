
def write_comment(name: str, age: int, height: float, weight: float, bmi: float) -> str:
	category = ""
	if bmi < 18.5:
		category = "Underweight"
	elif (18.5 <= bmi <= 24.9):
		category = "Healthy-Weight"
	elif (25.0 <= bmi <= 29.9):
		category = "Overweight"
	else:
		category = "Obese"
	
	comment = "Hi {} You are {} years old with a height of {} cm and your BMI is {}. Scientifically, you're in the {} category.".format(name, age, height, bmi, category)
	with open('bmi-info.txt','a') as bmi_file:
	    bmi_file.write(comment)
	    bmi_file.write('\n')
	
	return comment
