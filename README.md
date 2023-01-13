### Django project
python version: 3.10.8

#### Description
This is a test django project. The database used is sqlite3.    

#### API supported
/api/tasks -> GET : Retrieve a list of all tasks.  
  
/api/tasks/{uuid} -> GET: Retrieve the task with the specified uuid.  
  
/api/tasks/ -> POST: Create the task.  
payload: {  
    "title": "task1",  
    "description": "1234 bla"  
}  
  
/api/tasks/{uuid}/ -> PUT: Update the task.  
payload: {  
    "title": "new task",  
    "description": "1234 bla"  
}  
  
/api/tasks/{uuid}/ -> PATCH: Partially update the task.  
payload: {  
    "completed": true  
}  
  
/api/tasks/{uuid}/ -> DELETE: Delete the task.  
  
#### Searching API
/api/tasks?completed=false -> GET: Retrieve a list of all tasks where completed is set to false (vice versa for true).  
/api/tasks?search=some%20text -> GET: Retrieve a list of all tasks where title OR description include the substring "some%20text".  
/api/tasks?search=some%20text&completed=false -> GET: Retrieve a list of all tasks where completed is set to true AND (title OR description include the substring) "some%20text".  

#### Create and activate virtual environment: 
1. python3 -m venv venv
2. source venv/bin/activate (on unix systems)

#### Install dependencies (previous step obligatory)
1. python -m pip install -r requirements.txt

#### Run Project (previous step obligatory)
1. export SECRET="random_string" (this is needed to populate the environmental variable for app SECRET_KEY)
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver
