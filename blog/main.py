from fastapi import FastAPI, Depends, HTTPException, status
from . import schemas
from . import database
from . database import engine, SessionLocal
from . import models
from sqlalchemy.orm import Session
from blog import database


app= FastAPI()
get_db = database.get_db
models.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create

@app.post('/blog', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {'detail': f'successfully created blog with ID {new_blog.id}'}
 
 # read all

@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs



 # READ

@app.get('/blog/{id}')
def show(id,response:Response, db: Session = Depends(get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code= status.H, status.HTTP_404_NT_FOUND)
    #     detail= f'blog with {id} not found'
    return blog


