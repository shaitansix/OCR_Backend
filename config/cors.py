from fastapi.middleware.cors import CORSMiddleware

def corsSetup(app): 
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ['http://localhost', 'http://localhost:5173', 'https://ocr-frontend-phi.vercel.app'], 
        allow_credentials = True,
        allow_methods = ['*'], 
        allow_headers = ['Content-Type']
    )