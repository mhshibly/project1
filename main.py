# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# import uvicorn

# app= FastAPI()

# @app.get("/blog")

# def index(limit= 10, published: bool= True, sort: Optional[str]= None):
    
#     if published:
#         return {'data': f'{limit} Published Blogs form database'}
#     else:
#         return {'data': f'{limit} Blogs form database'}





# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data": "All unpublished blogs"}




# @app.get('/blog/{id}')
# def show(id: int):
#     return {'data': id}




# @app.get("/blog/{id}/comments")

# def comments(id):
#     return{'data': {"1", "2"}}


# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]

# @app.post('/blog')
# def create_blog(requst: Blog):
#     return {'data': f"Blog is created with {requst.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port= 9000)

