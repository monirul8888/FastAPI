from fastapi import FastAPI
from pydantic import BaseModel, AnyUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app=FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host="localhost", 
            database="university", 
            user="postgres", 
            password="1234", 
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Successfully Connected to Database")
        break
    except Exception as error:
        print("Not Connected")
        print(f"Error : {error}")
        time.sleep(2)


class Student(BaseModel):
    name: str
    id: int
    dept: str
    phone: int


@app.post("/student")
def create_student(post: Student):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                '''INSERT INTO student ("Name", "ID", "Dept", "Phone")
                   VALUES (%s, %s, %s, %s)
                   RETURNING *''',
                (post.name, post.id, post.dept, post.phone)
            )

            new_post = cursor.fetchone()
            conn.commit()

        return {"student": new_post}

    except Exception as e:
        conn.rollback()   # ⭐ VERY IMPORTANT
        return {"error": str(e)}





@app.get("/")
def home():
    return {"message": "Welcome To Fast-API Thanks...!"}



@app.get("/home")
def home():
    return {"message": "Welcome To Home Page"}


@app.get("/student")
def view_students():
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    return {"students": data}

