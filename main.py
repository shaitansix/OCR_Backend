from fastapi import FastAPI
from routes.imageRoute import router as imageRouter
from routes.notFound import router as notFoundRouter
from config.cors import corsSetup

app = FastAPI()
corsSetup(app)

app.include_router(imageRouter)
app.include_router(notFoundRouter)