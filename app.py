from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="todo"
)
mycursor = mydb.cursor()
app = FastAPI()


@app.get("/tasks")
def read_tasks():
    mycursor.execute("SELECT * FROM tasks")
    myresult = mycursor.fetchall()
    return myresult

@app.post("/tasks")  
def add_tasks(id:int = Form(None), title:str = Form(),description:str = Form(), time:str = Form(), status:int = Form(None)):
    if status is None:
        status= 0
    mycursor.execute(f"INSERT INTO tasks (id, title, description,time, status) VALUES ('{id}','{title}', '{description}', '{time}', '{status}')")
    mydb.commit()
    return read_tasks()

@app.delete("/tasks/{id}")  
def delete_tasks(id: int):
    mycursor.execute(f"SELECT * FROM tasks WHERE id ='{id}'")
    myresult = mycursor.fetchone()    
    if myresult != None:
      mycursor.execute(f"DELETE FROM tasks WHERE id = '{id}'")
      mydb.commit() 
      return read_tasks()
    else:
        raise HTTPException(status_code=404, detail="task not found")
    
@app.put("/tasks/{id}")  
def update_tasks(id: int, title:str = Form(None), description:str = Form(None), time:str = Form(None), status:int = Form(None)):
    mycursor.execute(f"SELECT * FROM tasks WHERE id ='{id}'")
    myresult = mycursor.fetchone()    
    if myresult != None:
        if title is None:
            title= myresult[1]
        if description is None:
            description= myresult[2]
        if time is None:
            time= myresult[3]    
        if status is None:
            status= myresult[4]        
            
        mycursor.execute(f"UPDATE tasks SET title = '{title}', description = '{description}', time = '{time}', status = '{status}' WHERE id = {id}")
        mydb.commit()
        return read_tasks()      
    else:
        raise HTTPException(status_code=404, detail="task not found")    