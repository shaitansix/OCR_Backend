from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes.imageRoute import router as imageRouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost', 'http://localhost:5173'], 
    allow_credentials = True,
    allow_methods = ['*'], 
    allow_headers = ['Content-Type']
)
app.include_router(imageRouter)

if __name__ == '__main__': 
    port = 8000
    uvicorn.run(app, port = port)