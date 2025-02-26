from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes.imageRoute import router as imageRouter
from schemas.responseSchema import responseEntity

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost', 'http://localhost:5173', 'https://ocr-frontend-phi.vercel.app'], 
    allow_credentials = True,
    allow_methods = ['*'], 
    allow_headers = ['Content-Type']
)

app.include_router(imageRouter)
# @app.get('/{full_path:path}')
# async def not_found(full_path: str):
#     return responseEntity(
#         state = 'Success', 
#         message = 'La ruta no existe'
#     )

if __name__ == '__main__': 
    port = 8000
    uvicorn.run(app, port = port)