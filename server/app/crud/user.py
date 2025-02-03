from sqlalchemy.orm import Session, joinedload
from app.models.user import User
from app import schemas
import bcrypt

def get_users(db:Session, skip: int = 0 , limit:int = 100):
    return db.query(User).options(joinedload(User.role)).offset(skip).limit(limit).all()

def show_user(db:Session,id:int):
    return db.query(User).options(joinedload(User.role)).filter(User.id == id) .first()

def update_user(db:Session, id:int, user_update:schemas.UserUpdate):
    user = db.query(User).filter(User.id == id).first()
    if user:
        if user_update.email:
            user.email = user_update.email
        if user_update.role_id:
            user.role_id = user_update.role_id
        db.commit()
        db.refresh(user)
        return user
    return None        
            
def delete_user(db:Session, id:int):
    user = db.query(User).filter(User.id ==id).first()
    if user:
        db.delete(user)
        db.commit()

def hash_pass(password:str)->str:
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password.encode('utf-8'),salt)
    return password_hashed.decode('utf-8')
    
def create_user(db:Session, user_add:schemas.UserCreate):
    password = hash_pass(user_add.password_hash)
    user = User(username= user_add.username,role_id=user_add.role_id, email=user_add.email, password_hash = password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user