from fastapi.encoders import jsonable_encoder


def show_data():
	'''
	This function shows all the previous comments stored in bmi-info.txt file.
	'''
	comment_list = list()
	with open("bmi-info.txt","r") as bmi_file:
		for line in bmi_file:
			comment_list.append(line[:-1])

	dump_data = jsonable_encoder(comment_list[::-1])
	return dump_data