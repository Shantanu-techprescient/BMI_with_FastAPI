
def write_comment(name: str, age: int, height: float, weight: float, bmi: float, category: str) -> str:

	'''
	This function writes the bmi result on bmi-info.txt file.
	:para name: name of the user
	:type name: str
	:para age: age of the user
	:type age: int
	:para height: height of the user in cms
	:type height: float
	:para weight: weight of the user
	:type weight: float
	:para bmi: bmi of the user
	:type bmi: float
	:para category: bmi category of the user
	:type category: str
	'''
	
	comment = "Hi {} You are {} years old with a height of {} cm and your BMI is {}. Scientifically, you're in the {} category.".format(name, age, height, bmi, category)
	with open('bmi-info.txt','a') as bmi_file:
	    bmi_file.write(comment)
	    bmi_file.write('\n')
	
	return comment
