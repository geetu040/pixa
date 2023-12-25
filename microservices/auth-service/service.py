import mysql.connector
from fastapi.responses import JSONResponse
from config import HOST, DATABASE, USER, PASSWORD

connection = mysql.connector.connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=3306,
    database=DATABASE,
)
cursor = connection.cursor()

create_user_query = "INSERT INTO users (username, password) VALUES ('{}', '{}');"
verify_user_query = "SELECT * FROM users WHERE username = '{}';"

def create_user(username, password):
    try:
        cursor.execute(create_user_query.format(username, password))
        connection.commit()
        return JSONResponse("user created")
    except Exception as e:
        connection.rollback()
        return JSONResponse(str(e), 500)

def verify_user(username, password):
    try:
        cursor.execute(verify_user_query.format(username))
        result = cursor.fetchone()

        if result is None:
            return JSONResponse('invalid username', 201)
        elif result[1] == password: 
            return JSONResponse("valid")
        else:
            return JSONResponse('invalid password', 400)
    except Exception as e:
        return JSONResponse(str(e), 500)