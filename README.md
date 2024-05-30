# To-Do App with SQLite Database and FastAPI

This Python project is a to-do app that connects to a MySql database using FastAPI to provide a RESTful API for managing tasks.

## Features
- Create new tasks
- View existing tasks existing tasks
- Update task status
- Delete tasks

## Installation
1. Clone the repository:
```
git clone https://github.com/AbdollahRamezani/PyDeploy_04.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the FastAPI server:
```
uvicorn todo:app --reload
```

4. Access the API documentation:
Open your web browser and go to http://127.0.0.1:8000/docs to interact with the API.

## Usage
- Use the provided Swagger UI or OpenAPI documentation to test the API endpoints.
- Create, read, update, and delete tasks as needed.

## API Endpoints
- /read_tasks (GET): Get all tasks
- /insert_task (POST): Add a new task
- /update_task/{id} (PUT): Update a task's title, description, time or status
- /delete_task/{id} (DELETE): Delete a task

## Technologies Used
- Python
- FastAPI
- Mysql
