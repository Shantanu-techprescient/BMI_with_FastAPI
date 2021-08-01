# BMI_with_FastAPI
  
This API is developed in python using FastAPI to calculate BMI of the user and store the response in a SQLite database.  
  
  
Instructions:  
Step 1: Install required libraries  
-> pip install fastapi  
-> pip install pydantic  
-> pip install uvicorn
-> pip install sqlalchemy
-> pip install python-multiport

Step 2: Open Command prompt and change directory where program files are present  

Step 3: type in terminal "uvicorn main:app --reload"  

Step 4: Open web browser and go to localhost  

step 5:  In the url section type "http://127.0.0.1:8000/docs" which will open swagger. Swagger is a ui for testing api. Here you'll see the 'Authorize' Button.
To test every api, you need to first authorize your self. Default username = 'shantanu' and password = 'password'. If you didn't authorized, on testing every api, you'll see response {"details" : "Not authenticated"}

Option 1: Calculate BMI  
Here you can enter name, age(yrs), weight(kgs), height(cms) and then execute it. age should be greater than 12yr, weight should be greater than 45.50kgs and height should be greater than 152.40cms. If the data is not valid, api will raise exception for each invalid data. If the all the data is valid, then after execution of api, it will add the data in database and will return json response containing name, age, height, weight, bmi and last updated data.  

Option 2: Delete BMI from db.


This will delete the bmi previously stored in db. User have to enter the name to be deleted. if the name is not in db then the api will raise exception saying 'User Not Found'. If the user is present in db, then it will delete the recoed from the db and we will get the response 'User Deleted Successfully'

Option 3: Updated the Bmi. 


with the help of this api, user can update their previously calculated bmi. user will need to enter the name and other optional parameters (age, height, weight). if the name is found in db, then the data will get updated and the new calculated bmi (if user updates weight or height or both) will be stored. If the name is not found in db, then api will raise exception 'User Not Found'.

Option 4: Read Bmi. 


with the help of this api, we can view previously stored users data in db. here we can also apply filter (name , age) and can also view data using pagination. We can set the limit the number of rows displayed (page size) and see the data on particular page (page number).

