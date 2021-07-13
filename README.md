# BMI_with_FastAPI
  
This API is developed in python using FastAPI to calculate BMI of the user and store the response in a text file.    
  
  
Instructions:  
Step 1: Install required libraries  
-> pip install fastapi  
-> pip install pydantic  
-> pip install uvicorn  

Step 2: Open Command prompt and change directory where program files are present  

Step 3: type in terminal "uvicorn main:app --reload"  

Step 4: Open web browser and go to localhost  

step 5:  
Option 1: Calculate BMI  
in the url section type "http://127.0.0.1:8000/docs" which will open swagger. Swagger is a ui for testing api.  
in the post api section , click on "Try it Out". Then you can see "Request Body" section.  
Here you can enter valid name, age, weight(kgs), height(feet and inches seperately) and then execute it.  
After executing it you'll get the result in response.  

Option 2: See previous results  
in the url section , type "http://127.0.0.1:8000/show". This will show you the previous results stored in the file(bmi-info.txt)
