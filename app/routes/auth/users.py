from fastapi import APIRouter
# lets connect to the database 
from mysql.connector import connect

db = connect(
    host="localhost",
    user="root",
    password="Password@1234",
    database="temple"
)

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_name}")
async def get_users(user_name: str):
    return [{"username": f"{user_name}"},{"Role": "Owner of Biggest Tech Empire Rules in every field."}]

# lets fetch data from database where id = user_name
@router.get("/fetch/{user_id}")
async def get_user_by_id(user_id: int):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    return result
