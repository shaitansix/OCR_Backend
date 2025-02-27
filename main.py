from fastapi import FastAPI
import uvicorn
from routes.imageRoute import router as imageRouter
from routes.notFound import router as notFoundRouter
from config.cors import corsSetup

app = FastAPI()
corsSetup(app)

app.include_router(imageRouter)
app.include_router(notFoundRouter)

if __name__ == '__main__': 
    port = 8000
    uvicorn.run(app, port = port)