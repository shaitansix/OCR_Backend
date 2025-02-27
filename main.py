from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from routes.imageRoute import router as imageRouter
from routes.notFound import router as notFoundRouter
from config.cors import corsSetup

app = FastAPI()
load_dotenv('.env')
corsSetup(app)

app.include_router(imageRouter)
app.include_router(notFoundRouter)

if __name__ == '__main__': 
    PORT = int(os.getenv('PORT', 8000))
    uvicorn.run(app, port = PORT)